import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
serviceurl = 'http://py4e-data.dr-chuck.net/json?'
api_key = 42

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address          # so the address u are entering is going into a dict parms
    parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms) # see this urlencode function is to add the entered address in required format to the url
                                                     # it adds & for spaces and so on...ex: sri rampura = sri&rampura 


    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()                       # file in utf-8 to unicode which basically has json data
    print('Retrieved', len(data), 'characters')


    try:
        js = json.loads(data)  # here parsing json data u got and js is a py dict....pls rem the function of this loads and dumps....very imp
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(js["results"][0]["place_id"])     #so this parsing is nothing but parsing python dict
    print(js["results"][0]["formatted_address"])
    #print(json.dumps(js, indent=4))
