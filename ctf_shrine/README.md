# CTF Shrine

## Challenge

Rating: easy

Provide the following to competitors:

```
All of my 344 and 247 homework was weighing me down the other day, so I looked around for a while and found a shrine to take a break at! There was even a flag there! I can't remember what it was though, can you go back and find it for me?

Flag format: byuctf{youknowwhatgoesinhere}
```

## Solve theory

All locations in Google Maps need to say what kind of place they are, such as a school or a fast food restaurant. This tag doesn't need to be even remotely related to what the place is, it's completely self reported by the person creating the entry in Google Maps. 

Searching for shrines in Utah will inevitably lead to challengers discovering "The Bradley House", a student house in Provo that is not a shrine in any way, but has the shrine tag in Google Maps. After looking through reviews, challengers will notice a base64 encoded string. Deciphering this will reveal the flag: 
`byuctf{whoknewtherearentmanyshrinesinutah}`