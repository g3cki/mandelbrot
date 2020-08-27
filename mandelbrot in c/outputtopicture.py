from PIL import Image
import subprocess
import os


#subprocess.run(["./mandelbrot/c#/mandelbrote"])                                # optional works under linux starts c script and then works instantly with the output

with open ("/home/adm1n/Documents/mandelbrot/c#/output.txt" , "r+") as file:    # open picture
    picture = file.readlines()                                                  

widthheigth = len(picture)                                                      # get the width and heigth of picture
                                                                                
im = Image.new('RGB', (widthheigth, widthheigth), color = (0, 0, 0))            # create image
pix = im.load()

counter = 0

for y in range(0,widthheigth):                                                  # run through the array and color every pixel                                              
    tempxlinearray = picture[y].split("/")
    for x in range(0,widthheigth):
        if int(tempxlinearray[x]) != 100:
            pix[x,y] = (0, 0, 0)                                                # color pixel black
        else:
            pix[x,y] = (255, 255, 255)                                          # color pixel white
        

os.remove("/home/adm1n/Documents/mandelbrot/c#/output.txt")                     # remove file

im.save('/home/adm1n/Documents/mandelbrot/c#/mandelbrot.png')                   # save image
