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

def sentiment_extraction(user_input):
    try:
        splitted=user_input.split()
        if(len(splitted)<4):
            blob=TextBlob(user_input)
            score=blob.sentiment.polarity
            return score
        else:
            sentiment=natural_language_understanding.analyze(text=user_input,
            features=Features(sentiment=SentimentOptions(user_input))).get_result()
            print(sentiment)
            dic=sentiment["sentiment"]
            doc=dic["document"]
            score=doc["score"]
            return score
    except:
        blob=TextBlob(user_input)
        score=blob.sentiment.polarity
        return score



data=pd.read_csv("output.csv")
tweets=data["tweet"]
#print("read")

tweets=tweets.tolist()
tweets=tweets[:100]
tweets2=[]

for i in tweets:
    if("pic" in i):
        pass
    else:
        tweets2.append(i)

#print("starting sentiment analysis")

sentiment=[]
for i in tweets2:
    sentiment.append(sentiment_extraction(i))


average_sentiment = sum(sentiment)/len(sentiment)
print("Average sentiment: ", average_sentiment)



if average_sentiment < 0:
    print("Mostly negative inclining sentiments")
elif average_sentiment>0 and average_sentiment<=0.4:
    print("Neutral tendencies")
else:
    print("Positive inclining tendencies")


#######Info on tweets#######
def keyword_extraction(user_input):
    user_input=user_input.strip()
    splitted=user_input.split()
    subject=''
    if(len(splitted)>3):
        keywords=natural_language_understanding.analyze(text=user_input,
        features=Features(semantic_roles=SemanticRolesOptions())).get_result()
        #print(json.dumps(keywords,indent=2))
        
        l=keywords["semantic_roles"]
        if(len(l)!=0):
            if "i" in splitted:
                semantic_roles=keywords["semantic_roles"]
                ob=semantic_roles[0]
                subject=ob["object"]
                subject=subject["text"]
            else:
                semantic_roles=keywords["semantic_roles"]
                sub=semantic_roles[0]
                subject=sub["subject"]
                subject=subject["text"]
        else:
            matcher=Matcher(nlp.vocab)
            pattern=[{'POS':'NOUN'}]
            matcher.add('NOUN_PATTERN',None,pattern)
            doc=nlp(user_input)
            for token in doc:
                #print(token.text,token.pos_)
                pass
            matches=matcher(doc)
            subs=[]
            for match_id, start,end in matches:
                #print("subject: ",doc[start:end].text)
                subs.append(doc[start:end].text)
            subject=' '.join(subs)
            
    else:
        matcher=Matcher(nlp.vocab)
        pattern=[{'POS':'NOUN'}]
        matcher.add('NOUN_PATTERN',None,pattern)
        doc=nlp(user_input)
        for token in doc:
                #print(token.text,token.pos_)
                pass
        matches=matcher(doc)
        subs=[]
        for match_id, start,end in matches:
            subs.append(doc[start:end].text)
        subject=' '.join(subs)
            

    list_of_sub=subject.split()
    #print(list_of_sub)
    return list_of_sub


for i in tweets2:
    print(keyword_extraction(i))
    print("\n")