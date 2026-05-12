# # # JSON: FILE HANDLING
# # #json.load(): to load the json files.
# # #json.dump(): to dump/create/store file/dictionary from other to create new json.abs


# # import json

# # with open("data.json", 'r') as file:
# #     data = json.load(file)
# #     print(data)
# #     print(data.keys())
# #     print(data['name'])

# # datas = {
# #     "name": "Krishnaa",
# #     "age": 8,
# #     "address": "Nepal",
# #     "Number": 90000,
# #     "Class": 18,
# #     "Hometown": "Dhulikhel"
# # }

# # with open("datas.json", 'w') as file:
# #     json.dump(datas, file, indent = 4)


# # XAMPP: Install/ database; 

# # Request library
# # api: it is like a waiter, who takes the role of middlemen, taking order and passing info to the backend developer
# # it is a key in which the 
# # To request api, 
# # To install requests: Syntax: pip install requests

# # XML: html

# # API
# #rest base
# #sop 
# #graphic ql: 

# # Right-click: inspect; 
# # Then, Network; refresh
# # Copy Url

# # Method
# # get request: server bata data liney
# # post request:

# # url

# # status code
# # 200, 201 : to accept the data as given
# # 400, 401
# # 403: Forbidden
# # 500: server not found

# # check the data type; json file ma huncha

# import requests
# url = "https://www.onlinekhabar.com/wp-json/okapi/v1/trending-posts?limit=3"


# r = requests.get(url=url)
# print(r)
# if r.status_code == 200:
#     print("Successfully fetch")
#     result = r.json()
#     final= result['data']['news']
#     for i in final:
#         print("Post id" ,i['post_id'])
#         print("Tile", i['title'])
#         print("Link",i['link'])

# else:
#     print("No data")

# url = "https://nepsealpha.com/ajax/gold-price?fsk=0swR4o8m&range=30d&fs=20260422am"
# r = requests.get(url=url)
# print(r)

# NRB API documentation

import requests
url = "https://www.nrb.org.np/api/forex/v1/rates?page=1&per_page=1&from=2025-03-03&to=2025-03-05"

# r = requests.get(url = url)

# if r.status_code == 200:
#     result = r.json()
#     data = result['data']['payload']
#     for i in data:
#         print(i['date'])
#         for j in i['rates']:
#             print(j)

# url = "https://www.nrb.org.np/api/forex/v1/rates?page=1&per_page=10&from=2025-03-01&to=2025-03-10"

# while True:
#     r = requests.get(url=url)
#     if r.status_code == 200:
#         result = r.json()['data']['payload']
#         for i in result:
#             print("Date: ",i['date'])
#             for j in i['rates']:
#                 print(j)
#         pagination = r.json()['pagination']
#         if pagination.get('next') is None:
#             break
#         url = pagination.get('next')
#     else:
#         break

from tabulate import tabulate
header = ['iso3','name','unit','buy','sell']
url = "https://www.nrb.org.np/api/forex/v1/rates?page=1&per_page=10&from=2025-03-01&to=2025-03-10"

while True:
    r = requests.get(url = url)
    if r.status_code == 200:
        result = r.json()['data']['payload']
        for i in result:
            print(i['date'])
            final_result = []
            for j in i['rates']:
                data = [
                    j['currency']['iso3'],
                    j['currency']['name'],
                    j['currency']['unit'],
                    j['buy'],
                    j['sell']
                ]
                final_result.append(data)
            print(tabulate(final_result, header, tablefmt="grid"))
        pagination = r.json()['pagination']
        if pagination.get('next') is None:
            break
        url = pagination.get('next')
    else:
        break