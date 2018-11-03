Writeup 8 - Forensics II, Network Analysis and File Carving/Parsing
=====

Name: *Ivan Quiles*
Section: *0201*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Ivan Quiles*

## Assignment 8 Writeup

### Part 1 (45 Pts)
1. Yes! The hackers did use `traceroute`. They used it once on `csec-vip.umiacs.umd.edu`. 

2. Names: laz0rh4x and c0uchpot4doz

3. Their ip addresses are 142.93.118.186 and 104.248.224.85. There are connecting to each other from Digital Ocean servers.

4. Port 33794

5. They didn't directly mention their plans but they gave a drive link and mentioned that they plan to do it tomorrow at 15:00. This would be October 25th @3pm

6. https://drive.google.com/file/d/1McOX5WjeVHNLyTBNXqbOde7l8SAQ3DoI/view and the file is named update.fpff

7. They mention they'll see each other "tomorrow" which is October 25th the same day as their plan.

### Part 2 (55 Pts)

*Report your answers to the questions about parsing update.fpff below.*

1. Generated At Unix Timestamp 1540428007. Date: Thu, 25 Oct 2018 00:40:07 GMT

2.The author is laz0rh4x

3. It is supposed to have 9 sections but it really has 11 sections

4.
-------  BODY  -------
SECTION 1: Call this number to get your flag: (422) 537 - 7946, SECTION TYPE: SECTION_ASCII

SECTION 2: ['3', '1', '4', '1', '5', '9', '2', '6', '5', '3', '5', '8', '9', '7', '9'], SECTION TYPE: SECTION_WORDS

SECTION 3: (38.991610,-77.027540), SECTION TYPE: SECTION_COORD

SECTION 4: This is a pointer pointing to block 1, SECTION TYPE: SECTION_REFERENCE

SECTION 5: The imfamous security pr0s at CMSC389R will never find this!, SECTION TYPE: SECTION_ASCII

SECTION 6: The first recorded uses of steganography Can be traced back to 440 BC when Herodotus Mentions two exampleS in his Histories.[3] Histicaeus s3nt a message to his vassal, Arist8goras, by sha9ving the hRead of his most trusted servan-t, "marking" the message onto his scal{p, then sending him on his way once his hair had rePrown, withl the inastructIon, "WheN thou art come to Miletus, bid _Aristagoras shave thy head, and look thereon." Additionally, demaratus sent a warning about a forthcoming attack to Greece by wrIting it dirfectly on the wooden backing oF a wax tablet before applying i_ts beeswax surFace. Wax tablets were in common use then as reusabLe writing surfAces, sometimes used for shorthand. In his work Polygraphiae Johannes Trithemius developed his so-called "Ave-Maria-Cipher" that can hide information in a Latin praise of God. "Auctor Sapientissimus Conseruans Angelica Deferat Nobis Charitas Gotentissimi Creatoris" for example contains the concealed word VICIPEDIA.[4}, SECTION TYPE: SECTION_ASCII

SECTION 7: (38.991094,-76.932802), SECTION TYPE: SECTION_COORD

SECTION 8: PNG saved to output8.png, SECTION TYPE: SECTION_PNG

SECTION 9: AF(saSAdf1AD)Snz**asd1, SECTION TYPE: SECTION_ASCII

SECTION 10: Q01TQzM4OVIte2gxZGQzbi1zM2N0MTBuLTFuLWYxbDN9
, SECTION TYPE: SECTION_ASCII

SECTION 11: ['4', '8', '15', '16', '23', '42'], SECTION TYPE: SECTION_DWORDS


5. From the photo: CMSC389R-{c0rn3rst0ne_airlin3s_to_the_m00n}. Phone Call Flag: dc16051. Well at least I called it I don't know if it was actually a flag.
