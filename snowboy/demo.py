import snowboydecoder
import sys
import signal

interrupted = False


def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted

if len(sys.argv) == 1:
    print("Error: need to specify model name")
    print("Usage: python demo.py your.model")
    sys.exit(-1)


def detected():
	print("你好")

model = sys.argv[1]
print("获取参数")
# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)
print("signal")

detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
print("创建detector")
print('Listening... Press Ctrl+C to exit')

# main loop
# detected_callback=snowboydecoder.play_audio_file,

def print_text():
    print('demo')
detector.start(detected_callback=print_text,
               interrupt_check=interrupt_callback,
               sleep_time=0.03)
print("开始执行")

detector.terminate()
print("terminate()")
