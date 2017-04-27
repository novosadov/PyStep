from flask import Flask
from flask import request
from werkzeug import secure_filename

htmltext = ''' <html>
<head>

<<meta charset="utf-8">
  <title>Меню</title>
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
<center><i><font size=7>Портфолио!</font></i></center>
</b>
</head>


<body BGCOLOR="#FFFFCC", text = "#111111">
<p>

<ul>
    <li><a href="1.html">Карьера</a></li>
    <li><a href="2.html">Образование</a></li>
    <li><a href="3.html">Курсы</a></li>
    <li><a href="4.html">Дополнительно</a></li>
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

app = Flask(__name__)

@app.route('/')
def index():
    return htmltext

@app.route('/hello')
def hello():
    return 'Hello World'

@app.route('/hello2')
def hello2():
    return 'Hello World2'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
