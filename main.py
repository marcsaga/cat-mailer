import yagmail  
import requests
import os


FILE_NAME = 'cat.gif'
QUOTE_API_URL = 'https://api.api-ninjas.com/v1/quotes?category=leadership'
CAT_API_URL = 'https://cataas.com/cat/gif'

contents = ['<h3>Buenísimos días celi</h3>']

def sendEmail(sender_email, sender_password, receiver_email, quote_api_key):
    
    r = requests.get(CAT_API_URL)
    if r.ok:
        with open (FILE_NAME, 'wb') as outfile:
            outfile.write(r.content)
            contents.append(FILE_NAME)

    response = requests.get(QUOTE_API_URL, headers={'X-Api-Key': quote_api_key})
    if response.status_code == requests.codes.ok:
        quoteInfo = response.json()[0]
        contents.append("<br/><h4>Quote of the day is:</h4>")
        contents.append("<p><i>{}</i></p><span>{}</span>".format(quoteInfo['quote'], quoteInfo['author']))
    else:
        print(r)

    yag = yagmail.SMTP(sender_email, sender_password)
    yag.send(to = receiver_email, subject="Urgent email, read as soon as possible", contents=contents)


def main():
    sendEmail(os.environ.get("SENDER_EMAIL"), os.environ.get("SENDER_PASSWORD"), os.environ.get("RECEIVER_EMAIL"), os.environ.get("QUOTE_API_KEY"))

main()