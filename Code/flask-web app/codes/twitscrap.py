from twitterscraper.query import query_user_info
import pandas as pd 
from multiprocessing import Pool
from IPython.display import display
from twitterscraper import query_tweets


global twitter_user_info
twitter_user_info = []


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

def main():
    
    # print("Enter number of users:\n")
    # n = (int(input()))
    # i = 0
    # name = ""
    # while (i < n):
    #print("Enter username:")
    name = "BillGates"
    users.append(name)  
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
    print(x)
    print(type(x))
    display(data_frame)
    data_frame.to_csv(r'User_Data.csv')
    
    # pd.DataFrame(twitter_user_info)

if __name__ == '__main__':
    # list_of_tweets = query_tweets("Trump OR Clinton", 10)

    # #print the retrieved tweets to the screen:
    # for tweet in query_tweets("Trump OR Clinton", 10):
    #     # print(tweet)
    #     print(type(tweet))

    # #Or save the retrieved tweets to file:
    # file = open("output.txt","a+")
    # for tweet in query_tweets("Trump OR Clinton", 10):
    #     file.write(tweet)
    # file.close()
    main()