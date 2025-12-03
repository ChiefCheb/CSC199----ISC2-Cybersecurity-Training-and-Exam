# BuckeyeCTF 2025 – Hackathon Summary

## Event Overview
- **Event:** BuckeyeCTF 2025 (Ohio State University)
- **Dates:** Nov 7–9, 2025
- **Team:** StringersUp (2 members)
- **Score:** 200 points
- **Placement:** 430 / 716 teams
- **Links:** 
  - Event: https://ctftime.org/event/2883
  - Team: https://ctftime.org/team/411625

## Challenges Attempted
### 1. Decryption Challenge (COMPLETED)
- **Description:** The challenge gave us an "email.txt" file with a uuencoded attachment, which we had to decode to find the flag
- **What I did:** To start, I created a controlled Linux environment by creating a VM on VirtualBox. I used a sharefile to transfer
                  "email.txt", and ran "uudecode email.txt". This gave me a DOS program called "FLGPRNTR.COM". In order to run it,
                  I installed DOSBox on my Linux VM, mounted the DOS program to it, and ran it, which printed out the flag shown in
                  the screenshot below. I then submitted the flag.
- **Screenshot:** <img width="525" height="166" alt="Screenshot_2025-11-07_174648" src="https://github.com/user-attachments/assets/9123f0d2-3328-443f-a311-c76820bc8641" />


### 2. OS Simulation Challenge (COMPLETED)
- **Description:** The challenge gave us a program called "cosmonaut.com" which we were supposed to use to find the flag.
- **What I did:** My teammate ran the program on their Linux device, which yielded a partial flag: "bctf{4_7ru3_", and a
                  hint: "Cosmonauts run their programs everywhere and all at once.\nLike on Linux!". This gave us the
                  idea to run the program on different operating systems in order to try to get the rest of the flag. I
                  downloaded the program and ran it on my Windows PC, which gave me a similar output: "Cosmonauts run their
                  programs everywhere and all at once.\nLike on Windows!", followed by a partial flag:
                  "c05m0p0l174n_c0nn353ur_". With most of the flag discovered, I decided to run the program on MAC, since
                  that's the next most logical choice. Unfortunately, neither I nor my partner owned any MAC devices, so
                  I tried to set up a VM using VirtualBox again. This attempt was foiled, as pirating a MAC ISO is illegal.
                  So, I tried to set up an Amazon EC2 MAC instance. After hacking into my own Microsoft account (they are
                  very strict about their authentications), I tried to set up the instance over and over, but failed each
                  time. With that attempt also exhausted, I looked online for a tip on running programs on a remote MAC
                  device. I learned that Git workflows can actually be used to simulate different OSs, so I created a repo
                  (I should've used this one but it slipped my mind at the time.), put the program there, and learned how
                  to write a git workflow. After many attempts, I finally succeeded in running the program, getting the
                  following result: "Cosmonauts run their programs everywhere and at once.\nExcept here...". Needless to
                  say, this isn't what I was looking for, so I checked in with my partner, and we agreed that the next
                  OS to try was FreeBSD. So, thankfully FreeBSD is free, so I downloaded an ISO and took another while to
                  setup the VM (setup was manual and I had to configure file system partitions, network settings, etc.).
                  Once set up, I tried to transfer the program to the VM from my host using a plethora of options (ssh, shared
                  folders, etc.), but all of them failed. Finally, I decided to turn the program into an ISO using a
                  python script, then attached it to the VM before launching it. Once launched and loggin in as root, I
                  mounted the ISO, copied the program into root, changed its permission, and ran it, and finally got the
                  last part of the flag: "Cosmonauts run their programs everywhere and all at once.\nLike on FreeBSD!", and
                  "kn0w5_n0_b0und5}". After all that, I went back and collected the frangments of the flag all together,
                  combined them, and submitted them on the CTF website to complete the challenge. 
                       
- **Screenshot:** <img width="846" height="725" alt="Screenshot 2025-12-02 232134" src="https://github.com/user-attachments/assets/a80c6637-860a-44a0-9dee-99932bd2df26" />
                  <img width="701" height="334" alt="Screenshot_2025-11-07_221649" src="https://github.com/user-attachments/assets/f83f5398-4244-4dbf-84f8-6fe736b4861a" />


### 3. Pwn Challenge (ATTEMPTED)
- **Description:** For this challenge, I decided to take on something I was completely unfamiliar with. A PWN challenge.
- **What I tried:** I kept seeing these challeges all over the board, and they really captured my interest because I'd never tried
                    them before. So, I watched a few PWN tutorials, and set about trying to crack this one. The premise of this
                    PWN is to connect to an exposed endpoint, and find a way to make it do something it "wasn't meant" to do. To
                    start, I explored the intended use of the endpoint: it was meant to take an input, and depending on the user's
                    command, supposed to output the binary of a hexadecimal value, or vice versa. There was also a command to
                    output the programs memory (dd) and also a command to list the addresses of the defined functions, one of which
                    was the function to print the flag. After doing some more research, I figured that the idea behind the solution
                    was for the user to send a payload to overflow the buffer to a very specific point, and overwrite the return
                    jump with the address of the print flag function. For some time, I tried to do this manually to see if I can
                    overflow the buffer to make the program break and output anything other than the intended output. After a few
                    tries, it became clear that wasn't going to happen, so I decided to try to do this programatically with a
                    python script. Unfortunately, soon after I wrote a script that finally yileded any sort of output, the
                    hackathon ended, and I wasn't able to submit the flag for this challenge. 
- **Screenshot:** Running my python script and it crashing
                  <img width="701" height="395" alt="Screenshot 2025-11-08 165302" src="https://github.com/user-attachments/assets/9b7a9e60-d0d9-4e1b-bbf5-e44727714b17" />


## Tools & Workflows Used
- 

## What I Learned
- 

