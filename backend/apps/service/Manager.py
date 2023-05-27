from flask import Flask
from search import search
from suggestion import suggestion
from friendrecommend import friendrecommend
from merchantrecommend import merchantrecommend
from loginandregister import basefunction

app = Flask(__name__)

app.register_blueprint(suggestion)
app.register_blueprint(search)
app.register_blueprint(friendrecommend)
app.register_blueprint(merchantrecommend)
app.register_blueprint(basefunction)

if __name__ == '__main__':
    app.run(debug=True)
