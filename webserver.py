from flask import Flask

from threading import Thread

app = Flask('')


@app.route('/')

def home():

    return "I'm alive" + " Bot (BOTnen) is ONLINE" + " BOTnen is working as intended" + " Mail will be sent if e == event:Down_time"

def run():

  app.run(host='0.0.0.0',port=8080)

def keep_alive():  

  t = Thread(target=run)
  t.start()
