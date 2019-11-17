from flask import Flask, render_template, url_for, flash, redirect
from flask import Flask, request, render_template, send_from_directory
from forms import RegistrationForm, LoginForm
import jinja2,os
import os

from uuid import uuid4

import jinja2
from flask import render_template


app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'



APP_ROOT = os.path.dirname(os.path.abspath("__file__"))
app.jinja_loader=jinja2.FileSystemLoader(r'C:\Users\SAMARTH G VASIST\flask projects\templates')
app._static_folder = r"C:\Users\SAMARTH G VASIST\flask projects\static"

@app.route("/")

@app.route("/home")

def home():
    flash('Welcome to Root Intelligence', 'success')
    return render_template('home.html')




@app.route("/upload", methods=["POST"])

def upload():

    target = os.path.join(APP_ROOT, 'images/')

    # target = os.path.join(APP_ROOT, 'static/')

    print(target)

    if not os.path.isdir(target):

            os.mkdir(target)

    else:

        print("Couldn't create upload directory: {}".format(target))

    print(request.files.getlist("file"))

    for upload in request.files.getlist("file"):

        print(upload)

        print("{} is the file name".format(upload.filename))

        filename = upload.filename

        destination = "/".join([target, filename])

        print ("Accept incoming file:", filename)

        print ("Save it to:", destination)

        upload.save(destination)

        print(filename)
    


    # return send_from_directory("images", filename, as_attachment=True)

        return render_template("complete1.html", image_name=filename,caption=description[9:-7])




@app.route("/about")

def about():

    return render_template('about.html', title='About')








@app.route("/login", methods=['GET', 'POST'])

def login():
    flash('Welcome to Root Intelligence','success')
    form = LoginForm()
    print(form.email.data)

    if form.validate_on_submit():

        if form.email.data == 'admin@osint.com' and form.password.data == 'root':

            flash('You have been logged in!', 'success')
            

            return render_template('default1.html') 

        else:

            flash('Login Unsuccessful. Please check username and password', 'danger')

    return render_template('login.html', title='Login', form=form)


@app.route('/try',methods=['GET','POST'])
def next():
    return render_template('default1.html')




@app.route('/upload/<filename>')

def send_image(filename):
    #print(send_from_directory("images", filename))
    return send_from_directory("images", filename)



if __name__ == '__main__':

    app.run(debug=True,use_reloader=False)