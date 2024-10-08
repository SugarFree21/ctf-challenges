# Logs, glorious logs

This challenge is intended to help become familiar with looking at logs, in this case specifically apache logs on Linux. 

## Challengers

Provide the following to challengers:
```md
Logs, glorious logs
--------
If you don't like looking at logs, get used to it. Welcome to the industry. One of the POST requests sent to this web server has a password, what is that password?

byuctf{password_here}
```
Also provide `access.log` as found in this directory

## Writeup
This is the access log of an apache web server. It's not super long, so this should be a pretty easy challenge. Searching the logs for POST requests using grep will reveal the request pretty quick. 

`byuctf{hellothere}`