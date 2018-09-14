Writeup 2 - OSINT (Open Source Intelligence)
======

Name: *Ivan Quiles*
Section: *0201*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Ivan Quiles*

## Assignment 2 writeup

### Part 1 (45 pts)

1. The real name of this online persona is Fred Krueger. I found this via his twitter account. Nice touch witch his following/followers.

2. - Twitter account `kruegster1990`. Found using username website. Followed by UMD Cyber Security.
   - [His Reddit Account](https://www.reddit.com/user/kruegster1990). He only has one karma. 
   - [Email](kruegster1990@tutanota.com). This is his personal email links to an Email account.
   - [Work Email](kruegster@tutanota.com) This is his work email.
   - [WordPress](https://zaralarsson115206071.wordpress.com/2018/08/12/kruegster1990/). Wordpress with no posts.
3. His IP address is 142.93.118.186. I found this out by just pinging the website with `ping www.cornerstoneairlines.co`

4. By looking at the `robots.txt` I found that they disallowed a folder named `/secret' and when I viewed the source
 of that page I found this flag. CMSC389R-{fly_th3_sk1es_w1th_u5}

5. 142.93.117.193 links to the "admin" site. I found it by clicking the admin part of the site.

6. If you scan the ports for the IP address found above with netcat you can find a few different services that are on the server. There's an ssh port
   and there's an administrative service that seems to be the target. This is the server for the administrative part of the website so it's a bit different. The server is located in New York and it's owned by Digital Ocean.


7. Ubuntu. There's a few different ways. I just typed a random directory that wasn't real and it just told me.

8. *(BONUS)*

### Part 2 (55 pts)

His username was simple I just took the front of the email he had on his website

So first I just wanted to connect to the server. So I read up on netcat and ran this command
```bash
netcat -v -z 142.93.117.193 1-13000
```
This took a few minutes but after a while game me these results

- 142.93.117.193 80 (http) open
- 142.93.117.193 1337 (menandmice-dns) open
- 142.93.117.193 2222 (EtherNet-IP-1) open
- 142.93.117.193 10010 (rxapi) open

After a bit of messing around I realized the one I  wanted to target was Port 1337 which was the {menandmice-dns}.
One thing I noticed was that Fred liked pokemon GO so when I tried to log in I tried a few permutations of pokemon go
for some reason I didn't think to just type pokemon. So from there I wrote my script, figuring that it wasn't pokemon. Took me a second
to get the encoding and decoding of strings for socket to work but after that I just let it run for about 5-10 minutes and I ended up getting the
password `pokemon`. Then I logged in did 
```bash
cd home/flight_lists
```
and ran `cat AAC*` to get all of the flags out of the files.
List of All Flags using `cat AAC*`:
CMSC389R-{c0rn3rstone-air-27600}

CMSC389R-{c0rn3rstone-air-27601}

CMSC389R-{c0rn3rstone-air-27602}

CMSC389R-{c0rn3rstone-air-27603}

CMSC389R-{c0rn3rstone-air-27604}

CMSC389R-{c0rn3rstone-air-27605}

CMSC389R-{c0rn3rstone-air-27606}

CMSC389R-{c0rn3rstone-air-27607}

CMSC389R-{c0rn3rstone-air-27608}

CMSC389R-{c0rn3rstone-air-27609}

CMSC389R-{c0rn3rstone-air-27610}

CMSC389R-{c0rn3rstone-air-27611}

CMSC389R-{c0rn3rstone-air-27612}

CMSC389R-{c0rn3rstone-air-27613}

CMSC389R-{c0rn3rstone-air-27614}

CMSC389R-{c0rn3rstone-air-27615}

CMSC389R-{c0rn3rstone-air-27616}

CMSC389R-{c0rn3rstone-air-27617}

CMSC389R-{c0rn3rstone-air-27618}

CMSC389R-{c0rn3rstone-air-27619}

CMSC389R-{c0rn3rstone-air-27620}

CMSC389R-{c0rn3rstone-air-27621}

CMSC389R-{c0rn3rstone-air-27622}

CMSC389R-{c0rn3rstone-air-27623}

CMSC389R-{c0rn3rstone-air-27624}

CMSC389R-{c0rn3rstone-air-27625}

CMSC389R-{c0rn3rstone-air-27626}

CMSC389R-{c0rn3rstone-air-27627}

CMSC389R-{c0rn3rstone-air-27628}

CMSC389R-{c0rn3rstone-air-27629}

CMSC389R-{c0rn3rstone-air-27630}

CMSC389R-{c0rn3rstone-air-27631}

CMSC389R-{c0rn3rstone-air-27632}

CMSC389R-{c0rn3rstone-air-27633}

CMSC389R-{c0rn3rstone-air-27634}

CMSC389R-{c0rn3rstone-air-27635}

CMSC389R-{c0rn3rstone-air-27636}

CMSC389R-{c0rn3rstone-air-27637}

CMSC389R-{c0rn3rstone-air-27638}

CMSC389R-{c0rn3rstone-air-27639}

CMSC389R-{c0rn3rstone-air-27640}

CMSC389R-{c0rn3rstone-air-27641}

CMSC389R-{c0rn3rstone-air-27642}

CMSC389R-{c0rn3rstone-air-27643}

CMSC389R-{c0rn3rstone-air-27644}

CMSC389R-{c0rn3rstone-air-27645}

CMSC389R-{c0rn3rstone-air-27646}

CMSC389R-{c0rn3rstone-air-27647}

CMSC389R-{c0rn3rstone-air-27648}

CMSC389R-{c0rn3rstone-air-27649}

CMSC389R-{c0rn3rstone-air-27650}

CMSC389R-{c0rn3rstone-air-27651}

CMSC389R-{c0rn3rstone-air-27652}

CMSC389R-{c0rn3rstone-air-27653}

CMSC389R-{c0rn3rstone-air-27654}

CMSC389R-{c0rn3rstone-air-27655}

CMSC389R-{c0rn3rstone-air-27656}

CMSC389R-{c0rn3rstone-air-27657}

CMSC389R-{c0rn3rstone-air-27658}

CMSC389R-{c0rn3rstone-air-27659}

CMSC389R-{c0rn3rstone-air-27660}

CMSC389R-{c0rn3rstone-air-27661}

CMSC389R-{c0rn3rstone-air-27662}

CMSC389R-{c0rn3rstone-air-27663}

CMSC389R-{c0rn3rstone-air-27664}

CMSC389R-{c0rn3rstone-air-27665}

CMSC389R-{c0rn3rstone-air-27666}

CMSC389R-{c0rn3rstone-air-27667}

CMSC389R-{c0rn3rstone-air-27668}

CMSC389R-{c0rn3rstone-air-27669}

CMSC389R-{c0rn3rstone-air-27670}

CMSC389R-{c0rn3rstone-air-27671}

CMSC389R-{c0rn3rstone-air-27672}

CMSC389R-{c0rn3rstone-air-27673}

CMSC389R-{c0rn3rstone-air-27674}

CMSC389R-{c0rn3rstone-air-27675}

CMSC389R-{c0rn3rstone-air-27676}

CMSC389R-{c0rn3rstone-air-27677}

CMSC389R-{c0rn3rstone-air-27678}

CMSC389R-{c0rn3rstone-air-27679}

CMSC389R-{c0rn3rstone-air-27680}

CMSC389R-{c0rn3rstone-air-27681}

CMSC389R-{c0rn3rstone-air-27682}

CMSC389R-{c0rn3rstone-air-27683}

CMSC389R-{c0rn3rstone-air-27684}

CMSC389R-{c0rn3rstone-air-27685}

CMSC389R-{c0rn3rstone-air-27686}

CMSC389R-{c0rn3rstone-air-27687}

CMSC389R-{c0rn3rstone-air-27688}

CMSC389R-{c0rn3rstone-air-27689}

CMSC389R-{c0rn3rstone-air-27690}

CMSC389R-{c0rn3rstone-air-27691}

CMSC389R-{c0rn3rstone-air-27692}

CMSC389R-{c0rn3rstone-air-27693}

CMSC389R-{c0rn3rstone-air-27694}

CMSC389R-{c0rn3rstone-air-27695}

CMSC389R-{c0rn3rstone-air-27696}

CMSC389R-{c0rn3rstone-air-27697}

CMSC389R-{c0rn3rstone-air-27698}

CMSC389R-{c0rn3rstone-air-27699}

CMSC389R-{c0rn3rstone-air-27700}

CMSC389R-{c0rn3rstone-air-27701}

CMSC389R-{c0rn3rstone-air-27702}

CMSC389R-{c0rn3rstone-air-27703}

CMSC389R-{c0rn3rstone-air-27704}

CMSC389R-{c0rn3rstone-air-27705}

CMSC389R-{c0rn3rstone-air-27706}

CMSC389R-{c0rn3rstone-air-27707}

CMSC389R-{c0rn3rstone-air-27708}

CMSC389R-{c0rn3rstone-air-27709}

CMSC389R-{c0rn3rstone-air-27710}

CMSC389R-{c0rn3rstone-air-27711}

CMSC389R-{c0rn3rstone-air-27712}

CMSC389R-{c0rn3rstone-air-27713}

CMSC389R-{c0rn3rstone-air-27714}

CMSC389R-{c0rn3rstone-air-27715}

CMSC389R-{c0rn3rstone-air-27716}

CMSC389R-{c0rn3rstone-air-27717}

CMSC389R-{c0rn3rstone-air-27718}

CMSC389R-{c0rn3rstone-air-27719}

CMSC389R-{c0rn3rstone-air-27720}

CMSC389R-{c0rn3rstone-air-27721}

CMSC389R-{c0rn3rstone-air-27722}

CMSC389R-{c0rn3rstone-air-27723}

CMSC389R-{c0rn3rstone-air-27724}

CMSC389R-{c0rn3rstone-air-27725}

CMSC389R-{c0rn3rstone-air-27726}

CMSC389R-{c0rn3rstone-air-27727}

CMSC389R-{c0rn3rstone-air-27728}

CMSC389R-{c0rn3rstone-air-27729}

CMSC389R-{c0rn3rstone-air-27730}

CMSC389R-{c0rn3rstone-air-27731}

CMSC389R-{c0rn3rstone-air-27732}

CMSC389R-{c0rn3rstone-air-27733}

CMSC389R-{c0rn3rstone-air-27734}

CMSC389R-{c0rn3rstone-air-27735}

CMSC389R-{c0rn3rstone-air-27736}

CMSC389R-{c0rn3rstone-air-27737}

CMSC389R-{c0rn3rstone-air-27738}

CMSC389R-{c0rn3rstone-air-27739}

CMSC389R-{c0rn3rstone-air-27740}

CMSC389R-{c0rn3rstone-air-27741}

CMSC389R-{c0rn3rstone-air-27742}

CMSC389R-{c0rn3rstone-air-27743}

CMSC389R-{c0rn3rstone-air-27744}

CMSC389R-{c0rn3rstone-air-27745}

CMSC389R-{c0rn3rstone-air-27746}

CMSC389R-{c0rn3rstone-air-27747}

CMSC389R-{c0rn3rstone-air-27748}

CMSC389R-{c0rn3rstone-air-27749}

CMSC389R-{c0rn3rstone-air-27750}

CMSC389R-{c0rn3rstone-air-27751}

CMSC389R-{c0rn3rstone-air-27752}

CMSC389R-{c0rn3rstone-air-27753}

CMSC389R-{c0rn3rstone-air-27754}

CMSC389R-{c0rn3rstone-air-27755}

CMSC389R-{c0rn3rstone-air-27756}

CMSC389R-{c0rn3rstone-air-27757}

CMSC389R-{c0rn3rstone-air-27758}

CMSC389R-{c0rn3rstone-air-27759}

CMSC389R-{c0rn3rstone-air-27760}

CMSC389R-{c0rn3rstone-air-27761}

CMSC389R-{c0rn3rstone-air-27762}

CMSC389R-{c0rn3rstone-air-27763}

CMSC389R-{c0rn3rstone-air-27764}

CMSC389R-{c0rn3rstone-air-27765}

CMSC389R-{c0rn3rstone-air-27766}

CMSC389R-{c0rn3rstone-air-27767}

CMSC389R-{c0rn3rstone-air-27768}

CMSC389R-{c0rn3rstone-air-27769}

CMSC389R-{c0rn3rstone-air-27770}

CMSC389R-{c0rn3rstone-air-27771}

CMSC389R-{c0rn3rstone-air-27772}

CMSC389R-{c0rn3rstone-air-27773}

CMSC389R-{c0rn3rstone-air-27774}

CMSC389R-{c0rn3rstone-air-27775}

CMSC389R-{c0rn3rstone-air-27776}

CMSC389R-{c0rn3rstone-air-27777}

CMSC389R-{c0rn3rstone-air-27778}

CMSC389R-{c0rn3rstone-air-27779}

CMSC389R-{c0rn3rstone-air-27780}

CMSC389R-{c0rn3rstone-air-27781}

CMSC389R-{c0rn3rstone-air-27782}

CMSC389R-{c0rn3rstone-air-27783}

CMSC389R-{c0rn3rstone-air-27784}

CMSC389R-{c0rn3rstone-air-27785}

CMSC389R-{c0rn3rstone-air-27786}

CMSC389R-{c0rn3rstone-air-27787}

CMSC389R-{c0rn3rstone-air-27788}

CMSC389R-{c0rn3rstone-air-27789}

CMSC389R-{c0rn3rstone-air-27790}

CMSC389R-{c0rn3rstone-air-27791}

CMSC389R-{c0rn3rstone-air-27792}

CMSC389R-{c0rn3rstone-air-27793}

CMSC389R-{c0rn3rstone-air-27794}

CMSC389R-{c0rn3rstone-air-27795}

CMSC389R-{c0rn3rstone-air-27796}

CMSC389R-{c0rn3rstone-air-27797}

CMSC389R-{c0rn3rstone-air-27798}

CMSC389R-{c0rn3rstone-air-27799}

CMSC389R-{c0rn3rstone-air-27800}

CMSC389R-{c0rn3rstone-air-27801}

CMSC389R-{c0rn3rstone-air-27802}

CMSC389R-{c0rn3rstone-air-27803}

CMSC389R-{c0rn3rstone-air-27804}

CMSC389R-{c0rn3rstone-air-27805}

CMSC389R-{c0rn3rstone-air-27806}

CMSC389R-{c0rn3rstone-air-27807}

CMSC389R-{c0rn3rstone-air-27808}

CMSC389R-{c0rn3rstone-air-27809}

CMSC389R-{c0rn3rstone-air-27810}

CMSC389R-{c0rn3rstone-air-27811}

CMSC389R-{c0rn3rstone-air-27812}

CMSC389R-{c0rn3rstone-air-27813}

CMSC389R-{c0rn3rstone-air-27814}

CMSC389R-{c0rn3rstone-air-27815}

CMSC389R-{c0rn3rstone-air-27816}

CMSC389R-{c0rn3rstone-air-27817}

CMSC389R-{c0rn3rstone-air-27818}

CMSC389R-{c0rn3rstone-air-27819}

CMSC389R-{c0rn3rstone-air-27820}

CMSC389R-{c0rn3rstone-air-27821}

CMSC389R-{c0rn3rstone-air-27822}

CMSC389R-{c0rn3rstone-air-27823}

CMSC389R-{c0rn3rstone-air-27824}

CMSC389R-{c0rn3rstone-air-27825}

CMSC389R-{c0rn3rstone-air-27826}

CMSC389R-{c0rn3rstone-air-27827}

CMSC389R-{c0rn3rstone-air-27828}

CMSC389R-{c0rn3rstone-air-27829}

CMSC389R-{c0rn3rstone-air-27830}

CMSC389R-{c0rn3rstone-air-27831}

CMSC389R-{c0rn3rstone-air-27832}

CMSC389R-{c0rn3rstone-air-27833}

CMSC389R-{c0rn3rstone-air-27834}

CMSC389R-{c0rn3rstone-air-27835}

CMSC389R-{c0rn3rstone-air-27836}

CMSC389R-{c0rn3rstone-air-27837}

CMSC389R-{c0rn3rstone-air-27838}

CMSC389R-{c0rn3rstone-air-27839}

CMSC389R-{c0rn3rstone-air-27840}

CMSC389R-{c0rn3rstone-air-27841}

CMSC389R-{c0rn3rstone-air-27842}

CMSC389R-{c0rn3rstone-air-27843}

CMSC389R-{c0rn3rstone-air-27844}

CMSC389R-{c0rn3rstone-air-27845}

CMSC389R-{c0rn3rstone-air-27846}

CMSC389R-{c0rn3rstone-air-27847}

CMSC389R-{c0rn3rstone-air-27848}

CMSC389R-{c0rn3rstone-air-27849}

CMSC389R-{c0rn3rstone-air-27850}

CMSC389R-{c0rn3rstone-air-27851}

CMSC389R-{c0rn3rstone-air-27852}

CMSC389R-{c0rn3rstone-air-27853}

CMSC389R-{c0rn3rstone-air-27854}

CMSC389R-{c0rn3rstone-air-27855}

CMSC389R-{c0rn3rstone-air-27856}

CMSC389R-{c0rn3rstone-air-27857}

CMSC389R-{c0rn3rstone-air-27858}

CMSC389R-{c0rn3rstone-air-27859}

CMSC389R-{c0rn3rstone-air-27860}

CMSC389R-{c0rn3rstone-air-27861}

CMSC389R-{c0rn3rstone-air-27862}

CMSC389R-{c0rn3rstone-air-27863}

CMSC389R-{c0rn3rstone-air-27864}

CMSC389R-{c0rn3rstone-air-27865}

CMSC389R-{c0rn3rstone-air-27866}

CMSC389R-{c0rn3rstone-air-27867}

CMSC389R-{c0rn3rstone-air-27868}

CMSC389R-{c0rn3rstone-air-27869}

CMSC389R-{c0rn3rstone-air-27870}

CMSC389R-{c0rn3rstone-air-27871}

CMSC389R-{c0rn3rstone-air-27872}

CMSC389R-{c0rn3rstone-air-27873}

CMSC389R-{c0rn3rstone-air-27874}

CMSC389R-{c0rn3rstone-air-27875}

CMSC389R-{c0rn3rstone-air-27876}

CMSC389R-{c0rn3rstone-air-27877}

CMSC389R-{c0rn3rstone-air-27878}

CMSC389R-{c0rn3rstone-air-27879}

CMSC389R-{c0rn3rstone-air-27880}

CMSC389R-{c0rn3rstone-air-27881}

CMSC389R-{c0rn3rstone-air-27882}

CMSC389R-{c0rn3rstone-air-27883}

CMSC389R-{c0rn3rstone-air-27884}

CMSC389R-{c0rn3rstone-air-27885}

CMSC389R-{c0rn3rstone-air-27886}

CMSC389R-{c0rn3rstone-air-27887}

CMSC389R-{c0rn3rstone-air-27888}

CMSC389R-{c0rn3rstone-air-27889}

CMSC389R-{c0rn3rstone-air-27890}

CMSC389R-{c0rn3rstone-air-27891}

CMSC389R-{c0rn3rstone-air-27892}

CMSC389R-{c0rn3rstone-air-27893}

CMSC389R-{c0rn3rstone-air-27894}

CMSC389R-{c0rn3rstone-air-27895}

CMSC389R-{c0rn3rstone-air-27896}

CMSC389R-{c0rn3rstone-air-27897}

CMSC389R-{c0rn3rstone-air-27898}

CMSC389R-{c0rn3rstone-air-27899}

CMSC389R-{c0rn3rstone-air-27900}

CMSC389R-{c0rn3rstone-air-27901}

CMSC389R-{c0rn3rstone-air-27902}

CMSC389R-{c0rn3rstone-air-27903}

CMSC389R-{c0rn3rstone-air-27904}

CMSC389R-{c0rn3rstone-air-27905}

CMSC389R-{c0rn3rstone-air-27906}

CMSC389R-{c0rn3rstone-air-27907}

CMSC389R-{c0rn3rstone-air-27908}

CMSC389R-{c0rn3rstone-air-27909}

CMSC389R-{c0rn3rstone-air-27910}

CMSC389R-{c0rn3rstone-air-27911}

CMSC389R-{c0rn3rstone-air-27912}

CMSC389R-{c0rn3rstone-air-27913}

CMSC389R-{c0rn3rstone-air-27914}

CMSC389R-{c0rn3rstone-air-27915}

CMSC389R-{c0rn3rstone-air-27916}

CMSC389R-{c0rn3rstone-air-27917}

CMSC389R-{c0rn3rstone-air-27918}

CMSC389R-{c0rn3rstone-air-27919}

CMSC389R-{c0rn3rstone-air-27920}

CMSC389R-{c0rn3rstone-air-27921}

CMSC389R-{c0rn3rstone-air-27922}

CMSC389R-{c0rn3rstone-air-27923}

CMSC389R-{c0rn3rstone-air-27924}

CMSC389R-{c0rn3rstone-air-27925}

CMSC389R-{c0rn3rstone-air-27926}

CMSC389R-{c0rn3rstone-air-27927}

CMSC389R-{c0rn3rstone-air-27928}

CMSC389R-{c0rn3rstone-air-27929}

CMSC389R-{c0rn3rstone-air-27930}

CMSC389R-{c0rn3rstone-air-27931}

CMSC389R-{c0rn3rstone-air-27932}

CMSC389R-{c0rn3rstone-air-27933}

CMSC389R-{c0rn3rstone-air-27934}

CMSC389R-{c0rn3rstone-air-27935}

CMSC389R-{c0rn3rstone-air-27936}

CMSC389R-{c0rn3rstone-air-27937}

CMSC389R-{c0rn3rstone-air-27938}

CMSC389R-{c0rn3rstone-air-27939}

CMSC389R-{c0rn3rstone-air-27940}

CMSC389R-{c0rn3rstone-air-27941}

CMSC389R-{c0rn3rstone-air-27942}

CMSC389R-{c0rn3rstone-air-27943}

CMSC389R-{c0rn3rstone-air-27944}

CMSC389R-{c0rn3rstone-air-27945}

CMSC389R-{c0rn3rstone-air-27946}

CMSC389R-{c0rn3rstone-air-27947}

CMSC389R-{c0rn3rstone-air-27948}

CMSC389R-{c0rn3rstone-air-27949}

CMSC389R-{c0rn3rstone-air-27950}

CMSC389R-{c0rn3rstone-air-27951}

CMSC389R-{c0rn3rstone-air-27952}

CMSC389R-{c0rn3rstone-air-27953}

CMSC389R-{c0rn3rstone-air-27954}

CMSC389R-{c0rn3rstone-air-27955}

CMSC389R-{c0rn3rstone-air-27956}

CMSC389R-{c0rn3rstone-air-27957}

CMSC389R-{c0rn3rstone-air-27958}

CMSC389R-{c0rn3rstone-air-27959}

CMSC389R-{c0rn3rstone-air-27960}

CMSC389R-{c0rn3rstone-air-27961}

CMSC389R-{c0rn3rstone-air-27962}

CMSC389R-{c0rn3rstone-air-27963}

CMSC389R-{c0rn3rstone-air-27964}

CMSC389R-{c0rn3rstone-air-27965}

CMSC389R-{c0rn3rstone-air-27966}

CMSC389R-{c0rn3rstone-air-27967}

CMSC389R-{c0rn3rstone-air-27968}

CMSC389R-{c0rn3rstone-air-27969}

CMSC389R-{c0rn3rstone-air-27970}

CMSC389R-{c0rn3rstone-air-27971}

CMSC389R-{c0rn3rstone-air-27972}

CMSC389R-{c0rn3rstone-air-27973}

CMSC389R-{c0rn3rstone-air-27974}

CMSC389R-{c0rn3rstone-air-27975}

CMSC389R-{c0rn3rstone-air-27976}

CMSC389R-{c0rn3rstone-air-27977}

CMSC389R-{c0rn3rstone-air-27978}

CMSC389R-{c0rn3rstone-air-27979}

CMSC389R-{c0rn3rstone-air-27980}

CMSC389R-{c0rn3rstone-air-27981}

CMSC389R-{c0rn3rstone-air-27982}

CMSC389R-{c0rn3rstone-air-27983}

CMSC389R-{c0rn3rstone-air-27984}

CMSC389R-{c0rn3rstone-air-27985}

CMSC389R-{c0rn3rstone-air-27986}

CMSC389R-{c0rn3rstone-air-27987}

CMSC389R-{c0rn3rstone-air-27988}

CMSC389R-{c0rn3rstone-air-27989}

CMSC389R-{c0rn3rstone-air-27990}

CMSC389R-{c0rn3rstone-air-27991}

CMSC389R-{c0rn3rstone-air-27992}

CMSC389R-{c0rn3rstone-air-27993}

CMSC389R-{c0rn3rstone-air-27994}

CMSC389R-{c0rn3rstone-air-27995}

CMSC389R-{c0rn3rstone-air-27996}

CMSC389R-{c0rn3rstone-air-27997}

CMSC389R-{c0rn3rstone-air-27998}

CMSC389R-{c0rn3rstone-air-27999}

