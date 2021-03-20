import pyaudio
import wave
import numpy as np 
from scipy import fftpack
import os
import time
import webrtcvad
import speech_recognition as sr 

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK_DURATION_MS = 30       # supports 10, 20 and 30 (ms)
PADDING_DURATION_MS = 1500   # 1 sec jugement
CHUNK_SIZE = int(RATE * CHUNK_DURATION_MS / 1000)  # chunk to read
CHUNK_BYTES = CHUNK_SIZE * 2  # 16bit = 2 bytes, PCM
NUM_PADDING_CHUNKS = int(PADDING_DURATION_MS / CHUNK_DURATION_MS)
NUM_WINDOW_CHUNKS = int(240 / CHUNK_DURATION_MS)
# NUM_WINDOW_CHUNKS = int(400 / CHUNK_DURATION_MS)  # 400 ms/ 30ms  ge
NUM_WINDOW_CHUNKS_END = NUM_WINDOW_CHUNKS * 2



def rec(file_path='./data/audio_user.wav',rate=16000):
    r = sr.Recognizer()
    with sr.Microphone(sample_rate=rate)as source:
        print("please say something")
        try:
            audio = r.listen(source, timeout=5)
        except sr.WaitTimeoutError as e:
            print(e)
            return None


    with open(file_path, 'wb')as f:
        f.write(audio.get_wav_data())

    return file_path


def record_sound(file_path='./data/audio_user.wav'):
    # 录音，有声音自动写入文件，默认为'test.wav'，声音结束后录音也停止，调用一次，录制一个片段
    vad = webrtcvad.Vad(3) # 这个参数可为1，2，3，可改变灵敏度，越大越粗犷
    pa = pyaudio.PyAudio()
    print("录音开始")
    stream = pa.open(format=FORMAT,
                     channels=CHANNELS,
                     rate=RATE,
                     input=True,
                     start=False,
                     # input_device_index=2,
                     frames_per_buffer=CHUNK_SIZE)
 
    got_a_sentence = False
    leave = False
    no_time = 0
 
    while not leave:
        ring_buffer = collections.deque(maxlen=NUM_PADDING_CHUNKS)
        triggered = False
        voiced_frames = []
        ring_buffer_flags = [0] * NUM_WINDOW_CHUNKS
        ring_buffer_index = 0
 
        ring_buffer_flags_end = [0] * NUM_WINDOW_CHUNKS_END
        ring_buffer_index_end = 0
        buffer_in = ''
        # WangS（原作者的名字，就喜欢这种造轮子的人）
        raw_data = array('h')
        index = 0
        start_point = 0
        StartTime = time.time()
        print("* recording: ")
        stream.start_stream()
 
        while not got_a_sentence and not leave:
            chunk = stream.read(CHUNK_SIZE)
            # add WangS
            raw_data.extend(array('h', chunk))
            index += CHUNK_SIZE
            TimeUse = time.time() - StartTime
 
            active = vad.is_speech(chunk, RATE)
 
            sys.stdout.write('1' if active else '_')
            ring_buffer_flags[ring_buffer_index] = 1 if active else 0
            ring_buffer_index += 1
            ring_buffer_index %= NUM_WINDOW_CHUNKS
 
            ring_buffer_flags_end[ring_buffer_index_end] = 1 if active else 0
            ring_buffer_index_end += 1
            ring_buffer_index_end %= NUM_WINDOW_CHUNKS_END
 
            # start point detection
            if not triggered:
                ring_buffer.append(chunk)
                num_voiced = sum(ring_buffer_flags)
                if num_voiced > 0.8 * NUM_WINDOW_CHUNKS:
                    sys.stdout.write(' Open ')
                    triggered = True
                    start_point = index - CHUNK_SIZE * 20  # start point
                    # voiced_frames.extend(ring_buffer)
                    ring_buffer.clear()
            # end point detection
            else:
                # voiced_frames.append(chunk)
                ring_buffer.append(chunk)
                num_unvoiced = NUM_WINDOW_CHUNKS_END - sum(ring_buffer_flags_end)
                if num_unvoiced > 0.90 * NUM_WINDOW_CHUNKS_END or TimeUse > 10:
                    sys.stdout.write(' Close ')
                    triggered = False
                    got_a_sentence = True
 
            sys.stdout.flush()
 
        sys.stdout.write('\n')
        # data = b''.join(voiced_frames)
 
        stream.stop_stream()
        print("* done recording")
        got_a_sentence = False
 
        # write to file
        raw_data.reverse()
        for index in range(start_point):
            raw_data.pop()
        raw_data.reverse()
        raw_data = normalize(raw_data)
        record_to_file(file_path, raw_data, 2)
        leave = True
 
    stream.close()
    print("录音结束")
    return file_path

def recording(filename='./data/audio_user.wav', time=5, threshold=7000):
    """
    filename: 文件名
    time:录音时间
    threshold:判断录音结束的阀值
    """

    # 块大小
    CHUNK = 1024
    # 每次采集的位数
    FORMAT = pyaudio.paInt16
    # 声道数
    CHANNELS = 1
    # 采样率：每秒采集数据的次数
    RATE = 16000
    # 录音时间
    RECORD_SECONDS = time
    WAVE_OUTPUT_FILENAME = filename
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    print("* 录音中...")

    frames = list()

    if time > 0:
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
    else:
        stopflag = 0
        stopflag2 = 0
        while True:
            data = stream.read(CHUNK)
            rt_data = np.frombuffer(data, np.dtype('<i2'))
            # print(rt_data*10)
            # 傅里叶变换
            fft_temp_data = fftpack.fft(rt_data, rt_data.size, overwrite_x=True)
            fft_data = np.abs(fft_temp_data)[0:fft_temp_data.size // 2 + 1]

            # 测试阈值，输出值用来判断阈值
            # print(sum(fft_data) // len(fft_data))

            # 判断麦克风是否停止，判断说话是否结束，# 麦克风阈值，默认7000
            if sum(fft_data) // len(fft_data) > threshold:
                stopflag += 1
            else:
                stopflag2 += 1
                oneSecond = int(RATE / CHUNK)
                if stopflag2 + stopflag > oneSecond:
                    if stopflag2 > oneSecond // 3 * 2:
                        break
                else:
                    stopflag2 = 0
                    stopflag = 0
            frames.append(data)
    print("* 录音结束")
    stream.stop_stream()
    stream.close()
    p.terminate()
    with wave.open(WAVE_OUTPUT_FILENAME, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

    return filename

def play():
    os.system('sox ./data/audio_machine.mp3 ./data/audio_machine.wav')
    wf = wave.open('./data/audio_machine.wav', 'rb')
    p = pyaudio.PyAudio()
 
    def callback(in_data, frame_count, time_info, status):
        data = wf.readframes(frame_count)
        return (data, pyaudio.paContinue)
 
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True,
                    stream_callback=callback)
 
    stream.start_stream()
 
    while stream.is_active():
        time.sleep(0.1)
 
    stream.stop_stream()
    stream.close()
    wf.close()
 
    p.terminate()


def play_sound():
    CHUNK = 512
    # 播放声音文件，默认为'test.wav'
    os.system('sox ./data/audio_machine.mp3 ./data/audio_machine.wav')
    wf = wave.open('./data/audio_machine.wav', 'rb')
    p = pyaudio.PyAudio()
 
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
 
    data = wf.readframes(CHUNK)
 
    while data != b'':
        stream.write(data)
        data = wf.readframes(CHUNK)
    stream.stop_stream()
    stream.close()
    p.terminate()
    return
 

