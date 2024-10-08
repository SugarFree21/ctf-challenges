# All the King's Horses

## Description  
Give the following to competitors:
```
In a daring raid, rebel forces have broken into an Imperial data center and escaped with an image of the location of their new prison! 

The image is odd, it doesn't look like a planet you've ever seen before. Maybe if you get some more specifics you can figure out where it is. 

What is the name of the city this picture was taken in?

Flag format: byuctf{city_name}
```
Also give competitors `trees.jpg` found in this directory. 

## Solve Theory  

The GPS coordinates for the photo are stored in the exif data. Pulling that will reveal the image location. 

`byuctf{humpty_doo}`