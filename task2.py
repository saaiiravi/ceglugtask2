import csv

fields=['id','name','price','rotten']

numlist=[]
fruitlist=[]
rottenlist=[]
pricelist=[]
newnumlist=[]
newfruitlist=[]
newpricelist=[]
newrottenlist=[]

with open("number.csv",'r') as op1:
	a=csv.reader(op1)
	for i in a:
		for j in i:
			dic={}
			dic['id']=j		
			numlist.append(dic)


with open("fruits.csv",'r') as op2:
	b=csv.reader(op2)
	for i in b:
		for j,d in zip(i,numlist):
			d['name']=j
			fruitlist.append(d)


with open("price.csv",'r') as op3:
    c=csv.reader(op3)
    for i in c:
        for j,d in zip(i,fruitlist):
            d['price']=j
            pricelist.append(d)

with open("rotten.csv",'r') as op4:
    d=csv.reader(op4)
    for i in d:
        for j,d in zip(i,pricelist):
            d['rotten']=j
            rottenlist.append(d)


a=0
for d in pricelist:
    if(d['id']==''):
        if(a%2==0):        
            a=a+1
        else:
            d['id']=int(a)
            a=a+1
            newnumlist.append(d)
    else:
        a=a+1
        newnumlist.append(d)

l=len(newnumlist)
a=0
for n in newnumlist:
    if(n['name']==''):
        n['name']=newnumlist[(int(a)-10)%l]['name']
        newfruitlist.append(n)
        a=a+1
    else:
        newfruitlist.append(n)
        a=a+1
        
for n in newfruitlist:
    if(n['price']==''):
        n['price']=float(0.00)
        newpricelist.append(n)
    else:
        newpricelist.append(n)

for n in newpricelist:
    if(n['rotten']=="1"):
        n['rotten']="t"
        n['price']=float(0.00)
        newrottenlist.append(n)
    elif(n['rotten']=="0"):
        n["rotten"]="f"
        newrottenlist.append(n)
    elif(n['rotten']=="t"):
         n['price']=float(0.00)
         newrottenlist.append(n)
    else:
        newrottenlist.append(n)
    
        

with open("output.csv",'w') as op6:
    w=csv.DictWriter(op6,fieldnames=fields)
    w.writeheader()
    w.writerows(newrottenlist)
        
        
    
 
        
    
            
        
