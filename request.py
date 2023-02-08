import requests
# r=requests.get('https://api.github.com/users/naveenkrnl')
# print(r)
# print(r.content)




response=requests.get('https://api.github.com/')
print(response.url)
print(response.status_code)