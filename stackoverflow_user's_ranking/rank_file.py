#@akash_singh
#The rank_func is responsible for assigning the rank to the stackoverflow user profile
#based on their reputation value.
#This method creates a 'log.csv' file to store the results and also updates their rank is their reputation changes.

from os import path
import pandas as pd

def rank_func(rep, url):
    if path.exists('log.csv'):
        df = pd.read_csv('log.csv')
        # checking if the entry of the user is already in log.csv file.
        if (url == df['url']).any():
            # checking for any change is user's 'stackoverflow' reputation.
            if ((df['url'] == url) & (df['rep'] != rep)).any():
                mask = (df['url'] == url) & (df['rep'] != rep)
                df['rep'][mask] = rep
                df['rep'] = df.rep.astype(int)
                df['Rank'] = df['rep'].rank(ascending=False)
                df.sort_values('Rank', inplace=True)
                df.to_csv('log.csv', index=False)
        #if user don't exit then add and update log.csv file withh new updated ranking
        else:
            new_rank = df['Rank'].max() + 1
            data = {'url': [url],
                    'rep': [rep],
                    'Rank': [new_rank]}
            df1 = pd.DataFrame(data)
            df = df.append(df1, ignore_index=True)
            df['rep'] = df.rep.astype(int)
            df['Rank'] = df['rep'].rank(ascending=False)
            df.sort_values('Rank', inplace=True)
            df.to_csv('log.csv', index=False)
    #if the log.csv doen't exit then create the file, and make user's entry in it.
    else:
        df = pd.DataFrame({'url': [url], 'rep': [rep]})
        df['Rank'] = df['rep'].rank(ascending=1)
        df.to_csv('log.csv', index=False)
