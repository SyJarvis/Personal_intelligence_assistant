from chatterbot import ChatBot 
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import pymysql
pymysql.install_as_MySQLdb()

chatbot = ChatBot('xiaorou', storage_adapter='chatterbot.storage.SQLStorageAdapter',
        database_uri='mysql://root:mysql0220@127.0.0.1:3306/chatbot_message?charset=utf8mb4')


#chatbot.trainer.export_for_training('./msg.yaml')
#trainer = ChatterBotCorpusTrainer(chatbot)


#trainer.train("chatterbot.corpus.chinese.msg")

while True:
    text = input("you said:")
    if text == 'bye':
        break
    response = chatbot.get_response(text)
    print("xiaorou said:", response)
