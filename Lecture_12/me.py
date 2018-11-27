from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    html = '''
        <h1> What am I? </h1>
        <br>
        <h3> Name </h3>
        <p> Danny Teng </p>
        <br>
        <h3> Hometown </h3>
        <p> Northville, MI </p>
        <br>
        <h3> Education </h3>
        <p> B.S. in Psychology, University of Michigan -- Ann Arbor, Class of 2018 </p>
        <p> Masters in Health Informatics, University of Michigan School of Information, Class of 2020 </p>
        <br>
        <h3> Picture </h3>
        <img src = "C:\\Users\\dteng\\OneDrive\\Pictures\\LORD_CHANKA.jpg">
        <br>
        <a href = '/classes'> Go to my W19 classlist </a>
        <br>
        <a href = '/resume'> Go to my resume </a>
    '''
    return html
    
@app.route('/classes')
def classes():
    html = '''
        <h1> IN PROGRESS </h1>
    '''
    return html
    
@app.route('/resume')
def resume():
    html = '''
        <h1> IN PROGRESS </h1>
    '''
    return html
    
    
if __name__ == '__main__':  
    print('starting Flask app', app.name)  
    app.run(debug=True)