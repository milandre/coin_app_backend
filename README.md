# Coin App

This is an example Django app

**This example is written with Django 2.1.4.**

## Building

It is best to use the python `virtualenv` tool to build locally. Make
sure you have it installed and then run:

```sh
$ make development
$ make serve
```

Then visit `http://localhost:8000` to view the app. 

## Testing

For test executions, run:

```sh
$ make test
```

## Application Code

This project has three apps: users, currency and account.

In the users app, you will find all the business logic
for clients.

In the currency app, you will find all the business logic
for currency and its API.

In the account app, you will find all the business logic 
for account, transactions and its API.

You could find all project templates in `templates` folder of each app.


## Updates

21/12/2018 - Missing Currency creation from client session. Creation only
             in Django Admin 