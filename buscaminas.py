from   tkinter   import *
from   tkinter   import ttk
from   tkinter   import messagebox
from   functools import partial
from   tkinter   import PhotoImage
from   tkinter   import font
import random
import time
#Programa Funcion===============================================================
def creacion_matriciana(fi,co):
    matriz = [None] * fi
    for n in range (fi):
        matriz[n] = [None] * co

    return(matriz)
#--------------------------------------------------------------------
def creacion_matriz_estado(fi,co):
    matriz = [None] * fi
    for n in range (fi):
        matriz[n] = [None] * co

    for i in range(fi):
        for j in range(co):
            matriz[i][j] = False
        
    return(matriz)
#--------------------------------------------------------------------     
def cargar_matriz_num(matriz_num, fi, co):
    for n in range(fi):
        for z in range(co):
            matriz_num[n][z] = 0
#--------------------------------------------------------------------
def cargar_minas(matriz_num):
    minas = int(0)
    while(minas < 8):
        f = random.randint(0,7)
        c = random.randint(0,7)
        
        while(matriz_num[f][c] == 4):
            f = random.randint(0,7)
            c = random.randint(0,7)
        matriz_num[f][c] = 4

        if(f > 0 and c > 0 and matriz_num[f-1][c-1] != 4):   #NO
            matriz_num[f-1][c-1] += 1
                
        if(f > 0 and matriz_num[f-1][c] != 4):               #N
            matriz_num[f-1][c] += 1
            
        if(f > 0 and c < 7 and matriz_num[f-1][c+1] != 4):  #NE
            matriz_num[f-1][c+1] += 1
                
        if(c < 7 and matriz_num[f][c+1] != 4):              #E
            matriz_num[f][c+1] += 1
                
        if(f < 7 and c < 7 and matriz_num[f+1][c+1] != 4): #SE
            matriz_num[f+1][c+1] +=1
                
        if(f < 7 and matriz_num[f+1][c] != 4):              #S
            matriz_num[f+1][c] += 1
                
        if(f < 7 and c > 0 and matriz_num[f+1][c-1] != 4):  #SO
            matriz_num[f+1][c-1] += 1
                
        if(c > 0 and matriz_num[f][c-1] != 4):               #O
            matriz_num[f][c-1] += 1
                     
                
        minas +=1
#Funcion Crear Vector imagenes++++++++++++++++++++++++++++++++++++++++++++++++
def vector_imagenes():
    vector_img=[]
    vector_img.append(PhotoImage(file= 'vacio.png'))       #0
    vector_img.append(PhotoImage(file= 'uno.png'))         #1
    vector_img.append(PhotoImage(file= 'dos.png'))         #2
    vector_img.append(PhotoImage(file= 'tres.png'))        #3
    vector_img.append(PhotoImage(file= 'vacio.png'))       #4
    vector_img.append(PhotoImage(file= 'mina.png'))        #5
    vector_img.append(PhotoImage(file= 'minaroja.png'))    #6
    vector_img.append(PhotoImage(file= 'bandera.png'))     #7
    vector_img.append(PhotoImage(file= 'bandera_mal.png')) #8
    
    return(vector_img)
#Funcion Del clikear botones++++++++++++++++++++++++++++++++++++++++++++++++++
def voltear_vacias(matriz_num, matriz_btn, matriz_est, n,z):
    if(not matriz_est[n][z]):
        matriz_est[n][z]= True
        matriz_btn[n][z]= Label(image = vector_img[matriz_num[n][z]], background = 'gray76',
                                borderwidth = 1, relief = 'solid')
        
        matriz_btn[n][z].place(x = (80*n)+55, y = (80*z)+55, height = 80, width = 80)
        app.update()

        if(matriz_num[n][z] == 0):
            if(n > 0 and z > 0 and matriz_num[n-1][z-1] != 4):  #NO
                voltear_vacias(matriz_num, matriz_btn, matriz_est, n-1,z-1)

            if(n > 0 and matriz_num[n-1][z] != 4):              #N
                voltear_vacias(matriz_num, matriz_btn, matriz_est, n-1,z)
  
            if(n > 0 and z < 7 and matriz_num[n-1][z+1] != 4):  #NE
                voltear_vacias(matriz_num, matriz_btn, matriz_est, n-1,z+1)
                         
            if(z < 7 and matriz_num[n][z+1] != 4):              #E
                voltear_vacias(matriz_num, matriz_btn, matriz_est, n,z+1)
        
            if(n < 7 and z < 7 and matriz_num[n+1][z+1] != 4):  #SE
                voltear_vacias(matriz_num, matriz_btn, matriz_est, n+1,z+1)
                      
            if(n < 7 and matriz_num[n+1][z] != 4):              #S
                voltear_vacias(matriz_num, matriz_btn, matriz_est, n+1,z)
          
            if(n < 7 and z > 0 and matriz_num[n+1][z-1] != 4):  #SO
                voltear_vacias(matriz_num, matriz_btn, matriz_est, n+1,z-1)
                      
            if(z > 0 and matriz_num[n][z-1] != 4):              #O
                voltear_vacias(matriz_num, matriz_btn, matriz_est, n,z-1)
#Funcion ganar++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def ganaste():
    cont = int(0)
    for i in range(8):
        for j in range(8):
            if(matriz_est[i][j] == True ):
                cont += 1

    if(cont == 56):
        reaccion_btn.configure(image = reaccion[2])
        messagebox.showinfo(title='Buscaminas', message='Felicidades, Ganaste')
        app.update()
        time.sleep(2)
        app.destroy()   
