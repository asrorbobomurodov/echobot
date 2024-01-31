from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Home page, Asror"

if __name__=="__main__":
    app.run()