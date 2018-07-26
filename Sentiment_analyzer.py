import os
import re
def generateSentiment():
    affinFile = open('D:\AFINN-111.txt','r')
    sentimentDict = {}
    outputDict = {}
    affinFile_read = affinFile.read()
    for each in affinFile_read.splitlines():
        each_split = re.split(r'[\-\s]',each)
        sentimentDict[each_split[0].strip()] = each[-1]
    path = "D:\yelp100Reviews"
    for each_file in os.listdir(path):
        fileHandle = open(path+"\\"+each_file,'r')
        eachFileRead = fileHandle.read()
        eachFileSentimentScore = 0
        for each_review_word in eachFileRead.split():
            if each_review_word in sentimentDict:
                eachFileSentimentScore = eachFileSentimentScore + int(sentimentDict[each_review_word])
        outputDict[each_file] = eachFileSentimentScore
        eachFileSentimentScore = 0
    print(outputDict)
generateSentiment()
#using text blob & nltk
from textblob import TextBlob
os.chdir("D:\yelp100Reviews")   
import glob as glob
file = glob.glob("*.txt")
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
for each in file:
   with open(each) as my_file:
       text = my_file.read().decode("UTF-8")
       sa = SentimentIntensityAnalyzer()
       pol = sa.polarity_scores(text)
       score = TextBlob(text)
       print("File name:", each, '\n',
             "NLTK :", pol, '\n',
             "Polarity:", score.sentiment.polarity, '\n',
             "Sentiment:", score.sentiment.subjectivity)
       
