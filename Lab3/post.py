import requests

def POST():
	
  #vessels=['132.239.17.225','130.161.40.153','206.117.37.7','137.165.1.113','150.244.58.161'] 
  vessels=[]
  for line in file("ipAddresses.txt","r"):
    vessels.append(line.split('/')[0])
  port = 63155
  count = 0
  for vessel in vessels:
  		url = 'http://%s'%vessel
  		url = url+":"+str(port)
  	 	count = count + 1
  	 	payload='comment:Hello%d'%int(count)
  	 	requests.post(url, data=payload) 

if __name__ == '__main__':

	POST()