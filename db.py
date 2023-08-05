import json

db = json.loads(open('db.json', 'r').read())

key = str(input("Enter Key: "))
value = str(input("Enter value: "))
db[key] = value

with open("db.json", 'w') as f:
    json.dump(db, f, indent='\t')

file =  json.loads(open('db.json', 'r').read())
for i in file:
    print("Key: {} \t Value: {}".format(i, file[i]))
