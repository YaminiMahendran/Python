import requests

from bs4 import BeautifulSoup

import urllib



url='https://www.opensecrets.org/lobby/firmbills.php?'

findata = open('D:\yamini\OpenSecrets\output12.csv','w')

def FirmID():

    lobby_csv = open('D:\yamini\OpenSecrets\LobbyistInput.csv','r') # input

    for each_line in lobby_csv:

        lobbyfirm_id = each_line.strip()

        if lobbyfirm_id[0]== 'C'or lobbyfirm_id[0]=='N':

            continue

        else:

            data(lobbyfirm_id)





        

def data(cid):

    

    cmpid= str(cid)

    y= [2018,2017,2016,2015,2014,2013,2012,2011,2010,2009,2008,2007,2006,2005,2004,2003,2002,2001,2000,1999,1998]    

    

    for i in y:

        try:

            param = {'id': cmpid, 'year':i}

            encodedParam = urllib.parse.urlencode(param)

            urlWithParam = str(url + encodedParam)

            page = requests.get(urlWithParam)

            soup = BeautifulSoup(page.content, 'html.parser')

            length =len(soup.find_all('td'))

            lst4= soup.find('h1').get_text()

            if length == 0:

                continue

            else:

                for count in range(0,length,4):

                    lst= soup.find_all('td')[count].get_text()

                    lst5= soup.find_all('td')[count+1]

                    lst6= soup.find_all('td')[count+2].get_text()

                    lst7= soup.find_all('td')[count+3].get_text()

                    

                    lst1= lst5.get_text()

                    s= lst4+"%"+str(i)+ "%" +cmpid+"%"+lst +"%" +lst1 +"%" + lst6 +"%" +lst7

                    s1=s.replace(',','')

                    print (s1)

                    findata.write (s1 + "\n")



        except:

            print ("Sorry, no records found in 2016")

            continue

    



FirmID()

   

    



