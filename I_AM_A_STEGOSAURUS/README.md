# I AM A STEGOSAURUS

This challenge is intended to teach competitors about zsteg and lsb text encoding in images, two basic steganography techniques.

## Challengers

Provide the following to challengers:
```md
I AM A STEGOSAURUS
--------
I think that stegosaurus might have just stomped a flag... could it possibly still be in the image?

```
Also provide the file `steg.png` from this directory.

## Writeup

We used zsteg to hide the flag in the rgb lsb's of the picture. Running the image through a tool such as [aperisolve](https://www.aperisolve.com/), or even just manually using the [zsteg tool](https://github.com/zed-0xff/zsteg), will reveal the flag.

`byuctf{gotta_catch_'em_all}`