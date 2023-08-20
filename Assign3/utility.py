# all util functions
import os
from tqdm import tqdm
import re
import string
# _________________________________________________________________
import nltk
nltk.download('stopwords',quiet=True)
from nltk.corpus import stopwords
#___________________________________________________________________
import numpy as np




def get_data_list(folder_name):#to get all test data
    email_collection = []  # store list of emails to be tested
    fl=os.listdir(folder_name+ os.sep)
    numberOfFiles=len(fl)  
    for file in fl:  # get that particular file path
        fileObject = open(folder_name+file, "r+", encoding='utf-8', errors='ignore')  # open the file
        email = fileObject.read()  # read the file
        email = email.lower()  # convert to lower case
        email_collection.append(email)  # append the email to a list
    return email_collection
#--------------------------------------------------------------------------------------------------------------

def cleanmail(emailarray):
#     Removes  urls, numbers,punctuation, and newlines. and converts to lower case.

    i = 0
    for email in emailarray:
        email = str(email)
        email = email.lower()#convert to lower acse
        #__________________________- replace /r /n
        email = re.sub(r'\\r', ' ', email)
        email = re.sub(r'\\n', ' ', email)
        email = re.sub(r'http\S+', 'httplink', email)#link placeholder
        email = re.sub(r'[^\s]+@[^\s]+', 'emailaddr', email)#emailplaceholdeer
        email = re.sub(r'[^\s]+\.(gif|png|jpg|jpeg)$', 'imgext', email)#imgplaceholder
        email = re.sub(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', 'ipaddr', email)#ip placeholder
        email = re.sub(r'[^\S]', ' ', email)
        email = re.sub(r' +', ' ', email)
      #The '$' sign gets replaced with 'dollar'
        email = re.sub('[$]+', 'dollar', email)
        email = email.translate(str.maketrans("", "", string.punctuation))
        email = re.sub("\d+", ' ', email)
        email = email.replace('\n', ' ')

        email = email.strip()
        emailarray[i] = email
        i += 1

    return emailarray
#_______________________________________________________________________________________________________________

stpword=stopwords.words('english')
stops=stpword+['emailaddr', 'enron', 'subject', 'received', 'dollar', 'width', 'ipaddr', 'td', 'id','tf', 
  'ansiansicpg','arialmt'
  'cocoartf',
  'cocoasubrtf',
  'fonttblf',
  'fswissfcharset',
  'helvetica',
  'colortbl',
  'ed',
  'green',
  'blue',
  'ed',
  'green',
  'blue',
  'paperw',
  'paperh',
  'margl',
  'margr',
  'vieww',
  'viewh',
  'viewkind',
  'deftab',
  'pardpardeftab',
  'slleading',
  'partightenfactor',
                 'httplink', 'ect', 'size', 'esmtp', 'height', 'company', 'sep', 'localhost', 'com']
def process(emailarr):
    
    email_tot=[]
    for email in emailarr:
        emailthis=[]
        words = email.split()
        for word in words:

            if word not in stops and len(word)>2:
                emailthis.append(word)
        email_tot.append(emailthis)
        
    return email_tot
