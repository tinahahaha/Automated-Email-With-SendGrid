# coding=utf-8
# python version: 2.7
# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import sendgrid
import os
from sendgrid.helpers.mail import *
import urllib2
import csv
import codecs
import base64
import time

# set api key
sg = sendgrid.SendGridAPIClient(apikey='##############') 
#os.environ.get('SENDGRID_API_KEY')


# email basic setting
from_email = Email("thesisaward2018@mis.nsysu.edu.tw")


# open the content text file
with open('mailcontent_30countdown.txt', 'rb') as f:
    text = f.read()
    f.close()


# add attachments 1
file_path = "attachments/attachment1.pdf"
with open(file_path,"rb") as f1:
    attach1 = f1.read()
    f1.close()
encoded1 = base64.b64encode(attach1).decode()
attachment1 = Attachment()
attachment1.content = encoded1
attachment1.type = "application/pdf"
attachment1.filename = "2018年台灣服務科學學會學術研究獎辦理辦法.pdf"
attachment1.disposition = "attachment"
attachment1.content_id = "attachmentPDF"


# add attachments 2
file_path = "attachments/poster1.jpg"
with open(file_path, "rb") as f2:
    attach2 = f2.read()
    f2.close()
encoded2 = base64.b64encode(attach2).decode()
attachment2 = Attachment()
attachment2.content = encoded2
attachment2.type = "image/jpeg"
attachment2.filename = "2018-服務科學論文獎海報-EMBA.jpg"
attachment2.disposition = "attachment"
attachment2.content_id = "poster1"


# add attachments 3
file_path = "attachments/poster2.jpg"
with open(file_path, "rb") as f3:
    attach3 = f3.read()
    f3.close()
encoded3 = base64.b64encode(attach3).decode()
attachment3 = Attachment()
attachment3.content = encoded3
attachment3.type = "image/jpeg"
attachment3.filename = "2018-服務科學論文獎海報-博碩士.jpg"
attachment3.disposition = "attachment"
attachment3.content_id = "poster2"


# add attachments 4
file_path = "attachments/attachment2.docx"
with open(file_path, "rb") as f4:
    attach4 = f4.read()
    f4.close()
encoded4 = base64.b64encode(attach4).decode()
attachment4 = Attachment()
attachment4.content = encoded4
attachment4.type = "application/pdf"
attachment4.filename = "2018年台灣服務科學學會學術研究獎申請表.docx"
attachment4.disposition = "attachment"
attachment4.content_id = "attachmentDOC"


# open the receivers csv file
csvfile = open('mails/allmails.csv', 'rb') 
# csvfile = open('mails/mails_test.csv', 'rb') 
count = 0
start = 1

# start to mail
for row in csv.reader(csvfile, delimiter=",", quotechar=" "): # 2
	count = count+1
	if count<start:
		continue

	print 'name:\n'+str(row[0])
	to_email = Email(row[1])

	text1 = str(row[0] + text).decode('big5')
	content = Content("text/plain", text1)
	subject = "【2018台灣服務科學學會學術研究獎】報名即將於107/7/31截止，敬邀"+ str(row[0]) +"老師推薦學生報名參加！"

	mail = Mail(from_email, subject, to_email, content)
	mail.add_attachment(attachment1)
	mail.add_attachment(attachment2)
	mail.add_attachment(attachment3)
	mail.add_attachment(attachment4)
	
	try:
		response = sg.client.mail.send.post(request_body=mail.get())	
	except urllib2.HTTPError as e:
		print e.read()
		print count

	print('response.status_code:',response.status_code)
	print('response.body',response.body)
	print('response.headers',response.headers)

	

