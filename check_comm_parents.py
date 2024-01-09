# -*- coding: utf-8 -*-

"""
@author: Dinesh

This file orders comments by the link on which they were posted, for each subreddit and for each month.
We finally have smaller files in csv format that makes parsing easier through pandas

"""

#type prefixes
#t1_	Comment
#t2_	Account
#t3_	Link
#t4_	Message
#t5_	Subreddit
#t6_	Award


import json
from operator import itemgetter 
import pandas as pd

json_file = open('./filtered_data/RC_2017-12.json', 'rb')
json_obj = json.loads(json_file.read())

subreddits_order = ["soccer", "Gunners", "reddevils", "LiverpoolFC", "chelseafc", "coys", "Barca", "realmadrid", "MCFC", "fcbayern", "borussiadortmund", "everton", "NUFC", "ACMilan", "Juve", "Hammers", "avfc", "CelticFC", "SaintsFC", "ASRoma", "benfica", "psg", "lcfc", "atletico", "FCInterMilan"]
df1 = pd.DataFrame()

for subreddit in subreddits_order:
    print(subreddit)
    if(subreddit not in json_obj.keys()):
        continue
    json_obj_considered = json_obj[subreddit]
    json_obj_considered = sorted(json_obj_considered, key=itemgetter('link_id', 'created_utc'))
    df = pd.DataFrame(json_obj_considered)
    df1 = df1.append(df)
    
#parent_ids = [i['parent_id'] for i in json_obj_considered]
#link_ids = [i['link_id'] for i in json_obj_considered]

#parent_ids = list(set(parent_ids))
#link_ids = list(set(link_ids))

df1.to_csv('RC_2017-12-GroupPost.csv')

'''
k=0
for i in parent_ids:
    indices = []
    k+=1
    print(k)
    for j,obj in enumerate(json_obj_considered):
        if(i==obj['parent_id']):
            indices.append(j)
    parent_children_json[i] = indices
    
list1 = [15808, 15914, 16172, 16173, 16174, 16175, 16176, 16177, 16178, 16179, 16180, 16181, 16182, 16183, 16184, 16185, 16514]
for i in list1:
    print(json_obj_considered[i]['body'])
    print("\n\n")
    
    
for i in json_obj_considered:
    if(i['parent_id']=='t1_dfxfu7d'):
        obj = {}
        obj['body'] = i['body']
        obj['link_id'] = i['link_id']
        obj['subreddit'] = i['subreddit']
        obj['id'] = i['id']
        obj['author'] = i['author']
        obj['parent_id'] = i['parent_id']
        print(obj)
        print("\n")
        
with open("lcfc_RC_2017-04.json", "w") as fp:
    json.dump({'lcfc':json_obj['lcfc']}, fp)
''' 
    
    

