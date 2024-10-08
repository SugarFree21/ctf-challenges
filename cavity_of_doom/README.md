# Cavity Of Doom

Cavity of Doom is a two part pentesting / password cracking challenge that takes place in a fictitious dentist's office. The first step of the challenge is to get administrative access to the machine. The first flag is found on the desktop of the computer. The second is to locate a hashed password used to connect to a sql database inside of the config files of an application. The second flag is the cracked password. The third part of the challenge involves connecting to the sql database and stealing a hashed password to crack. The third flag is the final cracked password.

## Challenge

### Part I

Rating: intermediate

Present the following to challengers:
```
You've been hired as a pentester for a large Indiana Jones themed dental office known as 'The Cavity of Doom'. You've managed to break in after-hours and made your way to the dentist's personal desk. You don't know the password, but you're a hacker! With physical access, nothing is safe from you. The flag can be found in clear text on the desktop of the computer.

(This VM is the closest we can give you to physical access)

Flag format: byuctf{flaghere}
```

Also give them the OVA found in this box directory: https://byu.box.com/s/u53adiyaeefaduf8pqhd9mr164pnh8ql

### Part II

Rating: hard

Present the following to challengers:
```
Now that you've got administrator access, it's time to prove that you can get to the user data stored on the on prep server. The doctor's username to the Open Dental program that accesses this data is 'Indiana Jones'. Some of the employees have put their passwords on sticky notes on their computers, and while you don't see Indy's anywhere, every other password just seems to be a four digit number...

NOTE: Some password cracking may be involved, but you MAY NOT use automated tools against the sql server

NOTE 2: the application will need to be on the BYU network to function

Flag format: byuctf{indiana's_password}
```

## Solve Theory

#### Creds for everything
Server creds  
`Cosmo:hahaguessthispassword`

Win7 creds  
`Cosmo:hahaguessthispassword`

mysql root creds  
`root:hahaguessthispassword`

mysql limited creds  
`Sallah:#1hottestperson`

Admin Open Dental creds  
`Admin:tombadmin`

Indiana Jones Open Dental creds  
`Indiana Jones:7533`

### Part I

If you have physical access to a windows machine, there are any number of methods you can use to get access. One such method would be running a sticky keys attack to get an administrative command line from the login screen, and using that to change the user's password. Once you can sign in the flag is in fact on the desktop. 

Flag: byuctf{areyouarealhackerordidyoujustgrepthis?}

### Part II

Once you're signed into the practice management application (Open Dental) you can make sql queries to the server using the User Query tool. Some research will reveal that the user passwords are stored in the `userod` table. A statement such as the following will retrieve the password hash for the Indiana Jones user:
`SELECT * from userod`. 

The password will be in a format like this:
`SHA3_512$hZ1d1zPTsd3O7k6Jcxw6aoCTDNO9M3/mOWT2WIyTvP+uQchKSI/46U6cKqaDJPt25SKHXld0EDU8TI1WB3y1rA==$I/MjOkcXHUnAAWKbg05snJYXB+38QBXkKIi2umdCEhhKeN+MTEsY5Bnd0B6o4Cf0pk6piEFpd0gL2hrcsNlsVg==`

In PHP, this is essentially how that string has been created:
```
$hash = base64_encode(hash('sha3-512', mb_convert_encoding($salt . $this->getRequest()->getPost('password'), "UTF-16LE"), true));
$hash = $hashType . '$' . $salt . '$' . $hash;
```
Flag: byuctf{7355}