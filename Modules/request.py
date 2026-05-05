import requests

# response = requests.get('https://google.com')
# res1 = requests.get('https://jsonplaceholder.typicode.com/todos/1')
# print(res1.json())
posreq = requests.post('https://jsonplaceholder.typicode.com/posts', data={'title': 'foo', 'body': 'bar', 'userId': 1})
print(posreq.json())