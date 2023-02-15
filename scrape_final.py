from Scweet.scweet import scrape
from Scweet.user import get_user_information, get_users_following, get_users_followers
import datetime
import glob
import os
import pandas as pd
import change_data_type
import DB_final
import matplotlib.pyplot as plt
from emosent import get_emoji_sentiment_rank

# definite variable
keyword = "cat23456"
hashTagWord = ""
startdate = "2023-1-25"
enddate = "2023-1-26"
# keyword = ""
# hashTagWord = ""
# startdate = ""
# enddate = ""

# Input keyword / hashTagWord 
while keyword == "" and hashTagWord == "":
    # Input Keyword
    print('Input the Keyword:') 
    keyword = input()

    # Input Hashtag
    print('Input the hashtag#:') 
    hashTagWord = input()

    # Check if there is one of the input A/B
    if keyword == "" and hashTagWord == "":
        print('Please input keyword / hashtag for finding tweet.')
    else:
        pass

# Input startdate with specify format
isInvalidStartDate= True
while isInvalidStartDate:
    if startdate == "":
        print('Input the start day(YYYY-MM-DD):')
        startdate = input()        
    try: 
        # try to convert startDate String to datetime 
        datetime.datetime.strptime(startdate, '%Y-%m-%d') 
        isInvalidStartDate = False
    except : 
        # print error message
        print('Please input valid date with correct format!!!!!!!')
        pass

# Input enddate with specify format
isInvalidStartDate= True
while isInvalidStartDate:
    if enddate == "":
        print('Input the end day(YYYY-MM-DD), empty = current date:')
        enddate = input()
    if enddate != "":
        try: 
            # try to convert endDate String to datetime 
            datetime.datetime.strptime(enddate, '%Y-%m-%d') 
            isInvalidStartDate = False
        except : 
            # print error message
            print('Please input valid date with correct format!!!!!!!')
            pass
    else: 
        # convert enddate to None if did not input anything
        enddate = None
        isInvalidStartDate = False

# input the word that want to check if any post mentioned (for analyze)
print('What are you looking for? (if any)')
test_keyword = input()

# print(keyword +' / '+ hashTagWord + ' / ' + str(startdate) + ' / ' + str(enddate) + ' / ' + str(test_keyword))

# Check keyword is empty or not
if keyword != '' and keyword != None:
    # find post with keyword
    data1 = scrape(words=keyword, since=startdate, until=enddate, from_account=None, interval=1,
                  headless=True, display_type="Top", save_images=False, lang=None,
                  resume=False, filter_replies=False, proximity=False, geocode=None)
    
    # add column 'keyword' to DF
    data1["Keyword"] = keyword
    print(data1)


    # tidy up data in column 'Likes' / 'Retweets' / 'Comments'  (data type & strange word)
    data1['Timestamp'] = data1[['Timestamp']].astype('datetime64')
    data1['Likes'] = data1['Likes'].apply(change_data_type.fix_numbers)
    data1['Retweets'] = data1['Retweets'].apply(change_data_type.fix_numbers)
    data1['Comments'] = data1['Comments'].apply(change_data_type.fix_numbers)

    # check data type
    # data1.info()
    
    # Connect to CockroachDB and insert record
    # DB_final.insert_record(conn, data1)
    # DB_final.conn.commit()

    # save dataframe tp pkl file for back up
    data1.to_pickle('twitter_keyword_'+keyword+'.pkl')
    # find latest pkl file & print out
    # list_of_files = glob.glob('*.pkl') 
    # latest_file = max(list_of_files, key=os.path.getctime)
    # df_keyword  = pd.read_pickle(latest_file)
    # print(df_keyword)
    


else:
    pass

# Check HashTag is empty or not
if hashTagWord != '' and hashTagWord != None:
    # find post with hashtag
    print(hashTagWord)
    data2 = scrape(hashtag=hashTagWord, since=startdate, until=enddate,from_account=None, interval=1,
              headless=True, display_type="Top", save_images=False, lang=None,
              resume=False, filter_replies=False, proximity=False, geocode=None)

    # add HashTagword to DF
    data2["Keyword"] = '#'+ hashTagWord
    print(data2)

    # tidy up data in column 'Likes' / 'Retweets' / 'Comments'  (data type & strange word)
    data2['Timestamp'] = data2[['Timestamp']].astype('datetime64')
    data2['Likes'] = data2['Likes'].apply(change_data_type.fix_numbers)
    data2['Retweets'] = data2['Retweets'].apply(change_data_type.fix_numbers)
    data2['Comments'] = data2['Comments'].apply(change_data_type.fix_numbers)

    # check data type
    # data1.info()

    # Connect to CockroachDB and insert record
    # DB_final.insert_record(conn, data2)
    # DB_final.conn.commit()

    # save dataframe tp pkl file for back up
    data2.to_pickle('twitter_hashtag_'+hashTagWord+'.pkl')
    # find latest pkl file & print out
    # list_of_files = glob.glob('*.pkl')
    # latest_file = max(list_of_files, key=os.path.getctime)
    # df_hashtag  = pd.read_pickle(latest_file)
    # print(df_hashtag)

else:
    pass