This has baked in directories to make cron happy so fix those if you download it.

The cron line I use is
```
* * * * * /home/chris/cs-check/crash-space-check.py
```

I use [msmtp](https://marlam.de/msmtp/) for the mail program. 

The cutesy quotes in the body of the message are done with the magic of the old unix [fortune](https://en.wikipedia.org/wiki/Fortune_(Unix)) program. The one I used was the apt-available debian one.
