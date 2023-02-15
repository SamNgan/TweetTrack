import pandas as pd
import pickle

# with open('twitter_keyword_toyota_17182.pkl') as f:
#     data = pickle.load(f)

data = pd.read_pickle('twitter_keyword_toyota_17182.pkl')

df = pd.DataFrame(data)


df.fillna(0, inplace=True)

def fix_numbers(x):

    if type(x) == int:
        return x

    elif type(x) == str:
        newNumber = x.replace(",", "").replace("K", "").replace("萬", "").replace(".", "")

        if "K" in x:
            if "." in x:
                newNumber = newNumber + "00"
            else:
                newNumber = newNumber + "000"

        if "萬" in x:
            if "." in x:
                newNumber = newNumber + "000"
            else:
                newNumber = newNumber + "0000"

    try:
        return int(newNumber)
    except:
        return 0

df["Retweets"] = df["Retweets"].map(fix_numbers)

df["Likes"] = df['Likes'].str.replace(',', '')
df["Likes"] = df['Likes'].map(fix_numbers)

df["Comments"] = df['Comments'].str.replace(',', '')
df["Comments"] = pd.to_numeric(df["Comments"])

#df.info()