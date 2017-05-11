from flask import Flask
from flask import request
from werkzeug import secure_filename
from flask import render_template
import webbrowser


app = Flask(__name__)

@app.route('/')
def index():
    return htmltext

@app.route('/karera')
def karera():
    webbrowser.open('1.html')
    return htmltext

@app.route('/obrazovanie')
def obrazovanie():
    return 'Hello World2'

@app.route('/kursi')
def kursi():
    return 'Hello World3'

@app.route('/dopolnitelno')
def dopolnitelno():
    return 'Hello World4'

htmltext = ''' <html>
<head>
<meta charset="utf-8">
  <title>Портфолио</title>
  <style>
   li {
    display: inline-block; /* Строчно-блочные элементы */
    background: #CA181A; /* Цвет фона */
    margin-right: 3px; /* Расстояние между пунктами меню */
    -webkit-transform: skewX(-30deg); /* Для Safari и Chrome */
    -moz-transform: skewX(-30deg); /* Для Firefox */
    -o-transform: skewX(-30deg); /* Для Opera */
    -ms-transform: skewX(-30deg); /* Для IE */
    transform: skewX(-30deg); /* CSS3 */
   }
   a {
    color: #fff; /* Цвет ссылок */
    display: block; /* Блочный элемент */
    padding: 5px 15px; /* Поля вокруг текста */
    text-decoration: none; /* Убираем подчёркивание */
    -webkit-transform: skewX(30deg); /* Для Safari и Chrome */
    -moz-transform: skewX(30deg); /* Для Firefox */
    -o-transform: skewX(30deg); /* Для Opera */
    -ms-transform: skewX(30deg); /* Для IE */
    transform: skewX(30deg); /* CSS3 */
   }
   li:hover {
    background: #333; /* Цвет фона при наведении курсора мыши */
   }
  </style>
  
<b>
<center><i><font face="Arial" size=7>Портфолио!</font></i></center>
</b>
</head>
<body BGCOLOR="#FFFFCC", text = "#111111">
<p>
<ul>
    <li><a href="/karera"><font face="Helvetica">Карьера</font></a></li>
    <li><a href="/obrazovanie"><font face="Helvetica">Образование</font></a></li>
    <li><a href="/kursi"><font face="Helvetica">Курсы</font></a></li>
    <li><a href="/dopolnitelno"><font face="Helvetica">Дополнительно</font></a></li>
  </ul>
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
</body>
</html> '''


webbrowser.open_new(
    'http://127.0.0.1:5000/')



if __name__ == '__main__':
    app.run(host='0.0.0.0')
