from tkinter import *
from PIL import Image, ImageDraw , ImageFilter
from PIL import ImagePath
from PIL import ImageTk
import math
import random

global idraw

def val(hval):
    global w
    global h
    global hcab
    global idraw
    global wrad
    idraw.ellipse( (w / 2 - w / 10 , hval - w / 10 , w / 2 + w / 10 , hval + w / 10 ), fill = "black")
    idraw.polygon( ( 0 , hval , w / 2  ,  hval + w / 20 , w , hval , w / 2  ,  hval - w / 20 , ), fill = "black" )
    idraw.rectangle(( w / 2 - w / 50 , h / 100 , w / 2 + w / 50 , hval  ), fill = "black" )
    idraw.rectangle(( 0 , hval - wrad , w/3-w / 50  , hval + wrad  ), fill = "black" )
    idraw.ellipse( ( 0 , hval - wrad - wrad / 10, w/3-w / 50  , hval - wrad + wrad / 10  ), fill = "black")
    idraw.ellipse( ( 0 , hval + wrad - wrad / 10, w/3-w / 50  , hval + wrad + wrad / 10  ), fill = "black")
    idraw.rectangle(( 0 , hval - wrad , w/3-w / 50  , hval + wrad  ), fill = "black" )
    idraw.ellipse( ( 0 , hval - wrad - wrad / 10, w/3-w / 50  , hval - wrad + wrad / 10  ), fill = "black")
    idraw.ellipse( ( 0 , hval + wrad - wrad / 10, w/3-w / 50  , hval + wrad + wrad / 10  ), fill = "black")
    idraw.rectangle(( w/3*2+w / 50 , hval - wrad , w  , hval + wrad  ), fill = "black" )
    idraw.ellipse( ( w/3*2+w / 50 , hval - wrad - wrad / 10, w  , hval - wrad + wrad / 10  ), fill = "black")
    idraw.ellipse( ( w/3*2+w / 50 , hval + wrad - wrad / 10, w  , hval + wrad + wrad / 10  ), fill = "black")

def sedlo(hsed):
    global w
    global h
    global idraw
    global srad
    idraw.ellipse(( w/2.5 - srad , hsed - srad , w / 2.5 + srad ,  hsed + srad  ) , fill = "slategrey" )
    idraw.ellipse(( w - w/2.5 - srad , hsed - srad , w - w / 2.5 + srad ,  hsed + srad  ) , fill = "slategrey" )
    idraw.rectangle((w/2.5 , hsed - srad , w - w / 2.5   , hsed + srad  ), fill = "slategrey" )
    idraw.polygon( ( w/2.5 - srad , hsed , w / 3 , hsed + srad * 2 , w / 3 + srad, hsed + srad * 2 , w / 2 , hsed - srad ,w / 3 * 2 - srad , hsed + srad * 2 ,w / 3 * 2  , hsed + srad * 2 , w - w/2.5 + srad , hsed  ), fill = "slategrey" , outline = "white")

def rama():
    global w
    global h
    global idraw
    idraw.rectangle((w/3-w / 50,100, w/3+w / 30, h), fill='grey')
    idraw.rectangle((w/3*2-w / 30,100, w/3*2+w / 50, h), fill='grey')

