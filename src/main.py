from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth
from textblob import TextBlob
from sklearn.linear_model import LinearRegression
import pickle

from config.config import config
#from config import BASIC_AUTH_USERNAME, BASIC_AUTH_PASSWORD

colunas = ['tamanho','ano','garagem']
modelo = pickle.load(open('models/modelo.sav','rb'))

print(config)

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = config['BASIC_AUTH_USERNAME']
app.config['BASIC_AUTH_PASSWORD'] = config['BASIC_AUTH_PASSWORD']

basic_auth = BasicAuth(app)

@app.route('/')
def home():
    return "Minha primeira API."

@app.route('/sentiment/<inputs>')
@basic_auth.required
def sentiment(inputs):
    tb = TextBlob(inputs)
    polaridade = tb.sentiment.polarity
    return "polarity: {}".format(polaridade)

app.run(debug=True)