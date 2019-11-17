from flask import Flask, render_template, url_for, flash, redirect
from flask import Flask, request, render_template, send_from_directory
from forms import RegistrationForm, LoginForm
import pandas as pd
import numpy as np
import jinja2,os
import os
from twitterscraper.query import query_user_info
import pandas as pd 
from multiprocessing import Pool
from IPython.display import display
from twitterscraper import query_tweets
from uuid import uuid4

import jinja2
from flask import render_template


app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

def get_user_info(twitter_user):
    user_info = query_user_info(user= twitter_user)
    twitter_user_data = {}
    twitter_user_data["user"] = user_info.user
    twitter_user_data["fullname"] = user_info.full_name
    twitter_user_data["location"] = user_info.location
    twitter_user_data["blog"] = user_info.blog
    twitter_user_data["date_joined"] = user_info.date_joined
    twitter_user_data["id"] = user_info.id
    twitter_user_data["num_tweets"] = user_info.tweets
    twitter_user_data["following"] = user_info.following
    twitter_user_data["followers"] = user_info.followers


    twitter_user_data["likes"] = user_info.likes

    # List of users the tweet is a reply to
    twitter_user_data["lists"] = user_info.lists
    
    return twitter_user_data

#APP_ROOT = os.path.dirname(os.path.abspath("__file__"))
app.jinja_loader=jinja2.FileSystemLoader(r'C:\Users\SAMARTH G VASIST\flask projects\templates')
app._static_folder = r"C:\Users\SAMARTH G VASIST\flask projects\static"

@app.route("/")

@app.route("/home")

def home():
    flash('Welcome to Root Intelligence', 'success')
    return render_template('home.html')




@app.route("/upload", methods=["POST"])

def upload():

    
    

    text = request.form['firstname']
    """# return send_from_directory("images", filename, as_attachment=True)
    
    #users = []
    #users.append(text)  
    # i+=1    

    # Calling user info function through callback, append to the list containing everything
    # POOL - FOR DATA PARALLELISM - EG RUNNING MAPS
    pool = Pool(8)    
    for user in pool.map(get_user_info,users):
        twitter_user_info.append(user)

    cols=['id','fullname','date_joined','location','blog', 'num_tweets','following','followers','likes','lists']
    data_frame = pd.DataFrame(twitter_user_info, index=users, columns=cols)
    data_frame.index.name = "Users"
    data_frame.sort_values(by="followers", ascending=False, inplace=True, kind='quicksort', na_position='last')
    # elapsed = time.time() - start
    # print(f"Elapsed time: {elapsed}")
    print(data_frame)
    x=data_frame.to_string()
    return text"""

    data=pd.read_csv(r'finalelect3.csv')

    for i in range(len(data)):
   # print(data.loc[i,"Names"])
        if data.loc[i,"Names"]==text:
            k=data.iloc[i].tolist()
        #k=k.join("  ")
            sent=k[1]+"   "+k[2]+"   "+k[3]
            return sent
            break;

    




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