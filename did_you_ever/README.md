# Did you ever hear the tragedy of Darth Plagueis the Wise

## Description
Give the following to competitors:
```
I thought not, it's not a story the Jedi would have told you. It's a sith legend. 

Y'all, I just watched that scene on Youtube and it's such a meme. There are at least four high quality quotes in those two minutes alone. 

Also apparently password cracking is just where I break the fourth wall ;)

Anyways, our forensics experts grabbed the /etc/shadow file from Darth Palgueis' computer. They suspect that instead of a proper password he used a six digit pin. Can you crack it?

Flag format: byuctf{pin}
```
Also provide them with `shadow` found in this directory. 

## Solve Theory

The password is hashed using yescrypt, a modern format that is currently not supported on hashcat. John kinda supports it, but you have to use the --format=crypt flag to say it's a UNIX password. The following command (while not strictly the most efficient) will give you the flag: `john -i=digits ./shadow --format=crypt`.

`byuctf{498500}`