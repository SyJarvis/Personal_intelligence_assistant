from robot import robot, xiaosi
from baidu_api import listen, speak
from audio_processing import recording, play, play_sound, record_sound, rec
from api_services import get_weather
import sys
import os
import sys
from xunfei_api import xunfeispeak
import time

print("开始1")
BASC_URL = os.getcwd()
sys.path.append(os.path.join(BASC_URL, 'snowboy'))

from snowboy import snowboydecoder
import sys
import signal
interrupted = False
def signal_handler(signal, frame):
    global interrupted
    interrupted = True

def interrupt_callback():
    global interrupted
    return interrupted


def start():
    print("开始3")
    time.sleep(0.5)
    speak('我在')
    play_sound()
    while True:
        text = None
        print("listen_start")
        text = listen(rec())
        print("listen_end")
        with open('./msg1.yaml', 'a+') as f:
            f.write('- - %s'%text)
            f.write('\n')
        # text = input('请输入想说的话:')
        if text == '闭嘴':
            break
        if text != None:
            print('you said:' + text)
            print("robot")
            speak(xiaosi(text))
            print("robot2")
            play_sound()
        else:
            break


model = './snowboy/扶苏.pmdl'
signal.signal(signal.SIGINT, signal_handler)
detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
detector.start(detected_callback=start,
               interrupt_check=interrupt_callback,
               sleep_time=0.03)


if __name__ == '__main__':
    print("开始2")
    detector.terminate()
