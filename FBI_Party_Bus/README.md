# FBI Party Bus

This challenge is intended to introduce competitors to packet capturing, and teach them sort through network traffic.
## Challengers

Provide the following to challengers:
```md
FBI Part Bus
--------
Our agents have intercepted some traffic from a suspect's LAN. It looks like at one point in time they signed into their router's web portal. Can you find the username and password they used to sign in?

Flag format is `byuctf{username_password}`

```
Also provide the file `chall.pcapng` located in this directory.

## Writeup

Competitors can filter the packets captures so that they are just viewing HTTP requests. From here it becomes easy to identify the router IP address, and to check the /login HTTP POST request. This request has the username and password base64 encoded together, and decoding it will give you everything you need for the flag. 

`byuctf{admin_H3110Th3re}`