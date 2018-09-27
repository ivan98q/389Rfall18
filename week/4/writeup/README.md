Writeup 3 - Pentesting I
======

Name: *Ivan Quiles*
Section: *0201*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Ivan Quiles*

## Assignment 4 Writeup

### Part 1 (45 pts)
Okay so first off here is the flag: CMSC389R-{p1ng_as_a_$erv1c3}
I used ```; cat /home/flag.txt``` to get this input. 

My thought process was pretty simple. Since we were given the server to connect to and we were told that they were using 
the ping command I started by 
trying to use it as intended by sending in an ip address. From there I remembered that 
Unix commands can be chained with a `;` and from there I just tried doing ```; ls``` and found that I was in
the root directory of the system. From there it was mostly smooth sailing by running ```; ls /home``` and I saw the flag
and ran the command above.


Finding the script took some work but I ended up running something like ```; ls * | find -atime -7 | grep .sh``` (Note: It's too far back in my shell's history
to get back to so this might not exactly be it.). This command returned all of the shell scripts edited in the last 7 days in order. There were a lot of them
but the one I needed was right at the top it was in the directory `/opt/container_shell.sh`. From here I didn't really know how to fix the vulnerability so 
I started googling and found out you can just do `\"$input\"'` which raps the input in quotes and gives ping the entire input instead of allowing an attacker
into the shell. This means that if an attacker runs ```; cat /home/flag.txt``` they would get an ordinary ping error instead of being able to execute arbitrary 
bash commands on the server.  After running it a few times on my computer to make sure it worked I saved it into the `fixed_shell_script.sh`  though I removed 
the cornerstone print out so it was a bit more readable to me. Besides changing that input I'm sure there is another way that someone could break this so Fred 
please don't allow people to put input right into the server without sanitizing it or else people will be able to get data off of the server relatively easily.
It may be better to allow for no free form input like that and only allow strings that have the format of an IP address.

### Part 2 (55 pts)
This aspect of the homework was much more difficult than the first part. 

The first thing I started with was just getting a basic "shell" opening and running. Just a simple while(True) and adding different if statements for the 
different possible commands.
From there I started the main part of the project which was getting the exploit that we found in part 1 to look like it was running as a shell. I started 
by adding the socket functionality and doing the basic work of connecting, sending and receiving. I did have an issue (that still occasionally creeps up) where the login page will
print instead of the command output but after I added `time.wait(1)` after connecting and sending data it went away. So now I could run one command but if 
I changed directory then no state was preserved so I wrote some basic `cd` logic that allowed a user to change directories and do `cd ..` to go up. This
involved just preserving the path that the user had moved into after the `cd` command was run. After a bit of string formatting I had something that mostly worked.

So now I had the shell I had to implement pull and at first I spent a lot of time googling for a fancy solution that involved the python socket library but 
after an hour or so of experiments I went back to the drawing board and decided to just do `; cat /path/tofile` to get the data through my socket. Then I
just received all the data and wrote it to a file with the name passed in. It's actually pretty awesome that we can do this with just a remote code exploit 
and some python/bash scripting. This project really shows off the power of remote code exploits, you can literally do anything if you have an exploit liked this.
