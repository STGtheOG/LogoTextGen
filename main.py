# This is a sample Python script.
import copy
import os
from math import floor, ceil
from PIL import Image, ImageDraw, ImageFont
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


base_image = Image.open("All_Team_Logos.png")
blank_icon = Image.new("RGBA",(91,91), (255,255,255,0))
blank_banner = Image.new("RGBA",(154,55), (255,255,255,0))

base_MSS = Image.open("MS_scoreboard.png")
blank_Score = Image.new("RGBA",(64,64), (0,0,0,255))

base_MST = Image.open("MS_text.png")
dMST = ImageDraw.Draw(base_MST)
blank_Txt = Image.new("RGBA",(32,32), (0,0,0,255))

dMST.font = ImageFont.truetype(font="tahomabd.ttf", size=248)

#print(base_image.size)
MS_files = ["tex1_512x128_36f2aabb09127bd4_14","tex1_256x64_aeb43fd19b34337a_14"]
IB_locations = [["Mario",2,0,0,0,0,0,"MF"],
                ["Luigi",3,0,1,0,0,1,"LK"],
                ["Peach",0,2,4,0,0,4,"PM"],
                ["Daisy",2,1,5,0,0,5,"DF"],
                ["Yoshi",2,2,6,0,0,6,"YE"],
                ["Birdo",0,0,1,1,1,2,"BB"],
                ["Wario",1,1,8,0,1,0,"WM"],
                ["Waluigi",1,0,0,1,1,1,"WS"],
                ["DonkeyKong",3,1,2,0,0,2,"DW"],
                ["DiddyKong",1,2,3,0,0,3,"DM"],
                ["Bowser",3,2,7,0,0,7,"BM"],
                ["BowserJr",0,1,0,2,1,3,"BR"]]

Stad_Info = [["tex1_256x256_0df697f8be986f07_14","Mario",96,80,16,0,""],
             ["tex1_256x256_965be7bcb78faeea_14","Luigi",128,64,16,0,""],
             ["tex1_256x128_8bb507857cb62392_14","Peach",112,32,8,-1,""],
             ["tex1_128x64_3adb42876318e76e_14","Daisy",56,36,4,0,""],
             ["tex1_256x256_11c716243c436c06_14","Yoshi",256,0,0,0,""],
             ["tex1_128x128_2fc33009c91cb1a3_14","Wario",112,8,8,0,"Wario"],
             ["tex1_256x256_92ff2cd0a340874a_14","DonkeyKong",96,80,0,0,""],
             ["tex1_128x128_e8cdbfbf2611229f_14","Bowser",96,16,16,0,"Bowser"],
             ["tex1_256x256_dfce413a313257cc_14","BowserJr",256,0,0,0,"Junior"]]

Output_files = ["tex1_512x512_a0f0024083f9b5a0_43dd6fb452bec1fa_9","tex1_512x512_a0f0024083f9b5a0_65062f74db7a1428_9","tex1_512x512_a0f0024083f9b5a0_b4691a041414bc7e_9",
                "tex1_512x512_a0f0024083f9b5a0_9b776bcade781332_9","tex1_512x512_a0f0024083f9b5a0_651f239bfbf97258_9","tex1_512x512_a0f0024083f9b5a0_873be0531a8fe343_9",
                "tex1_512x512_a0f0024083f9b5a0_d9f557e41c8e4dd1_9","tex1_512x512_a0f0024083f9b5a0_d9db46731d24d353_9","tex1_512x512_a0f0024083f9b5a0_f1169ded63327825_9",
                "tex1_512x512_a0f0024083f9b5a0_7f05fe10a5ab1b39_9","tex1_512x512_a0f0024083f9b5a0_82809c95d716595d_9","tex1_512x512_a0f0024083f9b5a0_aedffb74ba549d36_9",
                "tex1_512x512_a0f0024083f9b5a0_bd7273d9b7fb5eb1_9","tex1_512x512_a0f0024083f9b5a0_1cbb6189c7349886_9","tex1_512x512_a0f0024083f9b5a0_8a26cb61bbf750f1_9",
                "tex1_512x512_a0f0024083f9b5a0_25b1b23d19db3c4a_9","tex1_512x512_a0f0024083f9b5a0_a87e3ac788f7473a_9","tex1_512x512_a0f0024083f9b5a0_6c06764002e6dd97_9",
                "tex1_512x512_a0f0024083f9b5a0_9d1e374e2afca01d_9","tex1_512x512_a0f0024083f9b5a0_328f31f469f29588_9","tex1_512x512_a0f0024083f9b5a0_d06200237e47051d_9",
                "tex1_512x512_a0f0024083f9b5a0_df97de5b9db1227c_9","tex1_512x512_a0f0024083f9b5a0_f82b4d4139a4de9a_9"]


