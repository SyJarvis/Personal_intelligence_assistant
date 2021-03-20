from aip import AipSpeech
from settings import Baidu_Error, Baidu_conf




class BaiduApi():
	def __init__(self):
		pass

def get_file_content(filePath):
	with open(filePath, 'rb') as fp:
		return fp.read()


def listen(filename):
	if filename is None:
		return None
	client = AipSpeech(Baidu_conf['APP_ID'],
					Baidu_conf['API_KEY'],
					Baidu_conf['SECRET_KEY'])

	result = client.asr(get_file_content(filename), 'wav', 16000, {
			'dev_pid':1537,
		})
	if result['err_no'] == 0:
		return result['result'][0]
	else:
		for i in Baidu_Error:
			if i == result['err_no']:
				print("百度API_listen_err_no:{}".format(Baidu_Error[i]))
		# print(result['err_no'])
	"""{'corpus_no': '6717853199092486983', 
	'err_msg': 'success.',
	 'err_no': 0, 
	 'result': ['我是绝色美男不要对我动歪脑筋'], 
	 'sn': '624506842501564122084'}"""

def speak(tex="", cuid='zh', spd=5, pit=5, vol=5, per=1):
	client = AipSpeech(Baidu_conf['APP_ID'],
					Baidu_conf['API_KEY'],
					Baidu_conf['SECRET_KEY'])
	result = client.synthesis(tex, cuid, 1, {
			'spd': spd,
			'pit': pit,
			'vol': pit,
			'per': per,
		})
	if isinstance(result, dict):
		for i in Baidu_Error:
			if i == result['err_no']:
				print("百度API_speak_err_no:{}".format(Baidu_Error[i]))
				return 
	else:
		with open('./data/audio_machine.mp3', 'wb') as f:
			f.write(result)




