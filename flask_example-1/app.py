from os import path
from flask import (
    Flask,
    render_template,
)
app = Flask(__name__)
# Created instance of an class FLASK 

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/profile/<string:username>')
def profile(username:str)-> None: 
    return f" <h1>Hello Mr.<i>{username}</i></h1>"

@app.route('/id/<int:id>')
def id(id: int)-> None:
    return f"<code> Userid = {id} </code>"

@app.route('/userpath/<path:subpath>')
def userpath(subpath:any)-> any:
    path = []
    path.append(subpath)
    return f"subpathlist :  {path}"

if __name__ == "__main__":
     # Calling run funcation for suning flask app 
    app.run(debug=True,)