sett_extras = True

def edit_stad(txt,icon,size, x, y, rot, mask):
    #tex1_256x256_0df697f8be986f07_14.png
    stad = Image.open("StadTextures/"+txt+ ".png")
    if not os.path.exists("Input/" + icon + "S.png"):
        stad.save("Output/"+txt+".png")
        return
    r = rot
    print(r)
    img = Image.open("Input/"+icon+"S.png").convert("RGBA").resize((size,size))
    while r <0:
        img = img.transpose(Image.ROTATE_90)
        r+=1
    while r >0:
        img = img.transpose(Image.ROTATE_270)
        r-=1
    imgmask = Image.new("RGBA",(size,size),(255,255,255,0))
    if os.path.exists("Masks/" + mask + ".png"):
        imgmask.paste(img,(0,0), Image.open("Masks/" + mask+ ".png").convert("RGBA"))
    else:
        imgmask.paste(img, (0, 0))
    if sett_extras and os.path.exists("Input/"+icon+"S.png"):
        stad.paste(img, (x,y,x+size,y+size),imgmask)
    stad.save("Output/" +txt +".png")



def edit_base(name, ri, ci, rb, cb, sr, sc,txt):
    if os.path.exists("Input/" + name + ".png"):
        add_icon(Image.open("Input/"+name+".png"), ri, ci)
        add_sc(Image.open("Input/"+name+".png"),sr,sc,txt)
    if os.path.exists("Input/"+name+"B.png"):
        add_banner(Image.open("Input/"+name+"B.png"),rb ,cb )


def add_sc(image, row, column, txt):
    size = 60
    padding = (64-size)/2
    left = 64 * column
    right = 64 * (column+1)
    top = 64 * row
    bottom = 64 * (row+1)
    adding = image.resize((size, size))
    base_MSS.paste(blank_Score, (left,top,right, bottom))
    base_MSS.paste(adding, (left+floor(padding), top+floor(padding), right-ceil(padding), bottom-ceil(padding)))
    p = column + 8*row
    c = p % 6
    r = floor(p / 6)
    base_MST.paste(blank_Txt,(32*c,32*r,32*(c+1),32*(r+1)))

    ln = ceil(dMST.textlength(txt))+16
    newImg = Image.new("RGBA",(ln,248),(0,0,0,255))
    d = ImageDraw.Draw(newImg)
    d.font = dMST.getfont()
    d.text((16,-16),txt, fill =(255,191,0,255))

    base_MST.paste(newImg.resize((32,32)), (32 * c, 32 * r, 32 * (c + 1), 32 * (r + 1)))


def add_icon(image, row, column):
    size = 80
    padding = (91-size)/2
    left = (155 + (91 * column))+floor(padding)
    right = (246 + (91 * column))-ceil(padding)
    top = (0 + (91 * row))+floor(padding)
    bottom = (91 + (91 * row)) - ceil(padding)
    adding = image.resize((size, size))
    base_image.paste(blank_icon, ((155 + (91 * column)),(0 + (91 * row)),(246 + (91 * column)),(91 + (91 * row))))
    #base_image.paste(adding, (0, 0, 81, 81))
    base_image.paste(adding, (left, top, right, bottom))

def add_banner(image, row, column):
    width = 150
    height =50
    paddingW = (154 - width) / 2
    paddingH = (55 - height)/2
    left = 154*column
    right = 154*(column+1)
    top = 55*row + ((91*4) if column > 0 else 0)
    bottom = top+55
    adding = image.resize((150, 50))
    base_image.paste(blank_banner, (left, top, right, bottom))
    # base_image.paste(adding, (0, 0, 81, 81))
    base_image.paste(adding, (left+floor(paddingW), top+floor(paddingH), right-ceil(paddingW), bottom-ceil(paddingH)))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


for v in IB_locations:
    edit_base(v[0],v[1],v[2],v[3],v[4],v[5],v[6],v[7])

base_image.save("New_Team_Logos.png")
base_MSS.save("New_MS_Scoreboard.png")
base_MST.save("New_MS_Text.png")
for v in Output_files:
    base_image.save("Output/" + v + ".png")

if sett_extras:
    for v in Stad_Info:
        edit_stad(v[0],v[1],v[2],v[3],v[4],v[5],v[6])

