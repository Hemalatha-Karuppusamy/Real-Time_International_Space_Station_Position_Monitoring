import requests, json, time, pymongo, pandas as pd
client = pymongo.MongoClient("mongodb+srv://iam_hema:<password>@hemz.fo3int4.mongodb.net/?retryWrites=true&w=majority")
db = client['ISS']
col = db['satellite']
for i in range(12):
  time.sleep(5)
  sat = requests.get('http://api.open-notify.org/iss-now.json')
  x = sat.text
  f = json.loads(x)
  col.insert_one(f)
sat_list = []
for i in col.find({},{'_id':0}):
  sat_list.append(i)
df = pd.DataFrame(sat_list)
df[['longitude','latitude']] = df['iss_position'].apply(lambda i:pd.Series([i['longitude'],i['latitude']]))
df.drop('iss_position',axis = 1,inplace = True)