#Funcion Boton Click++++++++++++++++++++++++++++++++++++++++++++++++++++++++++                  
def boton_click(n, z):
    matriz_btn[n][z].configure(image= vector_img[int(matriz_num[n][z])])
    app.update()

    if(matriz_num[n][z] == 4):
        matriz_btn[n][z].configure(image = vector_img[6])
        reaccion_btn.configure(image = reaccion[1])
        messagebox.showerror(title='Buscaminas', message='Tocaste una mina! Perdiste')
        app.update()
        time.sleep(2)
        app.destroy()
        
    elif(matriz_num[n][z] != 4):
        voltear_vacias(matriz_num, matriz_btn, matriz_est, n,z)

    ganaste()
#Funcion Cargar Botones+++++++++++++++++++++++++++++++++++++++++++++++++++++++
def cargamiento_botones(matriz_btn, matriz_num, matriz_est, vector_img, reaccion, reaccion_btn):

    for n in range(8):
        for z in range(8):
            matriz_btn[n][z]= Button(image= vector_img[0], borderwidth=6,
                                     background = 'gray76', command=partial(boton_click,n, z))

            matriz_btn[n][z].place(x = (80*n)+55, y = (80*z)+55, height = 80, width = 80)

            matriz_btn[n][z].bind('<Button-3>', lambda event, a=n, b=z: boton_derecho(a,b))

            app.update()
#Funcion Boton Derecho+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def boton_derecho(a, b):
    matriz_btn[a][b].configure(image= vector_img[7])
    app.update()
#Funcion vector reacciones+++++++++++++++++++++++++++++++++++++++++++++++++++++
def vector_reaccion():
    reaccion = []
    reaccion.append(PhotoImage(file = 'sonrisa.png'))
    reaccion.append(PhotoImage(file = 'perdio.png '))
    reaccion.append(PhotoImage(file = 'ganaste.png'))

    return(reaccion)
#Funcion Estetica+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def marco_estetica():
    frame = Frame(background = 'gray76', relief = 'raised', borderwidth = 10 )
    frame.place(x= 0, y= 0, width = '50', height = '750')
    #-------------------------------------------------------------------------
    frame2 = Frame(background = 'gray76', relief = 'raised', borderwidth = 10 )
    frame2.place(x= 950, y= 0, width = '50', height = '750')
    #-------------------------------------------------------------------------
    frame3 = Frame(background = 'gray76', relief = 'raised', borderwidth = 10 )
    frame3.place(x= 700, y= 0, width = '50', height = '750')
    #-------------------------------------------------------------------------
    frame4 = Frame(background = 'gray76', relief = 'raised', borderwidth = 10 )
    frame4.place(x= 0, y= 0, width = '1000', height = '50')
    #-------------------------------------------------------------------------
    frame5 = Frame(background = 'gray76', relief = 'raised', borderwidth = 10 )
    frame5.place(x= 0, y= 699, width = '1000', height = '50')

    label = Label(background= 'gray76')
    label.place(x= 5, y= 640, width = '35', height = '50')

    label2 = Label(background= 'gray76')
    label2.place(x= 5, y= 10, width = '35', height = '50')

    label9 = Label(background= 'gray76')
    label9.place(x= 5, y= 680, width = '35', height = '50')

    label10 = Label(background= 'gray76')
    label10.place(x= 705, y= 680, width = '35', height = '50')

    label11 = Label(background= 'gray76')
    label11.place(x= 955, y= 680, width = '35', height = '50')

    labelaux2 = Label(background= 'white')
    labelaux2.place(x= 0, y= 10, width = '5', height = '50')

    label3 = Label(background= 'gray76')
    label3.place(x= 955, y= 10, width = '35', height = '50')

    labelaux3 = Label(background= 'gray46')
    labelaux3.place(x= 990, y= 10, width = '5', height = '50')

    label4 = Label(background= 'gray76')
    label4.place(x= 955, y= 640, width = '35', height = '50')

    labelaux4 = Label(background= 'gray46')
    labelaux4.place(x= 990, y= 680, width = '5', height = '50')

    labelaux8 = Label(background= 'black')
    labelaux8.place(x= 995, y= 680, width = '5', height = '50')

    label5 = Label(background= 'gray76')
    label5.place(x= 705, y= 10, width = '35', height = '50')

    labelaux5 = Label(background= 'black')
    labelaux5.place(x= 995, y= 640, width = '5', height = '50')

    label6 = Label(background= 'gray76')
    label6.place(x= 705, y= 640, width = '35', height = '50')

    labelaux6 = Label(background= 'gray46')
    labelaux6.place(x= 740, y= 40, width = '5', height = '50')

    labelaux7 = Label(background= 'gray46')
    labelaux7.place(x= 40, y= 40, width = '5', height = '50')  
#Programa Principal=============================================================

app = Tk ()
app.title    ("Busca Minas")
app.geometry ("1000x800"   )
#app.iconbitmap('minesweeper.ico')
app.configure(background='gray76')
#Componentes====================================================================
fi   = int(8)
co   = int(8)
#Matrices----------------------------------------------------------------------
matriz_num = creacion_matriciana(fi,co)
matriz_btn = creacion_matriciana(fi,co)
matriz_est = creacion_matriz_estado(fi,co)

cargar_matriz_num(matriz_num, fi, co)
cargar_minas(matriz_num)
#------------------------------------------------------------------------------
vector_img = vector_imagenes()
reaccion = vector_reaccion()
reaccion_btn = Button(image = reaccion[0], borderwidth= 6, background = 'gray76')
reaccion_btn.place(x = 810, y = 290, height = 80, width = 80)

cargamiento_botones(matriz_btn, matriz_num, matriz_est , vector_img, reaccion, reaccion_btn)
marco_estetica()

for i in range(8):
    for j in range(8):
        print(matriz_num[j][i], end='')
    print()         
#===============================================================================
app.mainloop()