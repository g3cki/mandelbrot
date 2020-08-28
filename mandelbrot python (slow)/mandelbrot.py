import math
from PIL import Image

                                            # width and height 1 to 1
width = 10000                               # von -2 bis 1
height = 10000                              # von -1,5 bis 1,5
iterations = 131                            # can be freely chosen
maxiterations = iterations
xstart = -2                                 
xstartsave = xstart
ystart = -1.5          
distance = 3         
intervall = 1/(width/distance)


im = Image.new('RGB', (width, height), color = (0, 0, 0)) 
pix = im.load()


def calc(iterations,z):
    if iterations == maxiterations:
        return iterations
    if abs(z) > 2:
        return iterations-1
    return calc(iterations+1,z*z+c)


for a in range(0,height):
    ystart = ystart + intervall
    xstart = xstartsave
    for b in range(0,width):
        xstart = xstart + intervall
        c = complex(xstart,ystart)
        iterations = 0
        calcresult = calc(iterations,0)

        if calcresult != maxiterations and calcresult != 0:             # The coloring

            i = calcresult%10

            if i == 0:
                pix[b,a] = (66, 30, 15)
            elif i == 1:
                pix[b,a] = (25, 7, 26)
            elif i == 2:
                pix[b,a] = (9, 1, 47)
            elif i == 3:
                pix[b,a] = (4, 4, 73)
            elif i == 4:
                pix[b,a] = (0, 7, 100)
            elif i == 5:
                pix[b,a] = (12, 44, 138)
            elif i == 6:
                pix[b,a] = (24, 82, 177)
            elif i == 7:
                pix[b,a] = (57, 125, 209)
            elif i == 8:
                pix[b,a] = (134, 181, 229)
            elif i == 9:
                pix[b,a] = (211, 236, 248)  
            
        
        else:
            pix[b,a] = (0, 0, 0)

im.save('/home/adm1n/Documents/mandelbrot/Python/mandelbrot.png')
