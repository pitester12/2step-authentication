# 2step-authentication
this code will generate a time-based One-time password that expires in a certain amount of time that you can run scripts using this
reqirements:
linux system: (ubuntu based or debian based. such as elementary os, pop os, linux mint, kali linux, Q4OS, sparkly linux and MXLinux)


how to download:

sudo apt update && sudo apt upgrade && sudo apt install git && sudo apt install python3 && sudo apt-get install python3-pip && pip install pyotp 

how to clone this github repo:
git clone https://github.com/pitester12/2step-authentication/
cd 2step-authentication

how to run:

python3 totp-GENERATE-No-QR.py #this generates the totp
python3 totp-RECEIVER #this reseves the totp

IMPORTANT:
You can't run the totp generator multiple times in withing the expiration date 

DONATE MONERO: 453ottx4pLWCUxj8c592PS2gTwGQZdh45gjW3PgzotJobi8srydhm5A93ZKKp9Cdp7De5DXC1hFXd252HMvGrJTg7VRxW8H
DONATE BITCOIN: 1NAbqot6pHmysXVWegCrRTyya5BXzRuzFt
