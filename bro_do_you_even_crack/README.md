# Bro do you even crack?

## Quick Note

I lost the pcap file after the competition ended, and haven't re-generated it. You get the idea behind the challenge from the writeup though. 

## Challenge

Rating: intermidiate

Provide the following to challengers:
```
You've landed in Cario, and have made your way to a local coffee shop to meet up with your last contact before raiding the tomb. While connecting your phone to the wifi, you see a network that's owned by one of your rivals available in the area. You quickly start a packet sniff, and you're in luck! You managed to capture a WPA handshake in the password. Now you just need to crack it. 

What is the password for the Gandalf network?

Hint: it's a city in Utah, all in lowercase.
Flag format: byuctf{city}
```

## Solve Theory

Running aircrack-ng on the pcap using a wordlist of lowercase utah city names will reveal the flag. 

byuctf{paradise}