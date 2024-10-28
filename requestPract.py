import requests


url = 'https://jsonplaceholder.typicode.com/posts'

data = {
    'title': 'hashim',
    'body': 'khan',
    'userId': 1,
}

headers = {'Content-type': 'application/json; charset=UTF-8'}

allPosts = requests.post(url,headers=headers,json=data,)

print(allPosts.text)
print(allPosts.headers)