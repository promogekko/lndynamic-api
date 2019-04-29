from lndynamic import LNDynamic

with open(r"/home/hme/commands.txt") as hpass:
    lines = hpass.readlines()

api = LNDynamic(lines[0].rstrip('\n'), lines[1].rstrip('\n'))
results = api.request('vm', 'list')
print(results)
val = (results.get("vms"))
#print type(val)
#print (val[0])
#print type(val[0])
print len(val)
for i  in range(0,len(val)):
    for key, value in val[i].items():
        if key == 'name':
            print('name=',value)
        if key =='primaryip':
            print('ip=',value)
        if key == 'plan_id':
            print('plan_id=',value)
api.request("vm","create",{'hostname':'user2','plan_id' : 89 ,'region' :'toronto', 'set_password': 'lawn-vex', 'image_id': 148497})
#results = api.request('vm', 'info', {'vm_id': '51ed49a3-1332-4fdb-82d5-5facae99c6d1'})
#print ("-----------------------")
#print (results)

#results = api.request('image', 'list')
#print(results)
