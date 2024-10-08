# Portal Gun

This challenge is intended to teach participants about http web redirects.

## Setup

This folder is prepped with a docker container for the website that will run it on port 12346. You can change this as needed to adapt to existing infra. Just run `docker compose up` from this folder. 

## Challengers

Provide the following to challengers:
```md
Portal Gun
--------
I think this website has a flag, but I can't seem to get to it. Can you figure out what's going on?
http://link.to.site:12346
```

## Writeup

The page that we give a link to will automatically redirect users to the cyber kickstart github. However, the flag is inside of a commented out h2 tag on the initial page. Competitors will need to look at the page source of the inital page, or use a tool like curl, wireshark, or burpsuite in order to get the initial HTTP response and see the commented out code. The flag is:

`byuctf{yo,_coming_up_with_creative_flag_names_is_hard!}`