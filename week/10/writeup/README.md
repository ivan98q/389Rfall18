Writeup 10 - Crypto II
=====

Name: *Ivan Quiles*
Section: *0201*

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Ivan Quiles*

## Assignment 10 Writeup

### Part 1 (70 Pts)
To begin I had a lot of problems getting the solution of this correct. I made a lot of little errors, like forgetting to 
add the secret length to the length of the message and not doing `\\x` so I got a weird unicode symbol instead of the 
actual `\x` in front of my generated message. Here comes the information from my solution:

Hash that was used to make crafted hash: `e89d8fc9c2d6fd654c33a883372590ae`

Crafted Hash: `0cbfdd25abbc93f8105774d8e12f7259`

Payload: `CMSC389R Rocks!\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc8\x00\x00\x00\x00\x00\x00\x003v1l_hack3r`

Flag: `CMSC389R-{i_still_put_the_M_between_the_DV}`

For some reason I had a lot of trouble with getting the sockets to work correctly in this project. I would get to the loop for 
checking my crafted hash w/ payload but it would only run once through. This is shown in `stub.py` which has a mistake still
in computing the correct length. My final solution is in `attempt.py` which has the correct calculation of length as well.
In that solution I just printed out each generated message and tested it manually which is how I got the above solution.
Basically I just ran a for loop with the different lengths and added different padding/ length depending on the secret length
and outputted that to the console for me to test manually.

![This is the final console output](https://github.com/ivan98q/389Rfall18/tree/master/week/10/writeup/part1sol.png)

### Part 2 (30 Pts)
I had to do:

`gpg --gen-key` to generate my key since I accidentally lost my last one when my previous computer died.
`gpg --import pgpassignment.key` was to import your key!
`gpg -e -u "Ivan Quiles-Rodriguez" -r "UMD Cybersecurity Club" message.txt` encrypted the message with the key I just imported
`mv message.txt.gpg message.private` this was to make sure the encrypted message was actually called `message.private`.

I then ran through the same process but encrypted it with my own key and decrypted it to make sure I did it correctly. 
After that you should have an encrypted key that whoever owns the `pgpassignment.key`'s private can use to decrypt it.

