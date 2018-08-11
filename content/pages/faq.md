Title: Frequently Asked Questions (FAQ)


Are you interested in trying out this year's OpenCTF contest, but you have no
idea what’s going on? This document is for you!


## What is Capture the Flag?

Whether you are new to computer security or are a veteran,
[Capture the Flag (CTF)](https://en.wikipedia.org/wiki/Capture_the_flag#Computer_security)
competitions are a great way to both learn new skills and hone existing
ones. CTF competitions are a series of computer security challenges, with teams
competing to solve the most challenges and earn the most points.

It's *Hacker Sport*.


## What is OpenCTF?

OpenCTF is a CTF competition, being run at this year’s [DEFCON](https://defcon.org/).
OpenCTF is **open to all players** of any skill level, with no
pre-registration or qualification required. Formerly called "amatuer CTF,"
OpenCTF has been running since DEFCON , and has traditionally been
passed on from one organizing group to another.

Come on by, try out the game, learn something new, and meet interesting people!


## How do I play CTF?

There are multiple formats and styles of CTF, but they all have one thing in
common - the challenges. Players are presented with puzzles, programs with
security vulnerabilities, or systems to break in to. Embedded in the puzzle,
program, or system, is a secret key, or “flag”. Finding this flag is proof that
you solved the puzzle, and submitting it to the scoreboard earns your team
points. Flags are typically chosen to look very distinctive, so that when you
see one, you’ll know it’s a flag, and that you’ve solved the puzzle. Flags in
OpenCTF will tend to be a phrase or sentence in [l33tsp34k](https://en.wikipedia.org/wiki/Leet), for example,
`ther5s_n0_Place_l1ke_h0m3`.


## How do I play OpenCTF?

See: "[Getting Started]({filename}/pages/getting-started.md)"


## Do I need a team?

While you can participate solo, you’ll probably have a much better time if you
play with a team. Get a few friends, sit down, and work together to solve
challenges. After the beginning of the game, there’s multiple challenges open,
so each person can work on their own, or they can try to collaborate to solve
one.  If none of your friends want to play, ask some of the existing teams
whether they want an extra member. It’s a great way to meet new people, and
learn skills you’ve never even heard of!


## What should I bring?

You will need a computer of some sort to play. Typically people play with
laptops.

The ability to run VMs is very helpful, so that you can use Windows, Linux,
or whatever else the contest requires. It also allows you to isolate programs
which could potentially be dangerous.  For that matter, it’s a good idea to just
use a fresh hard drive, with no personal data on it, that you can just wipe
after DEFCON.

This *is* DEFCON, you should consider using a burner laptop anyway :)

OpenCTF will provide each table with physical connections to the contest network,
and there will be a power strip at each table. You should bring your own power
strip (the provided one may not have enough outlets), and some way to share the
one physical network connection you get. Since this may or may not be ethernet,
we recommend being prepared to use either one players laptop or a dedicated
laptop as a router. An ethernet switch and enough cables for everyone on your
team is also advised.


## Challenges

There’s a wide variety of challenges that show up in a CTF, but they tend to be
grouped into a few categories:

### Web

These challenges involve attacking common vulnerabilities in web technology.
For example, you might need to use SQL injection to read the `secret_flag` table
of a database, use directory traversal to get a web server to serve you
`flag.txt`, use Cross-Site Scripting to trick a simulated user to send you their
password, or bypass some client-side checks implemented by obfuscated javascript.

### Digital Forensics

This is a fairly broad category. You might receive an image of
a disk in FAT format, and you’ll need to un-delete `flag.txt`. Maybe you receive
a zip file, that contains a 7z file, that contains a tar archive, that contains
some obscure file format you’ve never heard of, and unpacking the entire chain
eventually gives you a flag.

### Steganography

Steganography is the art of hiding a
secret message in plain sight, and it leads to a variety of implementations and
challenges. yoU might be given an image, where all the blue pixels can be
filtered out to reveal a seCret message. maybe an innocuous Http transfer hides
A Secret flag. or maybe a video file, That’s been subtly watermarked witH the
secret flag. maybe a paragraph of text hIdes a secret message in the capital
letterS.

### Packet Analysis

In this category, you’ll typically receive a packet
capture dump (a "pcap"), and you’ll try to decode, analyze, and interpret it, using tools
such as Wireshark. Maybe a simulated user was sending their password in
plaintext, and you have to retrieve it. Or, perhaps a simulated user was having
a VOIP call without encryption, and you need to listen in and hear the secret
flag.

### Binary Reversing

Several categories of challenge involve
reverse engineering programs. You’ll receive the program, but not the source code, so
you need to disassemble it, look at the assembly code, and figure out what it does
(and if it has any weaknesses!). Programs can be x86 Windows, x86 Linux, ARM
Linux, obfuscated Java, and a whole bevy of more obscure formats.

Sub-categories include:

- **Pwnables:** The program you received is running as a service on a remote
machine. Reverse-engineer it, figure out its vulnerability, and use that to take
exploit the remote service into serving you a flag. Often, there’s a `flag.txt`
you can get the program to read, or perhaps it has a flag in memory you need to
get it to accidentally send you. Or, sometimes you are able to just execute
shellcode, and read a `flag.txt` directly.

- **Crackmes:** These programs include
anti-reversing measures, like anti-debugger instructions, code obfuscation, or
even dual-use opcodes. There’s a few ways the flag could be embedded - the
program could implement a particular password check, and the string that is
accepted is the flag, or perhaps the program calculates the decryption of an
encrypted flag, but requires rewriting certain instructions so that it performs
the decryption.

### Cryptography

In this category, you’ll attack poorly implemented
crypto, outdated crypto, or use well-known vulnerabilities to attack encrypted
messages. You might be given a few RSA keys whose modulus share a factor, and
you decrypt a message encrypted by one of these keys. Or you’re given a password
database with unsalted password hashes. You could get a cipher, where you can
guess some of the plaintext, and use that to figure out the key and decrypt the
remainder of the message. Or, it could just be ROT13.

### Miscellaneous

Miscellaneous is, well, miscellaneous. These are often lower-point value
challenges that ask for trivia, or bizarre messages that just have to looked at
with the right perspective, or programs that will output the key, if you can get
them to run correctly. This could also be a bitmap image, printed out in Base64
over several pages of tractor-feed paper, that you need to OCR into a computer,
in order to view the secret flag on the image.


## What formats are there for CTF? How does the whole contest work, outside of individual challenges?

There are a few common formats for CTF.

In *"Jeopardy-style*", there is a board full of challenges in various categories. At
the beginning of the game, only one challenge is open, and all others are closed
(inaccessible). The first team to solve the open challenge gets to pick another
challenge to open, which becomes the new *"lead question"*. Previously opened
challenges remain open, so slower teams can still solve and submit them for
points. Solving the lead question gives you the privilege of picking the next
challenge to open, which becomes the new lead question. Each challenge is worth
points, and the team with the most points at the end of the game, wins.

**OpenCTF is a Jeopardy-style contest.**

Some CTFs follow a linear path, where you start on one challenge, and solving it
unlocks the next challenge, but only for you. The first team to solve all
challenges, in sequence, wins.

There’s also *"Attack/Defense*", or *"Player VS Player (PvP)"* contests.
In these, instead of the contest
organizers running the game servers, individual teams do. You gain points by
capturing the flag off of your opponent’s servers, and you lose points either by
having your flags captured, or when your servers are offline. Instead of merely
needing to solve challenges, you also need to defend yourself from other teams,
and patch the vulnerabilities that you discover. The team with the most points at the
end of the game wins.

**DEFCON CTF is Attack/Defense style.**


## Any hints or tips?

- Make copious use of Google.
- These challenges were written by people, and these people want to see the challenges
solved. If you get stuck, it can be worth asking for a hint, especially if you
have a good idea of what you’ve tried so far and what you’re stuck on.
Sometimes, just talking aloud with the author is a good way of getting that
burst of inspiration. Or, the author can point out if you’re on the right track,
or way off base.  If you get stuck, you can also just take a break, try a
different challenge, and come back to this challenge later.
- If you’re programming, minimizing time spent coding is your goal.
You’re writing code that will be **used once**.
Maintainability, readability, and robustness aren’t concerns.
Make it pretty for the writeup later.
- Linux shell utilities are your friend. I’ve solved many challenges with one-liners.
Some helpful utilities include:

| Tool          | Description                                          |
| ------------- | ---------------------------------------------------- |
| `imagemagick` | creation, modification and display of bitmap images |
| `sox`         | the Swiss Army knife of audio manipulation          |
| `sed`         | stream editor for filtering and transforming text   |
| `awk`         | pattern scanning and processing language            |
| `grep`        | print lines matching a pattern                      |
| `strings`     | print the strings of printable characters in files  |
| `file`        | determine file type                                 |
| `xxd`         | make a hexdump or do the reverse                    |
| `sort`        | sort lines of text files                            |
| `uniq`        | report or omit repeated lines                       |

- Some other teams may prank or troll you. This can be all in good fun, but it helps
to have a thick skin about these kinds of things. (Again, this is DEFCON). Prank or
troll them back!  But please also be reasonable, and don’t do anything that
causes lasting damage.

**If you feel another team has really crossed the line, talk to the contest organizers.**

Have Fun!

