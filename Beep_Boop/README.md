# Beep Boop

This challenge is intended to teach participants about the #1 web enumeration tactic, checking `robots.txt`.

## Setup

This folder is prepped with a docker container for the website that will run it on port 12345. You can change this as needed to adapt to existing infra. Just run `docker compose up` from this folder. 

## Challengers

Provide the following to challengers:
```md
Beep Boop
--------
I've found this odd site that seems to be all about robots, can you find the flag hidden here?
http://link.to.site:12345
```

## Writeup

The flag is located in the home directory of the site in a file called robots.txt. This is a common file for a website to have; it tells web crawlers what parts of the site the creators don't want indexed (which is convenient for us hackers, as we can learn what parts of a site the creators don't want us finding). going to `http://link.to.site:12345/robots.txt` will reveal the flag:

byuctf{r2d2_is_the_best_movie_robot_prove_me_wrong}