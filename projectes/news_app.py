import secrets_data
import requests
import json


apiKey = secrets_data.apiKey


def getNews(query):
    print('Loading....')
    
    url = f'https://newsapi.org/v2/everything?q={query}&sortBy=popularity&apiKey={apiKey}'
    
    responce = requests.get(url)
    
    news = json.loads(responce.text)
    
    for article in news['articles']:
        print(f'News name: ${article['author'] if article['author'] != "None" else article['source']['name']}')
        print(f'News Title: ${article['title']}')
        print(f'New Link: ${article['url']}')
        print('---------------------------------------------')
    
    print("------------- NEWS ENDS HERE -------------")
        
        

newsTopic = input("What type news are you intrested in: ")
getNews(newsTopic)