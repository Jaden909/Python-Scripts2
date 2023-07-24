import json
save=json.load(open('SAVETEST.json'))
y={}
y["yourDad"]=0
y["yourMom"]=1
with open('SAVETEST.json','w') as f:
    json.dump(y,f)
    print(save)
u=save.get('yourMom')
print(u)