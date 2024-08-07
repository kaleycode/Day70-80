from flask import Flask, request

app = Flask(__name__)

logins = {}
logins["sherlock"] = {"email": "sherlock@e.com", "password": "bakerstreet"}
logins["kitty"] = {"email": "kitty@e.com", "password": "meow"}
logins["harry"] = {"email": "harry@e.com", "password": "scarhead"}

@app.route("/login", methods=["POST"])

def login():
  form = request.form
  isThere = False
  details = {}
  try:
    details = logins[form["username"]]
    isThere = True
  except:
    return "Username, email or password incorrect"
  if form["email"] == details["email"] and form["password"] == details["password"]:
    return "You are logged in!"
  else: 
    return "Username, email or password incorrect"
  

@app.route('/')
def index():
  page = """
  <!DOCTYPE html>
  <html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>login</title>
    <style>
h1, p{
  text-align: center;
}
.container { 
  height: 0px;
  position: relative;
  border: none;
  text-align: center;
}
.center {
  margin: 0;
  position: absolute;
  top: 50%;
  left: 50%;
  -ms-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
  text-align: center;
}
  </style>
  </head>
  <body>
    <h1>Login</h1>
    <div class="container">
      <div class="vertical-center">
    <form method = "post" action = "/login">
      <p>Username:
      <input type = "text" name = "username" required></p>
      <p>Email: <input type = "email" name = "email" required></p>
      <p>Password: <input type="password" name="password"> </p>
      <button type = "submit">Login</button>
    </div>
  </div>
    </form>
    <script src="script.js"></script>

  </body>

  </html>"""
  return page
app.run(host='0.0.0.0', port=81)