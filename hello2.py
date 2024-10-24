from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def home():
    return render_template('index.html', current_time=datetime.utcnow())

@app.route('/user/<name>/<pront>/<org>')
def user(name, pront, org):
    return render_template('user.html', name=name, pront=pront, org=org)

@app.route('/contextorequisicao/<name>')
def contextorequisicao(name):
    user_agent = request.headers.get('User-Agent')
    ip_remoto = request.remote_addr
    host_aplicacao = "https://brafero.pythonanywhere.com/"
    return render_template('contextorequisicao.html', name=name, user_agent=user_agent, ip_remoto=ip_remoto, host_aplicacao=host_aplicacao)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

