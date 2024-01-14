key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMDAxNmI4YTYtMDQ4OC00MjU4LWFhZGItZDIxN2ZiNWQ4NTU4IiwidHlwZSI6ImZyb250X2FwaV90b2tlbiJ9.uBrNT2i_0uwZ_t37h5iyjFhfb-XHWGgeTu4yO33TTDo'

import json
import requests
import traceback

headers = {"Authorization": f'Bearer {key}'}

url = "https://api.edenai.run/v2/image/explicit_content"

High = []
Medium_High = []
Medium = []
Medium_Low = []
Low = []
Error = []

def is_adult(link):
    def status(qaz):
        q = int(str(round(qaz, 2)*100).split('.')[0])
        if q > 80:return 'High'
        elif q <= 80 and q >= 60:return 'Medium-High'
        elif q <= 60 and q >= 40:return 'Medium'
        elif q <= 40 and q >= 20:return 'Medium_Low'
        elif q < 20:return 'Low'
    
    def adding(status, url):
        print(status, url)
        if status == 'High':High.append(url)
        elif status == 'Medium_High':Medium_High.append(url)
        elif status == 'Medium':Medium.append(url)
        elif status == 'Medium_Low':Medium_Low.append(url)
        elif status == 'Low':Low.append(url)

    
    json_payload = {
        "providers": "microsoft",
        "file_url": link,
        "fallback_providers": ""
    }
    response = requests.post(url, json=json_payload, headers=headers)
    result = json.loads(response.text)
    if 'Too many requests, upgrade your plan if you need a higher rate limit.' in str(result.get('details')):
        print('Many requests')
    else:
        index = result['microsoft']['nsfw_likelihood_score']
        adding(status(index), link)
    
import json
with open('data.json', "r+") as f:data = json.load(f)
import time
for url_ in data:
    aza = {
    "High" : High,
    "Medium_High" : Medium_High,
    "Medium" : Medium,
    "Medium_Low" : Medium_Low,
    "Low" : Low,
    "Error" : Error}

    if url_ != '':
        if str(url_.split('/')[5].split('?size')[0].split('.')[-1]) in ['jpg', 'png', 'jpeg']:
            # print('IN')
            try:
                is_adult(url_)
                time.sleep(20)
            except Exception as e:
                json.dump(aza, open('SORT.json', 'w'), indent=4, default=list)
                print(url_,'not indexed')
                Error.append(url_)
                traceback.format_exc()

json.dump(aza, open('SORT.json', 'w'), indent=4, default=list)
