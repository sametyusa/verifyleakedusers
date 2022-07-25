import csv, time, pdb, json, random
import logging, requests

logger = logging.getLogger(__name__)

def uploadFile(f):
    #Uploads CSV file to server
    randomNumber = random.randint(1,10000)
    filename='media/'+str(randomNumber)+f.name
    with open(filename, 'wb+') as ufile:  
        for chunk in f.chunks():  
            ufile.write(chunk) 
    return filename

def testCredsByAPI(filename):
    creds = {}
    credResult = {}
    apiurl='' #Put service URL here
    try:
        with open(filename, 'r') as nfile:
            reader=csv.reader(nfile,delimiter=',', lineterminator='\\n')
            for row in reader:    
                creds[row[0]] = row[1]
        for c in creds:
            if "@" in c:
                postCred={"credentialType": "EMAIL","password": creds[c],"userCredential": c}
            else:
                postCred={"credentialType": "USERNAME","password": creds[c],"userCredential": c}
            logger.error(json.dumps(postCred))
            postRequest = requests.post(apiurl,data=json.dumps(postCred),headers={"Content-Type": "application/json"})
            logger.error(postRequest.text)
            responseJson = postRequest.json()
            loginResult = responseJson["data"]["result"]
            credResult[c] = loginResult
        return credResult
    except UnicodeDecodeError:
        #user didn't upload a CSV file
        credResult = {
            'error':'Only CSV files are allowed'
        }
        return credResult