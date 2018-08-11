Title: Getting Started


If you still have questions after following the registration procedures, check the [FAQ]({filename}/pages/faq.md).


## Registration

1. Go to the right side of our event table, where the little receipt
   printer is.
1. Give your team name.
1. You will receive a printed receipt with a SSH key (the QR code) and a
   password for the shell box.
1. Use a QR reader to scan the receipt code, and save the SSH key to your
   machine.


## Connecting to Contest WiFi

If you were lucky enough to find a free network cable, congrats.
For everyone else, we are coodinating wireless access with the DefCon NOC.
Our WiFi runs on the same hardware as the official WiFi, and should be
accessible near and far.

1. Register for DefCon Wifi: [https://wifireg.defcon.org](https://wifireg.defcon.org)
1. Using the **exact same** settings as the DefCon WiFi, connect to the OpenCTF SSID: `openCTF`.


## Accessing the Scoreboard

The contest scoreboard is located at: **[scoreboard.openctf.com](https://scoreboard.openctf.com)** (172.31.1.5).

You can view a real time listing of open/solved challenges and the leaderboard
through the web.

To submit flags, you need to log into the scoreboard via SSH. Only key
authentication is allowed (no passwords). For example, if your registered
team name is `f00` and you saved your SSH key as `$HOME/.ssh/mykey`, then
connect with:

```
ssh -i $HOME/.ssh/mykey f00@scoreboard.openctf.com
```

## The Shell Box

If you don't have a *nix machine, or are limited to a web browser, fear not!

We are providing a FreeBSD shell box to players, accessible over SSH and HTTPS,
located at: **[shell.openctf.com](https://shell.openctf.com)** (172.31.2.2).

You can authenticate with either the SSH key or password on your registration
receipt.
