from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'chave secretissima'

class NameForm(FlaskForm):
    nome = StringField('Informe o seu nome', validators=[DataRequired()])
    sobrenome = StringField('Informe o seu sobrenome', validators=[DataRequired()])
    org = StringField('Informe a sua Instituição de ensino', validators=[DataRequired()])
    materia = SelectField('Informe a sua disciplina', choices=[('DSWA5', 'DSWA5'), ('Outros', 'Outros')], validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        session['nome'] = form.nome.data
        session['sobrenome'] = form.sobrenome.data
        session['org'] = form.org.data
        session['materia'] = form.materia.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, nome=session.get('nome'), sobrenome=session.get('sobrenome'), org=session.get('org'), materia=session.get('materia'), ip=request.remote_addr, host=request.host)

if __name__ == '__main__':
    app.run(debug=True)
