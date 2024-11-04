from flask import Flask, render_template, session, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)
moment = Moment(app)

class InfoForm(FlaskForm):
    name = StringField('Informe o seu nome', validators=[DataRequired()])
    surname = StringField('Informe o seu sobrenome', validators=[DataRequired()])
    institution = StringField('Informe a sua Instituição de ensino', validators=[DataRequired()])
    course = SelectField('Informe a sua disciplina', choices=[('Gestão de Projetos', 'Gestão de Projetos'), ('DSWA5', 'DSWA5'), ('DWBA4', 'DWBA4'), ('Estatística', 'Estatística')], validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InfoForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['surname'] = form.surname.data
        session['institution'] = form.institution.data
        session['course'] = form.course.data
        session['ip_remoto'] = request.remote_addr
        session['user_agent'] = request.user_agent.string
        session['host_aplicacao'] = request.host
        session['timestamp'] = datetime.utcnow() 
        return redirect(url_for('index'))
    
    return render_template(
        'index.html',
        form=form,
        name=session.get('name', 'Estranho'),
        surname=session.get('surname'),
        institution=session.get('institution'),
        course=session.get('course'),
        ip_remoto=session.get('ip_remoto'),
        user_agent=session.get('user_agent'),
        host_aplicacao=session.get('host_aplicacao'),
        current_time=session.get('timestamp') or datetime.utcnow()
    )

if __name__ == '__main__':
    app.run(debug=True)
