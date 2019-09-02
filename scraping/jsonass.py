import urllib.request, urllib.parse, urllib.error
import json
import ssl


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter Location: ')
uh = urllib.request.urlopen(url, context=ctx)
print('Retrieving',url)
data = uh.read().decode()


try:
    js = json.loads(data)       # refer w3 schools on conversion from python dict to json strings  
except:							# so js is a py dict
    js = None

if not js or 'status' not in js or js['status'] != 'OK':
    print('==== Failure To Retrieve ====')
    #print(data)
    #quit()

i = len(js["comments"])-1
l = list()
while i!=-1:
	l.append(js["comments"][i]["count"])
	i = i-1
print(sum(l))


#print(json.dumps(js, indent=4))  # so bacically dumps converts python dicts into json strings


#l = list()
#i = len(js["comments"])-1  # here u retrieve the length of the list of dectionaries that is present in key "comments"
#    l.append(js["comments"][i]["count"]) # first access dict js,within that access key comments which is a list, within comments access firlst ele i.e comments[0] and within that access the data of count 
    #i = i-1

#print(sum(l))


#rint(sum)
