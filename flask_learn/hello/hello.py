from flask import Flask, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask.ext.wtf import Form


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def hello_world():
    return render_template('index.html', current_time=datetime.utcnow())

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
