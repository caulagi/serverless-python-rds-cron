```
  _________________________________
< CRON jobs in a cloud native world >
  ---------------------------------
         \   ^__^
          \  (oo)\_______
             (__)\       )\/\
                 ||----w |
                 ||     ||

```

# serverless-python-rds-cron

A serverless python example that periodically removes entries from RDS.

For instance, you might want to delete users who have not verified their
email after 30 days.

```bash
$ python3.7 -m venv .venv
$ source ./venv/bin/activate
$ pip install -r requirements.txt # (or requirements-dev.txt)

$ export DATABASE_URL='mysql+pymysql://apa:apa@localhost/customer?charset=utf8mb4'
$ python cleanup.py

# Tests (if you installed dev requirements)
$ python -m pytest -v
```

## Deploying

This script is meant to be deployed as a [Lambda Cron](https://docs.aws.amazon.com/lambda/latest/dg/tutorial-scheduled-events-schedule-expressions.html)
using [serverless](https://serverless.com/)

Install [yarn](https://yarnpkg.com/lang/en/)

```bash
$ yarn global add serverless
$ cp .env.yml.example .env.yml

# We can deploy to different stages (environments)
$ serverless deploy -v

# See what we have
$ serverless info

# tail logs for the cronjob function
$ serverless logs -f cleanupCron -t

# invoke the function manually (if a pm pings you or because you can)
$ serverless invoke -f cleanupCron
```

## Fineprint/Don't forget

The tricky/hard part is to make your lambda talk to resources like RDS **and**
outside world. Follow the tutorial [here](https://aws.amazon.com/premiumsupport/knowledge-center/internet-access-lambda-function/)

## Bonus point

Put the database url in secrets manager and get it from there


## LICENSE

Licensed under [MIT](./LICENSE).
