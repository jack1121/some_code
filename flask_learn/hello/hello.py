#-*- coding:utf-8 -*-
from flask import Flask, render_template, session, redirect, url_for, flash
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

class NameForm(Form):
    name = StringField("What's your name?", validators = [Required()])
    submit = SubmitField(u'提交')

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you changed the name !')
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('hello_world'))
    return render_template('index.html', current_time=datetime.utcnow(), form=form, name=session.get('name'))

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name = name)

@app.route('/test')
def test():
    num = [1,2,3,4,5,6,7,8,9]
    return render_template('test.html', num = num)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug = True)
