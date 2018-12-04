from flask import Flask, render_template
import model

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <img src="/static/blockM.png"/>
        <h1>Michigan Sports Info!</h1>
        <ul>
            <li><a href="/bball"> Men's Basketball </a></li>
        </ul>
    '''

@app.route('/bball')
def bball():
    return render_template("seasons.html", seasons=model.get_bball_seasons())

if __name__ == '__main__':
    app.run(debug=True)
