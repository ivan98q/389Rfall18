Writeup 5 - Binaries I
======

Name: *IVAN QUILES*
Section: *0201*

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *IVAN QUILES*

## Assignment 5 Writeup
Starting this assignment I decided to use the 'loop' instruction given to us in the slides and try to copy into the string directly using `mov` and decided not
to bother with `stos`. 

So I started my doing `mov rcx rdx` since the `loop` instruction uses `rcx` to decrement and compare. I also used `r8` for my `i` in the loop Then I did this 
`mov qword [rdi + r8] rsi` which I later learned would lead to _A LOT_ of issues but I did not know this at the time. Then I incremented `r8` and ran loop
and it worked! Or at least I though it did it was outputting `Hello zzzzz` instead of `Hello zzzzz!` but I didn't notice at the time. 

Then I started my_strncpy and did the same loop as above. my big code change was getting the char out of the source string
so

``` assembly
mov rdx, qword [rsi + r8]
mov qword [rdi + r8], rdx
```

was what I ended up doing and I put it in the same loop I had from memset. However, here is where I ran into the wall that I unwittingly created for myself earlier
when I ran `./main` I got `Hello ` and that was it instead of `Hello Hello!`. I spent a few hours troubleshooting this but I didn't realize what was wrong so 
I posted on Piazza and Josh (Thanks so much for the help!) pointed out to me that I was using the wrong sized registers so I changed my code to be 
``` assembly
mov dl, byte [rsi + r8]
mov byte [rdi + r8], dl 
```
but it still wasn't working correctly and that was because for some reason I didn't realized I did the same incorrect thing in the other function. So 
I spun around in circles for another our and asked Josh (Seriously thanks!) a few more questions before realizing that the output of my first function was missing
an '!' so I went back and checked it and realized that I was using the wrong sized registers and was clobbering the test string. So I went back and changed
the copying code in memset to `mov byte [rdi + r8] sil` and suddenly everything worked correctly. 

I think the main trouble I had with this assignment was misunderstanding how register sizes and copying worked which led to a lot of issues down the line but 
I learned what I was doing wrong and how to fix it so it was worth it in the end.
