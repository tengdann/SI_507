from flask import Flask, render_template

app = Flask(__name__)

@app.route('/name/<nm>')
def hello_name(nm):
    return render_template('name.html', name=nm)

if __name__ == '__main__':
    app.run(debug=True)