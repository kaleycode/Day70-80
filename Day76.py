from flask import Flask
import datetime 
app = Flask(__name__, static_url_path="/static")
@app.route('/')
def index(): 
  page = f""" <html><body> 
  <p><a href = "/home">Go home</a></p></body></html>"""
  return page
@app.route('/home') 
def home():
  today = datetime.date.today()
  page = f"""
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>Day 76</title>
  <link href="style.css" rel="stylesheet" type="text/css"/>
</head>
<body>
  <h1>Portfolio</h1>
  <h2>Day 76 of 100 Days of Python</h2>
  <h3>The date is {today}</h3>
  <script src="script.js"></script>
  <img src="static/images/day65.png" width = 95%>
  <h4>Day 65: Classes</h4>
  <p>  I enjoyed learning about how to create classes in python. This project was probably the fastest I ever wrote this many lines of code. It came together very fast and I had lots of fun creating the characters and getting to see the data displayed on the screen in a nice way. Overall, a very smooth and happy experience.</p>
<img src="static/images/day39.png" width = 95%>
<h4>Day 39: Hangman</h4>
<p>This may have been the first assignment that I felt proud of during 100 days of python. I found it was challenging to figure out how to get the lines to show how many letters are in the word and then to disapear once the correct letter was chosen.</p>
  <img src="static/images/day71.png" width = 95%>
  <h4>Day 71: Salting</h4>
  <p>Salting is a way to keep hackers from finding the passwords of users. Extremely necessary information to know about, and it was not hard to learn. Just very important, and I am glad we used this information for both the projects for day 71 and 72.</p>
  </body>
<footer>Invisible text hehehe</footer>
</html>"""
  return page
app.run(host='0.0.0.0', port=81) 