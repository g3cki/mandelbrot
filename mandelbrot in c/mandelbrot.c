#include<stdio.h>

// Create an new Datatype to save an complex number
struct array2{ long double real; long double imag; };

// Function to square an complex number
struct array2 squarecomplexnum(struct array2 complexnumber){

    long double real = complexnumber.real;
     
    complexnumber.real = (complexnumber.real*complexnumber.real)+(complexnumber.imag*complexnumber.imag)*(-1);
    complexnumber.imag = 2*real*complexnumber.imag;

    return complexnumber;
}
// Function to add an complexnumber
struct array2 addcomplexnum(struct array2 complexnumber1,struct array2 complexnumber2){

    complexnumber1.imag = complexnumber1.imag + complexnumber2.imag;
    complexnumber1.real = complexnumber1.real + complexnumber2.real;

    return complexnumber1;
}
// Function that calculates the mandelbrot set 
// returns the number of iterations
int calcmandelbrot(struct array2 complexnumber,struct array2 savecomplexnumber,int maxiterations,int iterations){

    if (maxiterations == iterations){
        return iterations;
    }
    if ((complexnumber.imag*complexnumber.imag + complexnumber.real*complexnumber.real) >= 4)
    {
        return iterations;
    }
    return calcmandelbrot(addcomplexnum(squarecomplexnum(complexnumber),savecomplexnumber),savecomplexnumber,maxiterations,iterations+1);
}


void main(){
// Create outputfile
    FILE *fp;
    fp = fopen("/home/adm1n/Documents/mandelbrot/c#/output.txt", "w+");

// calculating depth 100 is generally ok for small sizes up to 30000x30000 pixel
    int maxiterations = 100;
// the left and bottom border of your calculation window 
    float vary = -1.5;
    float varx = -2.1;
// the distance u want to calculate from the borders above
    float distance = 1.5;
// the length in pixels of one side
    int settings = 1000;

    double intervall = distance/settings;
    struct array2 v = {varx,vary};

    for (int x = 0;x<settings;x++){
        v.imag = v.imag + intervall;                                // change complex number component to new
        v.real = varx;                                              // reset var
        for (int y = 0;y<settings;y++){
            v.real = v.real + intervall;                            // change complex number to new
            int result = calcmandelbrot(v,v,maxiterations,0);       // calculate the function
            fprintf(fp, "%d/",result);                              // print the iterations to file
            }
        fprintf(fp,"\n");                                           // start new line
        }
    fclose(fp);                                                     // close file
}
