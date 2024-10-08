# sh0rt

## Description  
Give the following to competitors:
```
You know what y'all, it's late and I don't want to write flavortext. Imma give you a password hash. You need to crack it. It's pretty simple. 

Oh what, you want clues? You want somewhere to start? Fine. The person who made this password likes Dune short stories. And this is a hard challenge. Figure out the rest on your own. 

0c7cc8c48c685cdb47acd63421dfbaf430a6e6c1

Flag format: byuctf{password}
```

## Solve Theory

The password list can be built by running CEWL on the wikipedia page for Dune short stories. The password is two of these words with some leet replacements thrown in. It's expected that competitors will have to try a couple different rule sets, so the hashing format is SHA1 (which doesn't take forever). 

`byuctf{So0ston3s-W@li5}`