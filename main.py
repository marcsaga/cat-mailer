"""Script that sends an email with a cat gif and a quote of the day"""
import os
import yagmail
import requests


CAT_GIF_FILE = 'cat.gif'
QUOTE_API_URL = 'https://api.api-ninjas.com/v1/quotes?category=leadership'
CAT_API_URL = 'https://cataas.com/cat/gif'


def get_cat_gif():
    """Retrieve a cat gif and save it to a local file."""
    cat_response = requests.get(CAT_API_URL, timeout=10)
    cat_response.raise_for_status()

    with open(CAT_GIF_FILE, 'wb') as outfile:
        outfile.write(cat_response.content)


def get_quote_of_the_day(quote_api_key):
    """Retrieve the quote of the day."""
    headers = {'X-Api-Key': quote_api_key}
    quote_response = requests.get(QUOTE_API_URL, headers=headers, timeout=10)
    quote_response.raise_for_status()

    quote_info = quote_response.json()[0]
    return quote_info['quote'], quote_info['author']


def send_email(sender_email, sender_password, receiver_email, subject, author, quote):
    """Send an email with the cat gif and the quote of the day."""

    contents = [
        f'<h3>{subject}</h3>',
        "<br/><h4>Quote of the day is:</h4>",
        f'<p><i>"{quote}"</i> <span>- {author}</span></p>'
    ]

    yag = yagmail.SMTP(sender_email, sender_password)

    yag.send(
        to=receiver_email,
        subject=subject,
        contents=contents,
    )


def main():
    """Main function"""
    sender_email = os.environ.get("SENDER_EMAIL")
    sender_password = os.environ.get("SENDER_PASSWORD")
    receiver_email = os.environ.get("RECEIVER_EMAIL")
    quote_api_key = os.environ.get("QUOTE_API_KEY")
    email_subject = os.environ.get("EMAIL_SUBJECT")

    try:
        quote, author = get_quote_of_the_day(quote_api_key)
        send_email(sender_email=sender_email, sender_password=sender_password,
                   receiver_email=receiver_email, author=author, quote=quote, subject=email_subject)
    except requests.RequestException as error:
        print(f"Error occurred: {error}")
    finally:
        # Clean up the downloaded gif
        if os.path.exists(CAT_GIF_FILE):
            os.remove(CAT_GIF_FILE)


main()
