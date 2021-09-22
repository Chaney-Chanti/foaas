import http.client
import sys
import json
import urllib

#json.loads() - json -> dictionary
#json.dumps() - dictionary -> json

if len(sys.argv) < 2:
    print("Usage: redact URL")
    sys.exit(0)

path = sys.argv[1]
print(path)
headers = {'Accept': 'application/json'}
purgomalum = "www.purgomalum.com/service"

conn = http.client.HTTPSConnection("www.foaas.com")
conn.request('GET', path, headers=headers)
r1 = conn.getresponse()
print(r1.status, r1.reason)
data1 = r1.read()  
print(data1)
dictionary = json.loads(data1)

#makes the message safe to pass into purgomalum
safeString = urllib.parse.quote(dictionary['message'], safe='/', encoding=None, errors=None)
print(safeString)
 

conn2 = http.client.HTTPSConnection("www.purgomalum.com")
conn2.request('GET', "/service/json?text="+safeString)
r2 = conn2.getresponse()
print(r2.status, r2.reason)
data2 = r2.read()  
dictionary2 = json.loads(data2)
dictionary2['subtitle'] = dictionary['subtitle']
jsonObj = json.dumps(dictionary2, indent=5)
print(jsonObj)





