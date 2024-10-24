# A very simple Flask Hello World app for you to get started with...
from flask import Flask, request, make_response, redirect, abort
app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
        <head>
            <title>Avaliação contínua: Aula 030</title>
        </head>
        <body>
            <h1>Avaliação contínua: Aula 030</h1>
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/identificacao/Matheus%20Braga/PT3025446/IFSP">Identificação</a></li>
                <li><a href="/contextorequisicao">Contexto da requisição</a></li>
            </ul>
        </body>
    </html>
    '''
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)

@app.route('/contextorequisicao')
def contextorequisicao():
    user_agent = request.headers.get('User-Agent')
    ip_remoto = request.remote_addr
    host_aplicacao = "https://brafero.pythonanywhere.com/"

    return '''
    <html>
        <head>
            <title>Contexto da Requisição</title>
        </head>
        <body>
            <h1>Avaliação contínua: Aula 030</h1>
            <h2><b>Seu navegador é:</b> {}</h2>
            <h2><b>O IP do computador remoto é:</b> {}</h2>
            <h2><b>O host da aplicação é:</b> {}</h2>
            <a href="/">Voltar</a>
        </body>
    </html>
    '''.format(user_agent, ip_remoto, host_aplicacao)

@app.route('/codigostatusdiferente')
def codigostatusdiferente():
    return '<p>Bad request</p>'

@app.route('/objetoresposta')
def objetoresposta():
    msg = '<h1>Esse site retorna cookies!</h1>'
    resp = make_response(msg)
    resp.set_cookie('MeuCookie', '42')
    return resp

@app.route('/redirecionamento')
def redirecionamento():
    return redirect("https://ptb.ifsp.edu.br/")

@app.route('/abortar')
def abortar():
    return abort(404)

@app.route('/identificacao/<nome>/<prontuario>/<instituicao>')
def identificacao(nome, prontuario, instituicao):
    return '''
    <html>
        <head>
            <title>Identificação</title>
        </head>
        <body>
            <h1>Avaliação contínua: Aula 030</h1>
            <h2><b>Aluno:</b> {}</h2>
            <h2><b>Prontuário:</b> {}</h2>
            <h2><b>Instituição:</b> {}</h2>
            <a href="/">Voltar</a>
        </body>
    </html>
    '''.format(nome, prontuario, instituicao)
