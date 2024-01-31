from flask import Flask
import telegram

Token = '6365601102:AAFCK2wKjgM3Ui88ao5YQFokIQePu98B1GE'
bot = telegram.Bot(Token)
chat_id = 6082673969

app = Flask(__name__)

@app.route('/')
def home():
    bot.send_message(chat_id=chat_id, text = "Salom Asror")
    return "Home page, Asror"

if __name__=="__main__":
    app.run(debug=True)
