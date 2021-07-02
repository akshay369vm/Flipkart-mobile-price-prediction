
import numpy as np
import pandas as pd
import requests
import re
from bs4 import BeautifulSoup
page_num=input("Enter the page number")


name=[]
processor=[]
storage=[]
battery=[]
ram=[]
rom=[]
xtd=[]
price=[]
Battery=[]
Processor=[]
for i in range(1,int(page_num)+1):
    
    url=("https://www.flipkart.com/search?q=mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&as-pos=1&as-type=RECENT&suggestionId=mobiles%7CMobiles&requestId=b6e7f7ad-fa27-47a6-90de-61f680311991&as-backfill=on&p%5B%5D=facets.price_range.from%3D10000&p%5B%5D=facets.price_range.to%3DMax&page="+str(i))
    
    req=requests.get(url)
    
    content=BeautifulSoup(req.content,'html.parser')
    #print(content)
    
    page=content.find_all('ul',{"class":"_1xgFaf"})
    #print(processor)
    
    
    
    Phone_brand=content.find_all('div',{"class":"_4rR01T"})
    Price=content.find_all('div',{"class":"_30jeq3 _1_WHN1"})
    
    for i in Phone_brand:
        name.append(i.text)
        
    for i in Price:
        i=i.text
        price.append(re.sub("₹",'',i))
    
    
    
    for i in page:
        details = i.find_all("li")
        
        try:
            storage.append(details[0].text)
        except:
            storage.append('nan')
 
        try:
            battery.append(details[3].text)
        except:
            battery.append('nan')
            
        try:
            if ('Processor' in details[3].text):
                processor.append(details[3].text)
            else:
                processor.append(details[4].text)
        except:
            processor.append('nan')
        


#print(processor)
#print(len(processor))

for i in battery:
    if re.match("\w{1,12}[\s]mAh",i):
        Battery.append(re.findall("\w{1,12}[\s]mAh",i))
    else:
        Battery.append('nan')


for i in processor:
    i=re.sub('[^\w\s]','',i)
    if("Processor" in i):
        Processor.append(i)
    else:
        Processor.append('nan')

    


for i in storage:

    if re.match("[0-9]+[\s]GB[\s]RAM",i):
        ram.append(re.findall("[0-9]+[\s]GB[\s]RAM",i))
    else:
        ram.append('nan')

  
     
    try:
        rom.append(re.findall("[0-9]+[\s]GB[\s]ROM",i))
    except:
        rom.append('nan')
        
             
    try:
        xtd.append(re.findall(r"Expandable[\s]Upto[\s][0-9]+[\s][A-Z]+",i))
    except:
        xtd.append('nan')
        

        
xtdm=[]

for i in xtd:
    if len(i)==0:
        xtdm.append('nan')
    else:
        xtdm.append(i)


ram = [''.join(ele) for ele in ram]  

rom = [''.join(ele) for ele in rom] 

Battery = [''.join(ele) for ele in Battery] 

xtdm = [''.join(ele) for ele in xtdm]     
        
#print(len(name))    
#print(len(ram))
#print(len(rom))
#print(len(xtdm))
#print((ram))
#print(len(Processor))
#print((Battery))

data={"Name":name,"RAM":ram,"ROM":rom,"Extended_memory":xtdm,"Battery":Battery,"Processor":Processor,"Price":price}
df=pd.DataFrame(data)
print(df)
df.to_csv('flipkart1.csv', index=False)
