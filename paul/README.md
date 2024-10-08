# paul

## Description
Give the following to competitors:
```
You may have heard of my friend Paul. He had two space movies made about him recently. He calls himself a preacher, but I think that's going a little too far. 

Anyways, I have his password. Err, well, his password hash. If you want a flag please crack it. 

d71dfe1b9680e6f6b08f2c45b41ea2b5117f4da792681f3b3276b21dfad07454

Flag format: byuctf{password}
```

## Solve Theory

If you feed information about Paul Atreides into CUPP then it'll give you a list that contains the password. The hashing format is SHA256. 

`byuctf{A7r31d35&$&}`