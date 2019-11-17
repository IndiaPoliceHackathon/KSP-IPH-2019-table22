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
import urllib.request
import json
import sys
import os
import jinja2
from flask import render_template
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, SentimentOptions, EmotionOptions, KeywordsOptions, SemanticRolesOptions, CategoriesOptions
import pandas as pd
from textblob import TextBlob
from spacy.lang.en import English
from spacy.matcher import Matcher

natural_language_understanding=NaturalLanguageUnderstandingV1(version='2018-11-16',iam_apikey='0-d8QaCUmVksWZfJcAaHTRWGppP85p-xF5HBMkuPlY9n',url='https://gateway-lon.watsonplatform.net/natural-language-understanding/api')
#print("Imported")
import spacy

nlp=spacy.load("en_core_web_md")
nlp_sent=English()
sentencizer=nlp_sent.create_pipe("sentencizer")
nlp_sent.add_pipe(sentencizer)



app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'


#APP_ROOT = os.path.dirname(os.path.abspath("__file__"))
app.jinja_loader=jinja2.FileSystemLoader(r'C:\Users\SAMARTH G VASIST\flask projects\templates')
app._static_folder = r"C:\Users\SAMARTH G VASIST\flask projects\static"

@app.route("/")

@app.route("/home")

def home():
    flash('Welcome to Root Intelligence', 'success')
    return render_template('home.html')


@app.route("/infoga", methods=["POST"])
def info():
    text= "python phoneinfoga.py -n +91"+num
    os.system(text)



@app.route("/upload", methods=["POST"])

def upload():

    
    

    text = request.form['firstname']
    phone=request.form['num']
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
    data = urllib.request.urlopen("https://search5.truecaller.com/v2/search?q="+phone+"&countryCode=&type=4&locAddr=&placement=SEARCHRESULTS,HISTORY,DETAILS&adId=&clientId=1&myNumber=lS59d72f4d1aefae62ba0c1979l_Dl7_DEj9CPstICL1dRnD&registerId=645710775").read()

    parsed = json.loads(data)
    k=json.dumps(parsed["data"], indent=4, sort_keys=True)
    
    
  


    



    
    
    
    
    for i in k.splitlines():
        if "firstName" in i:
            print(i)
            x=i
        if "id" in i:
         #   print(i)
            y=i
        if "lastName" in i:
            print(i)
            w=i
        if "name" in i:
            print(i)
            a=i
        if "countryCode" in i:
            print(i)
            b=i
        if "dialingCode" in i:
            print(i)
            c=i
   # return x+"  "+w+"  "+a+"  "+b+"  "+c
    data=pd.read_csv('finalelect3.csv')

    for i in range(len(data)):
   # print(data.loc[i,"Names"])
        if data.loc[i,"Names"]==text:
            k=data.iloc[i].tolist()
        #k=k.join("  ")
            sent=k[1]+"   "+k[2]+"   "+k[3]
            cont= x+"  "+y+"  "+w+"  "+a+"  "+b+"  "+c+"<br><br>"+sent
            
            return render_template('newpolice.html',x=x,y=y,w=w,a=a,b=b,c=c,sent=sent)
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