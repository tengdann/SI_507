from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    html = '''
        <h1> Hello World! </h1>
        <a href='/about'> Go to about page </a>
        <br><br>
        <a href='/counter'> Go to counter page </a>
    '''
    return html
    
@app.route('/about')
def about():    
    html = '''        
        <h1> About this Site </h1>        
        <p> This is my first ever Flask website! </p>      
        <a href='/'> Go back home </a>    
    '''    
    return html
    
ctr = 0
@app.route('/counter')
def counter():    
    global ctr    
    ctr += 1
    html = '''
        <h3> {} </h3>
        <a href='/'> Go back home </a>
    '''.format(str(ctr))
    return html

if __name__ == '__main__':  
    print('starting Flask app', app.name)  
    app.run(debug=True)