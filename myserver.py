from flask import Flask
from threading import Thread

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, World!"


def run():
    app.run(host="0.0.0.0", port=8080)


def server_on():
    server = Thread(target=run)
    server.daemon = True  # ทำให้ปิดตามโปรแกรมหลัก
    server.start()
