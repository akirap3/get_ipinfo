import ipinfo, json, os, time
from json import loads
from dicttoxml import dicttoxml

# set your token and handler
access_token = 'your token'
handler = ipinfo.getHandler(access_token)

# read ip list and convert dict type to xml 
with open(os.getcwd()+"\\iplist.txt",'r+') as f:
 content = f.readlines()
 content = [x.strip() for x in content]
a = handler.getBatchDetails(content)
b = json.dumps(a)
xml = dicttoxml(loads(b))

# create input.xml file and put xml content into it
f2 = open(os.getcwd()+"\\input.xml", "wb")
f2.write(xml)
time.sleep(.500)
f2.close()
time.sleep(.500)

# clean unnecessary content and save into output.xml
with open(os.getcwd()+"\\input.xml", "r", encoding = "utf8") as infile, open(os.getcwd()+"\\output.xml", "wb") as outfile:
    data = infile.read()
    time.sleep(.500)
    data = data.replace(' type="str"', '')
    time.sleep(.500)
    data = data.replace(' type="dict"', '')
    time.sleep(0.500)
    data = bytes(data, encoding = "utf8")
    time.sleep(.500)
    outfile.write(data)
    time.sleep(.500)

# close files and detete input.xml file
infile.close()
os.remove(os.getcwd()+"\\input.xml")
outfile.close()