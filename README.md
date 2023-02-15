# JDE-Mid-Project-TemaRed
This is a tool to scrape Twitter data to explore the trend in social meida.

**Starting:**

The main pyhton package is Scweet.
Please refer to Scweet github https://github.com/Altimis/Scweet.

**For scrape Twitter data:**

1.install related package (especially Scweet)

2.Using _scrape_final.py_

There are some argument that able to modify the result, the meaning of argument as below:

Words: Words to search for.

Hashtag: Tweets containing #hashtag

Since: Start date for search query

Until : End date for search query

From_account: Tweets posted by this account

Interval : Interval days between each start date and end date for

Headless : Show the website or not

Display_type: Display type of Twitter page (Latest or Top tweets)

Lang : Tweets language

Resume: Resume the last scraping. specify the csv file path

Proximity / Geocode: Where the post was published

***The Result:***
The result will save in file output and the columns of result as below:

'UserScreenName' : User nickname

'UserName' : UserName

'Timestamp' : timestamp of the tweet

'Text' : tweet text

Embedded_text' : embedded text written above the tweet

'Emojis' : emojis in the tweet

'Comments' : number of comments

'Likes' : number of likes

'Retweets' : number of retweets

'Image link' : link of the image in the tweet

'Tweet URL' : tweet URL

**To change the datatype:**

Please use __change_data_type.py__ to change the datatype

**To send the result to related DB and using SQL to get the data:**

Please use __DB_final.py__

**The default analyses the data:**

Please use __Analytics_Jupyter.ipynb__
