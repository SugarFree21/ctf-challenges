# Cosmere

## Description
Give the following to competitors:
```
Welcome to the cosmere, an intergalactic network of planets and realms filled with creatures of the mist, glowing knights, talking swords, and teenage girls that are insanely good at stacking rocks. 

The Dustbringers are a powerful but historically chaotic order of the knights radiant, and your job as an intergalactic worldhopper is to infiltrate their ranks and figure out what they're up to. Fortunately you have access to an online quiz that can tell anyone how closely they are aligned to any given order, you can use that to learn more about the Dustbringers!

On a scale of Free-spirited to Disciplined, what percent disciplined is the ideal Dustbringer? 

Flag format: byuctf{percentage} (example: byuctf{45})

https://www.brandonsanderson.com/official-knights-radiant-order-quiz/

* Please note, THIS IS NOT OUR WEBSITE. You cannot use automated tools of any kind. You don't have to script this one. Figure it out. 
```

## Solve Theory
The online quiz is written in JavaScript, which means that the whole thing happens client side. After doing some investigation into the code, you can discover that user inputs are compared to a three-dimensional array called `traitData`, which has the ideal slider positions for each order in each question. Further investigation will reveal that question 4 is missing from the HTML list of questions, but not the array. After playing around with this, you can discover that the disciplined vs free spirit question is question 15, and that the dustbringer traits are index 2 in the array. This means that ideal dustbringer is 87% disciplined. 

`byuctf{87}`