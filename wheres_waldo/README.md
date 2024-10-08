# Where's Waldo?

## Challenge

Rating: hard

Provide the following to competitors:

```
My friend has been travelling recently, but he never tells me where he's going. He sent me this picture around lunch time yesterday. What is the street name that this business is on?

Flag format: byucft{streetname} 
(example, Jefferson St would become byuctf{jefferson})
```

Also provide `waldo.png`

## Solve Theory

The image pictures a Wawa in Allentown, PA. You can use the radio station playing to get a general idea of the location, and the other saved radio stations to triangulate it to the general Allentown area. After that it's just a matter of checking Google Maps until you find a Wawa with two sets of gas pumps, and using street view to confirm it.  
The address is 3321 Willow Ln, Macungie, PA 18062

The flag is `byuctf{willow}`