import json
from tweepy import OAuthHandler, Stream, StreamListener
from datetime import datetime
import dotenv
import os

# Cadastrar as chaves de acesso
dotenv.load_dotenv(dotenv.find_dotenv())
consumer_key = os.getenv("consumer_key")
consumer_secret = os.getenv("consumer_secret")

access_token = os.getenv("access_token")
access_token_secret = os.getenv("access_token_secret")

# Definir arquivo de saída para armazenar os tweets coletados
data_hoje = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
out = open(f"collected_tweets{data_hoje}.txt", "w")


# Implementar uma classe para conexão com twitter
class MyListener(StreamListener):

    def on_data(self, data):
        item_string = json.dumps(data)
        out.write(item_string + "\n")
        return True

    def on_error(self, status):
        print(status)


# Implementar nossa função MAIN
if __name__ == '__main__':
    l = MyListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=["Trump"])
