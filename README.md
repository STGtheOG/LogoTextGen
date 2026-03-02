# LogoTextGen

An image editor for use alongside Mario Super Sluggers. Takes in team logos and applies images to the scoreboard UI and to a texture within home stadiums.

# How to use:
    
Add team logos and Banners to the Input folder. Logos should be 1:1 in width:height, while banners should be 3:1. Name the files as character + the following:

".png" - Logo

"B.png" - Banner

For Example, if I want to edit Mario's Logo and Banner, I'd add the files and name them

"Mario.png"

"MarioB.png"

The Characters are as follows:
Mario, Luigi, Peach, Daisy, Yoshi, Birdo, Wario, Waluigi, DonkeyKong, DiddyKong, Bowser, BowserJr

Additionally, should you wish to add logos to stadiums, add them as character + "S.png". So, if I wanted to add a logo to Mario Stadium, I'd add the file:

"MarioS.png"

# Notes

This program only uses .png files.

If you wish to stop creating stadium files, there's a variable "sett_extra", set it to false.

Everything in the output can be easily moved to your texture folder in Dolphin