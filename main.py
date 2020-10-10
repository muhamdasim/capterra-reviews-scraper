from bs4 import BeautifulSoup
import requests
import json
import csv


def storeJsonFiles(i):
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    while (i <= 4250):
        url = 'https://www.capterra.com/spotlight/rest/reviews?apiVersion=2&productId=171840&from=' + str(i)
        r = requests.get(url, headers=header)
        fileName = url.replace('https://www.capterra.com/spotlight/rest/reviews?apiVersion=2&productId=171840&from=',
                               '')

        with open(fileName + '.txt', 'w') as outfile:
            json.dump(json.loads(r.text), outfile)
        print(i, " Done")
        i += 50


data = []

product = []
name = []
reviewTitle = []
date = []
overallRating=[]
Likelihood=[]
overall=[]
pros = []
cons = []
alternate = []
chosing = []
switchedFrom = []
reasonSwitch = []
url = []
source=[]


def readJsonFiles():
    i = 0
    while i <= 4250:
        with open(str(i) + '.txt') as json_file:
            data.append(json.load(json_file))

        i += 50

    for i in data:
        for k in i['hits']:
                    product.append("HubSpot Marketing Hub")
                    name.append(k['reviewer']['fullName'])
                    reviewTitle.append("HubSpot Marketing Hub Reviews")
                    dd=str(k['writtenOn']).strip()
                    dd=dd[:dd.find(' ')]
                    date.append(dd)
                    overallRating.append(str(k['overallRating'])+str("/5"))
                    Likelihood.append(str(k['recommendationRating'])+str("/10"))
                    overall.append(k['generalComments'])
                    pros.append(k['prosText'])
                    cons.append(k['consText'])
                    try:
                        alternate.append(k['alternativeProducts'][0]['productName'])

                    except:
                        alternate.append('-1')
                    chosing.append(k['chosenReasons'])
                    try:
                        switchedFrom.append(k['switchedProducts'][0]['productName'])
                    except:
                        switchedFrom.append('-1')
                    reasonSwitch.append(k['switchingReasons'])
                    url.append('https://www.capterra.com/p/76390/Infusionsoft/reviews/'+str(k['reviewId']))


                    source.append("Capterra")


readJsonFiles()



with open("out.csv", "w", newline='',encoding='utf-8') as csvFile:
    for a,b,c,d,e,f,g,h,i,j,k,l,m,n,o in zip(product,name,reviewTitle,date,overallRating,Likelihood,overall,pros,cons,alternate,chosing,switchedFrom,reasonSwitch,url,source):
        fk=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O"]
        writer = csv.DictWriter(csvFile,fieldnames=fk)
        writer.writerow({"A":a,"B":b,"C":c,"D":d,"E":e,"F":f,"G":g,"H":h,"I":i,"J":j,"K":k,"L":l,"M":m,"N":n,"O":o})


