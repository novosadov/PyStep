from flask import Flask
from flask import request
from werkzeug import secure_filename

def resume():
    ''' <html>
    <head>
    <b>
    <center><i><font size=7>Портфолио!</font></i></center>
    </b>
    </head>

    <body BGCOLOR="#FFFFCC", text = "#111111">
    <p>

    <p>
    <table border=5 align=center text = "#ff0000">
    <tr>
    <td>
    <center><i><h2>Новосадов Павел Александрович!</h2></i></center>
    <td>
    </tr>
    <tr>
    <td>
    <img src="https://pp.userapi.com/c10969/u78750690/-6/w_7e3e9f36.jpg" align=center width="900" height="700" alt="Новосадов Павел Александрович"> 
    </td>
    </tr>
    </table>
    </p>
    </p>
    <table border=3 align=center >
    <tr>
    <td>
    111
    </td>
    <td>
    222
    </td>
    <td>
    333
    </td>
    </tr>
    <tr>
    <td>
    1111
    </td>
    <td>
    222
    </td>
    <td>
    333
    </td>
    </tr>
    <tr>
    <td>
    1111
    </td>
    <td>
    222
    </td>
    <td>
    333
    </td>
    </tr>
    </table>
    </body>
    </html> '''

 

app = Flask(__name__)

@app.route('/')
def index():
    return resume()

@app.route('/hello')
def hello():
    return 'Hello World'

@app.route('/hello2')
def hello2():
    return 'Hello World2'




if __name__ == '__main__':
    app.run(host='0.0.0.0')