def cab(hcab):
    global w
    global h
    global idraw
    idraw.polygon((w / 50 ,h / 100, w - w / 50 , h / 100 , w , hcab ,0 , hcab ), fill = "red" )
    idraw.ellipse((w/50 , 0 , w - w / 50 , h / 50), fill="darkblue")
    idraw.ellipse((w/50 , 0 + h / 200 , w - w / 50 , h / 50 + h / 200 ), fill="red")

    idraw.polygon((w / 50 , hcab / 3, w - w / 50 , hcab / 3 , w , hcab ,0 , hcab), fill = "darkred" )
    idraw.ellipse((w / 50 , hcab / 3 - hcab / 12 , w - w / 50 , hcab / 3 + hcab / 12), fill="darkred")

    idraw.ellipse((( 0 , hcab , ( w/3-w / 50 ) / 2 , hcab + ( w/3-w / 50 ) / 2 )), fill="black")
    idraw.ellipse((( w/3-w / 50 ) / 2 , hcab , ( w/3-w / 50 ) , hcab + ( w/3-w / 50 ) / 2 ), fill="black")
    idraw.ellipse((( 0  , hcab + h / 8 , ( w/3-w / 50 ) / 2 , hcab + ( w/3-w / 50 ) / 2 + h / 8)), fill="black")
    idraw.ellipse((( w/3-w / 50 ) / 2 , hcab + h / 8, ( w/3-w / 50 ) , hcab + ( w/3-w / 50 ) / 2 + h / 8 ), fill="black")
    idraw.rectangle((0 , hcab + ( w/3-w / 50 ) / 4, w/3-w / 50 , hcab + ( (w/3- w / 50) / 4 ) + h / 8  ), fill = "darkgrey" )
    idraw.rectangle((0 , hcab + ( w/3-w / 50 ) / 4 + h / 100 , w/3-w / 50 , hcab + ( (w/3- w / 50) / 4 ) + h / 8 - h / 100 ), fill = "black" )

    idraw.ellipse((( ( w/3 * 2  + w / 50 ) , hcab , w , hcab + h / 50)), fill="black")
    idraw.ellipse((( ( w/3 * 2  + w / 50 ) , hcab + ( w/3-w / 50 ) / 2 + h / 8 - h / 50 , w , hcab + ( w/3-w / 50 ) / 2 + h / 8)), fill="black")
    idraw.rectangle((( w/3 * 2  + w / 50 ) , hcab + h / 100, w , hcab + ( w/3-w / 50 ) / 2 + h / 8 - h / 100  ), fill = "darkgrey" )
    idraw.rectangle((( w/3 * 2  + w / 50 ) , hcab + h / 50, w , hcab + ( w/3-w / 50 ) / 2 + h / 8 - h / 50  ), fill = "black" )
def fur(w1,h1,hcab,hsed,mval):#ширина , длинна фуры, длинна кабины, положение седла , массив с положением осей.
    global w
    global h
    global idraw
    global wrad
    global srad
    w = w1 
    h = h1 
    
    img = Image.new('RGBA', (int(w),int(h)), color=0 )
    idraw = ImageDraw.Draw(img)
    hsed = h - hsed
    wrad = w / 4
    srad = w / 8
    for hval in mval:
        val( h - hval )
    rama()
    cab(hcab)
    sedlo( hsed )
    #img = img.resize((w1, h1), Image.ANTIALIAS)
    
    img.save("fursv.png")

def pric ( wpric , hpric ):   
    imgc = Image.new('RGBA', (int(wpric),int(hpric)), color="darkred" )
    idrawc = ImageDraw.Draw(imgc)
    imgc.save("pricsv.png")
def col ( wpric , dcol ):   
    imgc = Image.new('RGBA', (int(wpric // 10 ),int(dcol)), color="black" )
    idrawc = ImageDraw.Draw(imgc)
    imgc.save("col.png")
def asfalt (w,h):
    w1 = w // 2
    h1 = h // 2
    imgf = Image.new('RGBA', (w,h), color="black" )
    r = [0,0,0,0]
    idrawf = ImageDraw.Draw(imgf)
    color = ["black","dimgrey","white","grey","slategrey","silver"]
    for i in range(w*h//4):
       r[0] = random.randint(0, w)
       r[1] = random.randint(0, h)
       r[2] = r[0] + 1
       r[3] = r[1] + 1
       idrawf.rectangle(r, fill = color[random.randint(0, 5)] )           
    imgf = imgf.filter(ImageFilter.GaussianBlur(radius=1))  
    imgf.save("fon.png")
#ширина , длинна фуры, длинна кабины, положение седла , массив с положением осей.

