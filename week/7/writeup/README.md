Writeup 7 - Forensics I
======

Name: *Ivan Quiles*
Section: *0201*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Ivan Quiles*

## Assignment 7 writeup

### Part 1 (40 pts)

1. This is a JPEG image file

2. This image was taken in Chicago at the John Hancock building.

3. The timestamp is `2018:08:22 11:33:24.801` 

4. The camera was an IPhone 8

5. This photo was taken 539.5 meters above Sea Level

6. A flag that I found CMSC389R-{look_I_f0und_a_str1ng}

### Part 2 (55 pts)
*Flag*: CMSC389R-{dropping_files_is_fun}

After installing radare2 and cutter I used cutter to help me look at the assembly in the binary. At first I didn't really know what I was doing
so I just messed around with all the different options but after a while I realized that the comments on the side said `/tmp/stego` and that
the binary was performing a write operation. So after that I ran the binary and lo and behold there was a file named stego in my `/tmp` folder.
From there I moved it to my home directory and started poking at it. 

First I hoped that the use of `strings` would make me lucky and I would just get a flag but that turned out not to be the case so then I used 
exiftool and it told me that it had some jpeg tags but that it wasn't complete. I wasn't really to sure what to do next so I went back to the slides
and after some reading found `binwalk` and I ran `binwalk --dd=".*" stego` (for some reason -e wasn't working) and I got an output folder with a 
single image of a stegosaurus in it. I figured that this was an obvious pun for steghide so I ran `steghide extract -sf 1 -xf out.txt` with the 
password `stegosarus` and I got the flag that I put above!. 
![Image of me figuring out binwalk correctly](https://github.com/ivan98q/389Rfall18/blob/master/week/7/writeup/last_part_of_the_assignment.png)
