# Cat mailer

Fun, simple project that sends an email once a day with a cat gif and a quote.

## APIs used
- [Catass API](https://cataas.com/) to obtain the cat gif.
- [Ninjas API](https://api-ninjas.com/) to obtain the quote and the author. An API key is needed to run the script, easy to obtain after sign-in.

## Others
- Github actions for configuring the cron job.
- Env variables configured in Github for customizing the script sender, receiver, and subject. See in `.github/workflows/daily_python_script.yml`
