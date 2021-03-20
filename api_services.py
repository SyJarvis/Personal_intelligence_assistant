from urllib import request, parse
import sys, ssl
import ast
import json

def get_quote(text):
	return parse.quote(text)

def get_unquote(text):
	return parse.unquote(text)


def get_weather(cityname=None):
	"""
		https://blog.csdn.net/qq_33160365/article/details/100036628
		获取城市代码
	"""
	num = '101280401'
	response = request.urlopen('http://t.weather.sojson.com/api/weather/city/{}'.format(num))
	j_data = json.loads(response.read().decode('utf-8'))
	text = '{},{},最高{},最低{},{}'.format(j_data['cityInfo']['city'],
											j_data['data']['forecast'][0]['type'],
											j_data['data']['forecast'][0]['high'][2:],
											j_data['data']['forecast'][0]['low'][2:],
											j_data['data']['forecast'][0]['fx'])
	return text



"""
心知天气
https://www.seniverse.com/
{
	"message":"success感谢又拍云(upyun.com)提供CDN赞助",
	"status":200,
	"date":"20200625",
	"time":"2020-06-25 00:41:23",
	"cityInfo":{"city":"梅州市",
				"citykey":"101280401",
				"parent":"广东",
				"updateTime":"00:16"},
	"data":{"shidu":"75%",
			"pm25":18.0,
			"pm10":39.0,
			"quality":"优",
			"wendu":"29",
			"ganmao":"各类人群可自由活动",
			"forecast":[{"date":"25","high":"高温 34℃","low":"低温 26℃","ymd":"2020-06-25","week":"星期四","sunrise":"05:29","sunset":"19:07","aqi":31,"fx":"西南风","fl":"2级","type":"阴","notice":"不要被阴云遮挡住好心情"},{"date":"26","high":"高温 34℃","low":"低温 26℃","ymd":"2020-06-26","week":"星期五","sunrise":"05:29","sunset":"19:07","aqi":22,"fx":"东风","fl":"1级","type":"阴","notice":"不要被阴云遮挡住好心情"},{"date":"27","high":"高温 35℃","low":"低温 25℃","ymd":"2020-06-27","week":"星期六","sunrise":"05:30","sunset":"19:08","aqi":25,"fx":"南风","fl":"2级","type":"阴","notice":"不要被阴云遮挡住好心情"},{"date":"28","high":"高温 35℃","low":"低温 25℃","ymd":"2020-06-28","week":"星期日","sunrise":"05:30","sunset":"19:08","aqi":31,"fx":"南风","fl":"2级","type":"阴","notice":"不要被阴云遮挡住好心情"},{"date":"29","high":"高温 35℃","low":"低温 25℃","ymd":"2020-06-29","week":"星期一","sunrise":"05:30","sunset":"19:08","aqi":27,"fx":"南风","fl":"2级","type":"小雨","notice":"雨虽小，注意保暖别感冒"},{"date":"30","high":"高温 35℃","low":"低温 25℃","ymd":"2020-06-30","week":"星期二","sunrise":"05:31","sunset":"19:08","aqi":18,"fx":"南风","fl":"2级","type":"小雨","notice":"雨虽小，注意保暖别感冒"},{"date":"01","high":"高温 35℃","low":"低温 25℃","ymd":"2020-07-01","week":"星期三","sunrise":"05:31","sunset":"19:08","aqi":24,"fx":"南风","fl":"1级","type":"阴","notice":"不要被阴云遮挡住好心情"},{"date":"02","high":"高温 34℃","low":"低温 24℃","ymd":"2020-07-02","week":"星期四","sunrise":"05:31","sunset":"19:08","aqi":32,"fx":"东南风","fl":"1级","type":"中雨","notice":"记得随身携带雨伞哦"},{"date":"03","high":"高温 31℃","low":"低温 24℃","ymd":"2020-07-03","week":"星期五","sunrise":"05:32","sunset":"19:08","aqi":25,"fx":"东南风","fl":"2级","type":"中雨","notice":"记得随身携带雨伞哦"},{"date":"04","high":"高温 30℃","low":"低温 23℃","ymd":"2020-07-04","week":"星期六","sunrise":"05:32","sunset":"19:08","aqi":27,"fx":"东南风","fl":"2级","type":"中雨","notice":"记得随身携带雨伞哦"},{"date":"05","high":"高温 31℃","low":"低温 24℃","ymd":"2020-07-05","week":"星期日","sunrise":"05:33","sunset":"19:08","aqi":25,"fx":"南风","fl":"2级","type":"中雨","notice":"记得随身携带雨伞哦"},{"date":"06","high":"高温 33℃","low":"低温 25℃","ymd":"2020-07-06","week":"星期一","sunrise":"05:33","sunset":"19:08","aqi":20,"fx":"南风","fl":"2级","type":"阴","notice":"不要被阴云遮挡住好心情"},{"date":"07","high":"高温 32℃","low":"低温 24℃","ymd":"2020-07-07","week":"星期二","sunrise":"05:33","sunset":"19:08","aqi":17,"fx":"南风","fl":"2级","type":"大雨","notice":"出门最好穿雨衣，勿挡视线"},{"date":"08","high":"高温 34℃","low":"低温 24℃","ymd":"2020-07-08","week":"星期三","sunrise":"05:34","sunset":"19:08","aqi":28,"fx":"南风","fl":"2级","type":"大雨","notice":"出门最好穿雨衣，勿挡视线"},{"date":"09","high":"高温 35℃","low":"低温 26℃","ymd":"2020-07-09","week":"星期四","sunrise":"05:29","sunset":"19:07","fx":"西南风","fl":"2级","type":"阴","notice":"不要被阴云遮挡住好心情"}],"yesterday":{"date":"24","high":"高温 35℃","low":"低温 26℃","ymd":"2020-06-24","week":"星期三","sunrise":"05:29","sunset":"19:07","aqi":37,"fx":"西南风","fl":"2级","type":"阴","notice":"不要被阴云遮挡住好心情"}}}
"""


