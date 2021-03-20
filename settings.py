import os


BASA_URL = os.path


# 百度语音识别API
Baidu_conf = {
    'APP_ID':'11325424',
    'API_KEY':'b6VMHpoX5rNO0xbnIQtb3Z7O',
    'SECRET_KEY':'235f4b7283e24b589f57b97418aa6f7f',
}

"""

dev_pid	语言	模型	是否有标点	备注
1536	普通话(支持简单的英文识别)	搜索模型	无标点	支持自定义词库
1537	普通话(纯中文识别)	输入法模型	有标点	支持自定义词库
1737	英语		有标点	不支持自定义词库
1637	粤语		有标点	不支持自定义词库
1837	四川话		有标点	不支持自定义词库
1936	普通话远场	远场模型	有标点	不支持

"""
dev_pid = 1536

# 图灵机器人
# TURING_KEY = "dea1ad6480c649de84d05bb9c188c6b9"
# TURING_KEY = "88f17f853d974387af64955bed9466f4"
# URL = "http://openapi.tuling123.com/openapi/api/v2"
# HEADERS = {'Content-Type': 'application/json;charset=UTF-8'}

Baidu_Error = { 500:"不支持的输入",
                501:"输入参数不正确",
                502:"token验证失败",
                503:"合成后端错误",
                3300:"输入参数不正确",
                3301:"音频质量过差",
                3302:"鉴权失败",
                3303:"语音服务器后端问题",
                3304:"用户的请求QPS超限",
                3305:"用户的日pv（日请求量）超限",
                3307:"语音服务器后端识别出错问题",
                3308:"音频过长",
                3309:"音频数据问题",
                3310:"输入的音频文件过大",
                3311:"采样率rate参数不在选项里",
                3312:"音频格式format参数不在选项里"
                }
