# -*- coding: utf-8 -*-
import json

file_names = ["RC_2017-01", "RC_2017-02", "RC_2017-03", "RC_2017-04", "RC_2017-05", "RC_2017-06", "RC_2017-07", "RC_2017-08", "RC_2017-09", "RC_2017-10",  "RC_2017-11", "RC_2017-12"]
line_counts = []


# Names of subreddits to be extracted
# For Now, Focus on top 6-8 subreddits (most conflicts as has most number of subscribers)
subreddits_order = ["soccer", "Gunners", "reddevils", "LiverpoolFC", "chelseafc", "coys", "Barca", "realmadrid", "MCFC", "fcbayern", "borussiadortmund", "everton", "NUFC", "ACMilan", "Juve", "Hammers", "avfc", "CelticFC", "SaintsFC", "ASRoma", "benfica", "psg", "lcfc", "atletico", "FCInterMilan"]
names_order = ["Soccer", "Arsenal", "Manchester_United", "Liverpool", "Chelsea", "Tottenham", "Barca", "Real_Madrid", "Manchester_City", "Bayern", "Dortmund", "Everton", "Newcastle","AC_Milan", "Juventus", "West_Ham", "Aston_Villa", "Celtic", "Southampton", "Roma", "Benfica", "PSG", "Leicester", "Atletico_Madrid", "InterMilan"]

no_of_subreddits = len(subreddits_order)
print("No. of subreddits considered :", no_of_subreddits, len(names_order))

for i in range(len(file_names)):
    json_file = open('E:\\Reddit comments\\' + file_names[i],'rb') 
    line_counts.append(sum(1 for i in json_file))
    print(line_counts[-1])
    json_file.close()

# Store each subreddit  data in a separate file
comment_objects = {}

for i in range(11,12):
    json_file = open('E:\\Reddit comments\\' + file_names[i],'rb') 
    print("Total no. of comments in " + file_names[i] + ":", line_counts[i])
    count = 0
    while(True):
        count += 1
        if(count % 200000 == 0):
            print(count)
        comment = json_file.readline()
        if(not comment and (count >= line_counts[i])):
            break
        if(not comment):
            continue
        comment_obj = json.loads(comment)
        if(("[removed]" not in comment_obj["body"]) and ("[deleted]" not in comment_obj["author"])):
            try:
                index = subreddits_order.index(comment_obj["subreddit"])
            except ValueError:
                index = -1
            if(index==-1):
                continue
            subreddit_index = subreddits_order[index]
            if(subreddit_index in comment_objects.keys()):
                comment_objects[subreddit_index].append(comment_obj)
            else:
                comment_objects[subreddit_index] = [comment_obj]
           
with open('filtered_data/'+file_names[11]+".json", "w") as fp:
    json.dump(comment_objects, fp)


authors = []
for i in comment_objects.keys():
    for j in comment_objects[i]:
        authors.append(j["author"])
        
        
        
        
        
# Converting to csv format for pandas to process easily    
"""        
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
"""


"""

# Some experiments on parent-child comments (Comment-reply)

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
"""
    
    