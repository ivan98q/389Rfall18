Writeup 9 - Crypto I
=====

Name: *IVAN QUILES*
Section: *0201*

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgment of honor pledge: *IVAN QUILES*

## Assignment 9 Writeup

### Part 1 (60 Pts)
The challenge for this part was to break 4 hashes in the `hashes` file. We were given a few assumptions to work with.
First, that the passwords would all come from a single password dump and secondly that they were all salted with a 
lowercase letter (a..z). My first solution was just going through each hash and for each password and possible salt 
just do comparisons. I had some problems because I had trailing newlines when I was dealing with text and so I wasn't
getting the correct hashes. In the end while I was trying to fix this I moved my hash generation process (for each password and hash)
to a separate loop because it would be more efficient since I wouldn't be calculating each hash 4 times. I also started using 
`.readlines()` (Thanks Michael) and `.strip()` to get rid of the newlines and after all that it began to work!

![This is the solution to part 1](https://github.com/ivan98q/389Rfall18/tree/master/week/9/writeup/part1_solution.png)

### Part 2 (40 Pts)
The Challenge for this part of the project was to connect to a service and then hash the data with the correct hashing algorithm
that the data tells you. First I just ran the service my self to see the different inputs and outputs I would get. Then I started
by just getting one pass of the script to work correctly before I put it in a while loop to solve all the possible challenges.
I decided to use a regular expression to get the type of algorithm and the hash that I need. I had a lot of problems with that
because I didn't know too much about python regular expressions but it started working when I did it with the `finditer` method.
After I got the hash algorithm and the string to hash I hashed it, sent it back (with a \n on the end) and it worked! From there
I just put the code in a while loop that checks if the data does not contain "CMSC389R" (to determine if I got the flag back).
And then after I ran it I got back this flag:

Flag: CMSC389R-{H4sh-5l!ngInG-h@sH3r}

![This is the solution to part 2](https://github.com/ivan98q/389Rfall18/tree/master/week/9/writeup/part2_solution.png)

