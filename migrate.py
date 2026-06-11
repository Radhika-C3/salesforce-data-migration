import csv
accounts={}
with open('migrateorg-accounts.csv','r') as f:
    for row in csv.DictReader(f):
        accounts[row['Name']]=row['Id']
contacts=[]
with open('contacts-with-account.csv','r') as f:
    for row in csv.DictReader(f):
        aid=accounts.get(row.get('Account.Name',''),'')
        if aid:
            contacts.append({'Email':row['Email'],'AccountId':aid})
with open('update-contacts.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['Email','AccountId'])
    w.writeheader()
    w.writerows(contacts)
print('Done!',len(contacts),'records')
