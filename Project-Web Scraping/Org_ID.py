import csv
import requests
import urllib
import logging
import re

url = 'https://www.opensecrets.org/api/?method=getOrgs&apikey=11502b5e9039aefad1904ae75fbc7ab0&output=json&'

def generateFirmID():
    lobby_csv = open('D:\yamini\OpenSecrets\LobbyistInput.csv','r') # input 
    lobby_csv_output = open('D:\yamini\OpenSecrets\output11.csv','w')# output
    firstLine = True
    for each_line in lobby_csv: # Skip header and just copy it to new output file
        if firstLine:   
            lobby_csv_output.write(each_line)
            firstLine = False
            continue
        lobbyfirm_name = each_line.strip() # remove leading and trailing space
        lobbyfirm_name = lobbyfirm_name[:-2] #remove commas
        
        if lobbyfirm_name.startswith('"'): # remove double quotes
            lobbyfirm_name = lobbyfirm_name[1:]
        if lobbyfirm_name.endswith('"'):
            lobbyfirm_name = lobbyfirm_name[:-1]
        lobbyfirm_name = re.sub(r"[\t]*", "", lobbyfirm_name) #remove tabs
        print (lobbyfirm_name)
        
        lobbyId = lobbynameToIDApi(lobbyfirm_name) #api call
        s = lobbyfirm_name + ',' + lobbyId
        lobby_csv_output.write(s + "\n")

    lobby_csv.close()
    lobby_csv_output.close()
    
def lobbynameToIDApi(lobbyName):
    param = {'org': lobbyName } #lobbyName :3M Co
    encodedParam = urllib.parse.urlencode(param) #url encoding 
    print (encodedParam) #example : org=3M+Co
    urlWithParam = str(url + encodedParam)
    print (urlWithParam)
    try:
        response = requests.get(urlWithParam) #Api call
        print(response)
        print (response.json()['response']['organization']['@attributes']['orgid'])
        return response.json()['response']['organization']['@attributes']['orgid']
    except:
        """logging.exception('')""" #fail silently
    
    return ""
     #Replace this with api call

generateFirmID() #starting point
