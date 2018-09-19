Writeup 3 - OSINT II, OpSec and RE
======

Name: *Ivan Quiles*
Section: *0201*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgment of honor pledge: *Ivan Quiles*

## Assignment 3 Writeup

### Part 1 (100 pts)
To Mr.Krueger and Cornerstone Airlines,

As you know recently a group of students from a class known as "Introduction to Ethical Hacking" taught at the University
of Maryland broke into your web server. After reading about our report that described how we broke into your server you reached out
to us looking for ways to improve your companies security. Here is our report.

Our first suggestion is to _change your passwords RIGHT NOW_. 
For instance, the former password to your server _pokemon_ could easily be gleaned by looking at one of your retweets and your
love for Pokemon Go. It was also easily breakable with a password list named 'rockyou.txt' in a time period of about 10 minutes.
The solution to this is to use a Password Manager for **EVERYTHING** from now on. Password Managers are programs that create randomized
long passwords for you increasing the difficulty of the password by one making it longer and two making it much harder to break by 
running a simple password word list. You have one master password that gets into the password manager that usually has a larger min size than
8 characters. You can also use Hardware authentication devices like the [Yubikey](https://www.yubico.com/) this makes it so now a hacker has to 
gain access to your system and your person to get your password. For a password manager I recommend [Keepass](https://keepass.info/) it's
an open source password manager that works on Windows and has compatible programs on just about every device imaginable. I have it on both 
my laptop which runs Linux and my phone which runs Android. I'd also suggest for your individual employees to have their Work and Personal
Life password managers completely separate just in case their home is broken into or if their is some other incident so that the business
isn't threatened. Another huge security gain is setting up Two Factor Authentication so that every time you attempt to log in to your server you have to have a 
secondary device to provide another layer of authentication past your password. I will also leave you with this [XKCD](https://www.xkcd.com/936/)

Our second suggestion is to hide the Admin part of your site **RIGHT NOW** and set up a firewall to block suspicious traffic 
(like repeatedly attempting to log in). The security vulnerability at the center of the hack was the exposed Admin Server on your site. 
The fact that not only could any user access it but 
it was just publicly lying around on the internet is just about as harmful as it could get. First things first remove it from your website
and maybe even changing the IP address of the server to make sure it can't be accessed by just looking 
at [Wayback Machine](https://web.archive.org/web/*/cornerstoneairlines.co/*). Then using a firewall block some suspicious incoming traffic. 
For instance, if the server keeps requesting to log in and just continues failing over and over you should
stop that connection right now so that password cracking can't happen. You could also implement a system where if a user gets their password
wrong 3-5 times in a row there's a 10-15 minute wait before being able to log in again. You need to implement rules to stop as much malicious 
traffic as possible from potentially getting into your server and getting sensitive info. You can also use a VPN (_Virtual Private Network_) to
restrict which computers could access your admin system.

Our final suggestion is restrict all information that is publicly available about your web administrators or at least make some differences between
your personal and work accounts/information. The ease to which the class used OSINT (Open Source Intelligence) techniques to discover Mr.Krueger's 
username and password were very worrying. To Mr.Krueger, make sure that usernames you use at home and in the workplace are different and that your work
username that you use to access the server is separate to your publicly available email. You want to make it as difficult as possible for an attacker to 
learn anything about you whatsoever. Make it hard for the attacker to use any personal information they have on you to break into your work system. 
In essence you have to make sure that every account/password/password manager/ public-private key pair/ email/ **Anything** that is used in your personal
life is not used at work. You are always a target and you always have to be ready for when someone tries to break into your system/phish you/ attempt to
use social engineering to gain access to your system.

In conclusion, here is a [report](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-44ver2.pdf) from NIST (National Institute for Standards and Technology ) about how to secure public web servers 

Sincerely,
The "Intro to Ethical Hacking" Class at UMD.



