# While Aboard the Death Star

## Description  
Give the following to competitors: 
```
C3PO: Oh my! This waiting around while master Luke goes to rescue the Princess has me on edge! I do hope he calls in soon. 

R2D2: Beep boop beep beep!

C3PO: What's this you found? The Imperial intranet site? Good job R2!

R2D2: Bweep bwoop! Whistle-beep-beep... Bwoop!

C3P0: Now there's an idea! Can you get to Lord Vader's password? We might be able to use that to help Master Luke!

Flag format: byuctf{flaghere}
```

Also provide challengers with the url to the website, and `while_aboard.zip` located in this directory. 

## Solve Theory

The website will display the password for the user after they sign in. A sql injection payload in the username field such as `darthvader';--` will allow them to sign in unauthenticated. 

`byuctf{who_makes_their_password_a_flag?}`

## Hosting

The challenge is in a docker container that runs a flask server on port `1341`. All of the files necessary are included here. The command to build the docker container (while located inside this directory) is:
```bash
docker build -t while_aboard .
```

The command to start the challenge is: 
```bash
docker run -p 1341:1234 --detach --name while_aboard while_aboard:latest
```

The command to stop the challenge is:
```bash
docker stop while_aboard