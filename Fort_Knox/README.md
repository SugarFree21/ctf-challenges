# Portal Gun

This challenge will help participants begin to look at their browser developer tools. It will involve viewing the page source, linked JS files, and browser local storage. 

## Setup

This folder is prepped with a docker container for the website that will run it on port 12346. You can change this as needed to adapt to existing infra. Just run `docker compose up` from this folder. 

## Challengers

Provide the following to challengers:
```md
Fort Knox
--------
I think this website has a flag, but I can't seem to get to it. Can you figure out what's going on?
http://link.to.site:12347
```

## Writeup

Competitors are given a link to the login page for the site. Once they check the page source, they'll see that there is a linked javascript file. This file will give them the username and password in static text. Once they sign in the admin page will tell them that the flag is the password they used to sign in. 

`byuctf{hahatrytoguessthispasswordhydra___;;1492}`