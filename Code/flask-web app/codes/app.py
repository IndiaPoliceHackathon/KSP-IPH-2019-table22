from flask import Flask
from flask import render_template,abort
import jinja2

app=Flask(__name__)
app.jinja_loader=jinja2.FileSystemLoader(r'C:\Users\SAMARTH G VASIST\flask projects\templates')
app._static_folder = r"C:\Users\SAMARTH G VASIST\flask projects\static"
@app.route('/home')
def index():
    return '<h1>This is the homepage</h1>'

@app.route('/test')
def test():
    
    return render_template('test.html',b="hello")



    
@app.route('/profile/<username>')
def profile(username):
    return "hello"+username

@app.route('/name')
def send():
    #print(send_from_directory("images", filename))
    return "hello"



if __name__=="__main__":
    app.run(debug=True,use_reloader=False)
    