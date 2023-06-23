import snscrape.modules.twitter as sntwitter
import pandas as pd
import csv

query = "(from:elonmusk) until:2023-01-01 since:2022-01-01"
tweets = []
limit = 500

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.username, tweet.content])
        
df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
df.to_csv('tweets.csv')


csv_path = 'Users\pendr\OneDrive\Desktop\Python\practise\SNA PROJECT\tweets.csv'
column_number = 2  

txt_path = 'Users\pendr\OneDrive\Desktop\Python\practise\SNA PROJECT\read.txt'

with open('read.txt', encoding="utf-8") as txt_file:
    
    with open('tweets.csv', encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            txt_file.write(row[column_number] + '\n')

print(txt_path)