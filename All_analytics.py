import datetime
import glob
import os
import pandas as pd
import matplotlib.pyplot as plt
import change_data_type
from emosent import get_emoji_sentiment_rank
import plotly.graph_objects as go
import plotly.io as pio
import plotly.express as px
import plotly
from emosent import get_emoji_sentiment_rank

test_keyword = 'toyota'
data1 = pd.read_pickle('twitter_keyword_tesla_21185 .pkl')
# data1.info()

data1['Timestamp'] = data1[['Timestamp']].astype('datetime64')
data1['Likes'] = data1['Likes'].apply(change_data_type.fix_numbers)
data1['Retweets'] = data1['Retweets'].apply(change_data_type.fix_numbers)
data1['Comments'] = data1['Comments'].apply(change_data_type.fix_numbers)
data1.groupby(data1["Timestamp"].dt.month)['Likes','Comments','Retweets'].mean().plot(title='Count by month',xlabel='Month(1-12)',ylabel='Count')
data1.groupby(data1["Timestamp"].dt.weekday)['Likes','Comments','Retweets'].mean().plot(title='Count by weekday',xlabel='weekday',ylabel='Count')
data1.groupby(data1["Timestamp"].dt.day)['Likes','Comments','Retweets'].mean().plot(title='Count by day',xlabel='Day(1-31)',ylabel='Count')
data1.groupby(data1["Timestamp"].dt.hour)['Likes','Comments','Retweets'].mean().plot(title='Count by Hour',xlabel='Hour(1-24)',ylabel='Count')

print(data1["Embedded_text"].str.contains(test_keyword).value_counts())
data1["Embedded_text"].str.contains(test_keyword).value_counts().plot(kind='bar')


# Analytics Emojis 
# data1['Emojis']
emoji_list = []
for i in data1['Emojis']:
    x = i.split()
    # print(x)
    
    try:
        for y in x:
            # print(y)
            emoji_list.append(y)
    except:
        pass
# print(emoji_list)

sentiment_score = []

for y in emoji_list:
    # print(y)
    try:
        z = get_emoji_sentiment_rank(y)
        sentiment_score.append(z['sentiment_score'])
    except:
        sentiment_score.append(0)
    
# print(len(sentiment_score))

emoji_count_list = {'emoji':'count'}
count_dic = []
for emoji_unique in emoji_list:
    emoji_count =  emoji_list.count(emoji_unique)
    count_dic.append(emoji_count)
print('1')
emoji_count_list['emoji'] = emoji_list
emoji_count_list['count'] = count_dic
# print(emoji_count_list)
emoji_count_df = pd.DataFrame(emoji_count_list)
# emoji_count_df.info()
print('2')
emoji_count_df['sentiment_score'] = sentiment_score
# print(emoji_count_df)
print('3')
fig = go.Figure()

fig.add_trace(go.Scatter(y=(emoji_count_df['sentiment_score']),
                x=emoji_count_df['count'],
                name='Emoji Counts',
                marker_color='white',
                orientation='h',
                text=emoji_count_df['emoji'],
                textposition='top center',
                mode='markers+text',
                textfont=dict(size=30),
                ))

fig.update_yaxes(title='score')
fig.update_xaxes(title='count')

fig.update_layout(
    template='simple_white', 
    yaxis_range=[-1,1.2],
    height=1000, width = 800,
    title="Emoji distribution",
    title_x=0.5)

plt.show()

print('done')