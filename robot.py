import requests
import json
import requests
import json
from chatterbot import ChatBot 
from chatterbot.trainers import ChatterBotCorpusTrainer
# chatbot = ChatBot('xiaorou', 
#                 storage_adapter='chatterbot.storage.SQLStorageAdapter',
#                 database_uri='mysql://root:mysql0220@127.0.0.1:3306/chatbot_meaasge?charset=utf8mb4')

def write_back_msg(text):
    with open('./msg.yaml', 'a+') as f:
        f.write('  - %s'%text)
        f.write('\n')


def xiaosi(text=""):
    if not text:
        return None
    url = 'https://api.ownthink.com/bot?appid=xiaosi&userid=user&spoken={}'.format(text)
    response = requests.get(url)
    j_data = response.json()
    text = j_data["data"]["info"]["text"]
    print("xiaosi:", text)
    write_back_msg(text)
    return text


#347b39ee228b4b109dae7270cc08d3c8
#65fd73e1a68f4fcd8c2305b2fc71b903
TURING_KEY = "40d56dcf5e1d4edc8a891eb824a11437"
URL = "http://openapi.tuling123.com/openapi/api/v2"
HEADERS = {'Content-Type': 'application/json;charset=UTF-8'}
 
def robot(text=""):
    if not text:
        return None
    data = {
        "reqType": 0,
        "perception": {
            "inputText": {
                "text": ""
            },
            "selfInfo": {
                "location": {
                    "city": "广州",
                    "street": ""
                }
            }
        },
        "userInfo": {
            "apiKey": TURING_KEY,
            "userId": "starky"
        }
    }
 
    data["perception"]["inputText"]["text"] = text
    try:
        response = requests.request("post", URL, json=data, headers=HEADERS)
    except Exception as e:
        print(e)
        raise "网络出错"
        return None

    response_dict = json.loads(response.text)
 
    result = response_dict["results"][0]["values"]["text"]
    print("tuling:" + result)
    return result

# chatbot.trainer.export_for_training('./msg.yml')


    



