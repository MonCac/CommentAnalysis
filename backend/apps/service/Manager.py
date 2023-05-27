from flask import Flask
from backend.apps.service.search import  search
from backend.apps.service.suggestion import suggestion
from backend.apps.service.friendrecommend import friendrecommend
from backend.apps.service.merchantrecommend import merchantrecommend
from backend.apps.service.LoginAndRegister import basefunction

app = Flask(__name__)

app.register_blueprint(suggestion)
app.register_blueprint(search)
app.register_blueprint(friendrecommend)
app.register_blueprint(merchantrecommend)
app.register_blueprint(basefunction)


@app.route('/hello')
def hello():
    return "nihao"


if __name__ == '__main__':
    print(11111111)
    app.run(debug=True)