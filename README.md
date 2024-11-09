# CS Button Announcer (I guess?)

Naming is hard. Let's go with that.

This software monitors a web page for a local makerspace I'm part of and then sends out an email when it changes to saying it's open. That's about it.
The python program is at least 70% chatgpt. The animal-say is something I developed for a pentium-90 hobbyist project a few years ago because cowsay was slow on it ( I mean like, multiple seconds ). So I use the magic of /usr/games/fortune twice! Once for the out of date, hopefully not insensitive quote, and once again for the whimsical ascii art character who is saying it.

### caveats and more!

This code baked-in full paths to make cron happy so fix those if you want to use it, or just name your unix user chris, drop it in the directory cs-check, and consider the code as-is to be flawless and omnipotent --- do as thou whilst.

The cron line I use is
```
* * * * * /home/chris/cs-check/crash-space-check.py
```

I use [msmtp](https://marlam.de/msmtp/) for the mail program. 

The cutesy quotes in the body of the message are done with the magic of the old unix [fortune](https://en.wikipedia.org/wiki/Fortune_(Unix)) program. The one I used was the apt-available debian one.
