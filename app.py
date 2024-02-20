from flask import Flask, render_template, request
from src.services.dengue import Requests 
import requests

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    info = Requests().data1()
    search = False
    q = request.args.get('q')
    if q:
        search = True
    return render_template('pages/index.html', texto='Olá', data=info)


if __name__ == '__main__':
    app.run(debug=True)