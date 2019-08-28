# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
import numpy as np

"""
num=np.arange(729).reshape(9,9,9)
x=0
y=1

if(x==0 and y==1):
    num[3:6,0:3,0:3]==num[0:3,0:3,3:6]
    print (num)
"""

def fun(x,y,num):  

    """
    profundidad 
    
    """
    
    fila1 = np.array([0,1,2,9,10,11,18,19,20])
    fila2 = np.array([3,4,5,12,13,14,21,22,23])
    fila3 = np.array([6,7,8,15,16,17,24,25,26])
    
    columna1 = np.array([0,3,6,9,12,15,18,21,24])
    columna2 = np.array([1,4,7,10,13,16,19,22,25])
    columna3 = np.array([2,5,8,11,14,17,20,23,26])
    

    if x>=0 and x<=8:
       xo1=0
       xo2=3
    elif x>8 and x<=17:   
       xo1=3
       xo2=6
    elif x>17 and x<=26:   
       xo1=6
       xo2=9

    if y>=0 and y<=8:
        xi1=0
        xi2=3
    elif y>8 and y<=17:   
       xi1=3
       xi2=6
    elif y>17 and y<=26:   
       xi1=6
       xi2=9       
    
"""
filas
""""    
    
    for i in range(fila1.shape[0]):     
        if fila1[i]==x:
            f1=1
            f2=0
            f3=0
    for i in range(fila2.shape[0]):     
        if fila2[i]==x:
            f1=0
            f2=1
            f3=0        
    for i in range(fila3.shape[0]):     
        if fila3[i]==x:
            f1=0
            f2=0
            f3=1
    
    if f1==1:
        yo1=0
        yo2=3
    elif f2==1:
        yo1=3
        yo2=6
    elif f3==1:
        yo1=6
        yo2=9
        
    for i in range(fila1.shape[0]):     
        if fila1[i]==y:
            f1=1
            f2=0
            f3=0
    for i in range(fila2.shape[0]):     
        if fila2[i]==y:
            f1=0
            f2=1
            f3=0        
    for i in range(fila3.shape[0]):     
        if fila3[i]==y:
            f1=0
            f2=0
            f3=1
    
    if f1==1:
        yi1=0
        yi2=3
    elif f2==1:
        yi1=3
        yi2=6
    elif f3==1:
        yi1=6
        yi2=9        
 
"""
columna
"""    
    
    for i in range(columna1.shape[0]):
        if columna1[i]==x:
            c1=1
            c2=0
            c3=0
    for i in range(columna2.shape[0]):
        if columna2[i]==x:
            c1=0
            c2=1
            c3=0
    for i in range(columna3.shape[0]):
        if columna3[i]==x:
            c1=0
            c2=0
            c3=1
            
    if c1==1:
        zo1=0
        zo2=3
    elif c2==1:
        zo1=3
        zo2=6
    elif c3==1:
        zo1=6
        zo2=9
        
        
    for i in range(columna1.shape[0]):
        if columna1[i]==y:
            c1=1
            c2=0
            c3=0
    for i in range(columna2.shape[0]):
        if columna2[i]==y:
            c1=0
            c2=1
            c3=0
    for i in range(columna3.shape[0]):
        if columna3[i]==y:
            c1=0
            c2=0
            c3=1
            
    if c1==1:
        zi1=0
        zi2=3
    elif c2==1:
        zi1=3
        zi2=6
    elif c3==1:
        zi1=6
        zi2=9

              
        
    num1=np.array(num[xo1:xo2,yo1:yo2,zo1:zo2])
    num3=np.copy(num1)
        
    num[xo1:xo2,yo1:yo2,zo1:zo2]=num[xi1:xi2,yi1:yi2,zi1:zi2]
    num[xi1:xi2,yi1:yi2,zi1:zi2]=num3
        
    print (num)

    
x = int(input('Ingrese un numero: '))
y = int(input('Ingrese un numero: '))
num = np.arange(729).reshape(9,9,9)
fun(x,y,num)
