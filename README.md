# Automated-Email-With-SendGrid


[Sending Email with SendGrid](https://cloud.google.com/appengine/docs/standard/python/mail/sendgrid)

## APIkey
因為免費版有一定的日期限額，如果被ban或日期過了就再申請新帳號新API

## GitHub example
[GitHub](https://github.com/sendgrid/sendgrid-python#example)


## 用到的File
* 主程式
    * sendMails.py
* 存放信件內容 (以UTF-8編碼)
    * mailcontent.txt
    * mailcontent_30countdown.txt
* 收件人列表 (以UTF-8編碼)
    * mails\mails1.csv
    * mails\mails2.csv
    * mails\mails3.csv
    * mails\mails4.csv
    * mails\mails5.csv
    * mails\mails6.csv
* 附件
    * attachments\attachment1.pdf
    * attachments\attachment2.docx
    * attachments\poster1.jpg
    * attachments\poster2.jpg

## develop environment
* python 2.7.14
* sublime


## 範例程式碼

```python=

# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import sendgrid
import os
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
from_email = Email("test@example.com")
to_email = Email("test@example.com")
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)
```

## Data Preprocess

1. 移除重複的mail
2. 若有兩個mail則取一
3. 姓名中有"恒"字者，取代為英文名字
4. 英文名字中不能有逗號

## Future Work

1. 解決python讀信件內容txt檔時，無法正確讀出每個空白行和縮排
2. 減少變成垃圾信件的可能....How?




---
::: success
以下不是重點
:::


Spam Check
===
[spam-check website](https://spam-check.glockapps.com/test/st-3-4cd8invdgs?_ga=2.260235213.1779452734.1528211781-1817789078.1528211781)

![](https://i.imgur.com/DzeTT8I.png)






multiple python version 
===

## python 3 
` py -3 (fileName)`

## python 2
` py -2 (fileName)`

pip install : ` py -2 -m pip install (packageName)`


```
C:\Users\tina8>py --version
Python 3.6.1 :: Anaconda 4.4.0 (64-bit)

C:\Users\tina8>python --version
Python 2.7.14
```


` ## -*- coding: utf-8 -*- `

` # encoding: utf-8 `

## virtual environment
cmd: python 2.7
```
virtualenv --python=c:\Python27\python.exe (envname)
```

D:\Lab\2018台灣福科學會博碩士論文獎\sendGrid\Scripts\python.exe


/my/python-venvs/env-py36/bin/virtualenv --python=/path/to/python27/bin/python /my/python-venvs/env-py27




App Engine Mail API
===

## call gmail api
1. [Getting Started with Flask on App Engine Standard Environment](https://cloud.google.com/appengine/docs/standard/python/getting-started/python-standard-env)

* app.yaml file:
The app.yaml file is a configuration file that tells App Engine how to run your application and how to map URLs to static files and Python modules.

## GCP (Google Cloud Platform)

* [User Guide ](https://sendgrid.com/docs/User_Guide/index.html)
Find out more about how to use every feature of SendGrid

* [API Reference Index](https://sendgrid.com/docs/API_Reference/index.html)
Learn how to use SendGrid's different APIs

* [Integrate With SendGrid](https://sendgrid.com/docs/Integrate/index.html)
Send email from your app whether it's a CMS, framework, CRM, or your own code
