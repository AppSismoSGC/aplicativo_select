#!/usr/bin/env python
from Tkinter import *
import tkFileDialog
import datetime
import tkMessageBox
import Tkinter
import sys
import os
import subprocess
import os, time, math, tempfile
import numpy 
from glob import glob

try:
    import Gnuplot, Gnuplot.PlotItems, Gnuplot.funcutils
except ImportError:
    # kludge in case Gnuplot hasn't been installed as a module yet:
    import __init__
    Gnuplot = __init__
    import PlotItems
    Gnuplot.PlotItems = PlotItems
    import funcutils
    Gnuplot.funcutils = funcutils


class Planificador(Frame):
    def __init__(self,master):
        Frame.__init__(self, master)
        self.master = master
        self.initUI()

    def initUI(self):
        self.master.title("Select")
        self.frameOne = Frame(self.master)
        self.frameOne.grid(row=0,column=0)
        self.frameTwo = Frame(self.master)
        self.frameTwo.grid(row=1, column=0)
        #self.frameTwo = Toplevel(self.master)
	#self.frameTwo.grid(row=1, column=0)
	self.frameThree = Frame(self.master)
        self.frameThree.grid(row=2, column=0)
	self.frameFour = Frame(self.master)
        self.frameFour.grid(row=3, column=0)
	
	#parametros=glob("/home/Cmunoz/read_select/select.inp")
	#archivo=open(parametros[0],"r")
	##print "Nombre del archivo : ", archivo.name
	##print "Cerrado o no : ", archivo.closed
	##print "Modo de apertura : ", archivo.mode
	#lines=archivo.readlines()
	##print (lines[0])
	#contenido = ''
	
	self.menu_inicial()
	
############################Ventana Inicial####################################

    def menu_inicial(self):
	self.frameTwo.destroy()
	self.frameThree.destroy()
	self.frameFour.destroy()
	self.frameOne=Toplevel()
	self.select = Button(self.frameOne,text="CARGAR SELECT", command=self.ir_select,width=14)
	self.select.grid(row=1, column=0, pady=(5,5))
	self.mapas = Button(self.frameOne,text="MAPAS", command=self.ir_mapas, width=8)
	self.mapas.grid(row=2, column=1, pady=(5,5))
	self.graficas = Button(self.frameOne,text="GRAFICAS_GNUPLOT",command=self.ir_graficas, width=16)
	self.graficas.grid(row=3, column=2, pady=(5,5))
	self.graficas = Button(self.frameOne,text="GRAFICAS_PYTHON",command=self.ir_graficas2, width=16)
	self.graficas.grid(row=4, column=2, pady=(5,5))
	self.tablas = Button(self.frameOne,text="TABLAS", width=8)
	self.tablas.grid(row=4, column=3, pady=(5,5))
	self.salir2=Button(self.frameOne, text='Salir', command=self.quit)
	self.salir2.grid(row=5, column=4, padx=(5,5))
	   
   

	

    #def aceptar_piezas(self):
    #    try:
    #        val = int(self.entrypiezas.get())
    #        self.aceptar_piezas_ok()
    #    except ValueError:
    #        showerror('Error', "Introduce un numero")

    def ir_select(self):
        #self.frameOne.grid_remove()
	self.frameOne.destroy()

	self.frameTwo=Toplevel()
	self.texto = Label(self.frameTwo, height='3', text = "SELECT\n", justify="center")
        self.texto.grid(row=0, column=3)
	
	v1 = StringVar()
	v2 = StringVar()
	self.v3 = StringVar()
	self.v4 = StringVar()
	v5 = StringVar()
	v6 = StringVar()
	self.v7 = StringVar()
	self.v8 = StringVar()
	self.v9 = StringVar()
	self.v10 = StringVar()
	v11 = StringVar()
	v12 = StringVar()
	v13 = StringVar()
	v14 = StringVar()
	v15 = StringVar()
	v16 = StringVar()
	v17 = StringVar()
	v18 = StringVar()
	v19 = StringVar()
	v20 = StringVar()
	v21 = StringVar()
	v22 = StringVar()
	v23 = StringVar()
	v24 = StringVar()
	v25 = StringVar()
	v26 = StringVar()
	v27 = StringVar()
	v28 = StringVar()
	v29 = StringVar()
	v30 = StringVar()
	v31 = StringVar()
	v32 = StringVar()
	v33 = StringVar()
	v34 = StringVar()
	v35 = StringVar()

	Var1 = IntVar()
	Var2 = IntVar()
	self.Var3 = IntVar()
	Var4 = IntVar()
	Var5 = IntVar()
	Var6 = IntVar()
	self.Var7 = IntVar()
	self.Var8 = IntVar()
	self.Var9 = IntVar()
	self.Var10 = IntVar()
	Var11 = IntVar()
	Var12 = IntVar()
	Var13 = IntVar()
	Var14 = IntVar()
	Var15 = IntVar()
	Var16 = IntVar()
	Var17 = IntVar()
	Var18 = IntVar()
	Var19 = IntVar()
	Var20 = IntVar()
	Var21 = IntVar()
	Var22 = IntVar()
	Var23 = IntVar()
	Var24 = IntVar()
	Var25 = IntVar()
	Var26 = IntVar()
	Var27 = IntVar()
	Var28 = IntVar()
	Var29 = IntVar()
	Var30 = IntVar()
	Var31 = IntVar()
	Var32 = IntVar()
    	Var33 = IntVar()
	Var34 = IntVar()
	Var35 = IntVar()
	
##################################Ventana del select################################
	os.system("cp  select_inp_estandar/select.inp .")
	
	def var_states():
	   print("Base de Datos: %d,\nTipo: %d,\nTiempo Inicial: %d,\nTiempo Final: %d," % (Var1.get(), Var2.get(), self.Var3.get(), Var4.get()))
	
	
	def select():
	   os.system("/bd/seismo/PRO/select select.inp")
	def inp():
	   os.system("soffice select.inp &")
	


	self.check = Checkbutton(self.frameTwo, variable = Var1, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=14, column=0)
	self.check = Checkbutton(self.frameTwo, variable = Var2, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=15, column=0)
	self.check = Checkbutton(self.frameTwo, variable = self.Var3, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=16, column=0)
	self.check = Checkbutton(self.frameTwo, variable = Var4, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=17, column=0)
	
	
	self.textopieza = Label(self.frameTwo, text = "Base de Datos", justify="left")
        self.textopieza.grid(row=14, column=1)
	self.textopieza = Label(self.frameTwo, text = "Tipo", justify="left")
        self.textopieza.grid(row=15, column=1)
	self.textopieza = Label(self.frameTwo, text = "Tiempo Inicial", justify="left")
        self.textopieza.grid(row=16, column=1)
	self.textopieza = Label(self.frameTwo, text = "Tiempo Final", justify="left")
        self.textopieza.grid(row=17, column=1)


	
	self.check = Checkbutton(self.frameTwo, variable = Var5, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=1, column=3)
	self.check = Checkbutton(self.frameTwo, variable = Var6, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=2, column=3)
	self.check = Checkbutton(self.frameTwo, variable = self.Var7, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=3, column=3)
	self.check = Checkbutton(self.frameTwo, variable = self.Var8, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=4, column=3)
	
	self.check = Checkbutton(self.frameTwo, variable = self.Var9, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=5, column=3)
	self.check = Checkbutton(self.frameTwo, variable = self.Var10, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=6, column=3)
	self.check = Checkbutton(self.frameTwo, variable = Var11, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=7, column=3)
	self.check = Checkbutton(self.frameTwo, variable = Var12, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=8, column=3)
	
	self.check = Checkbutton(self.frameTwo, variable = Var13, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=9, column=3)
	self.check = Checkbutton(self.frameTwo, variable = Var14, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=10, column=3)
	self.check = Checkbutton(self.frameTwo, variable = Var15, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=11, column=3)
	self.check = Checkbutton(self.frameTwo, variable = Var16, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=12, column=3)
	
	self.check = Checkbutton(self.frameTwo, variable = Var17, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=13, column=3)
	self.check = Checkbutton(self.frameTwo, variable = Var18, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=14, column=3)
	self.check = Checkbutton(self.frameTwo, variable = Var19, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=15, column=3)
	self.check = Checkbutton(self.frameTwo, variable = Var20, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=16, column=3)
	self.check = Checkbutton(self.frameTwo, variable = Var21, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=17, column=3)
	self.check = Checkbutton(self.frameTwo, variable = Var22, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=18, column=3)
	self.check = Checkbutton(self.frameTwo, variable = Var23, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=19, column=3)
	self.check = Checkbutton(self.frameTwo, variable = Var24, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=20, column=3)
	
	self.check = Checkbutton(self.frameTwo, variable = Var25, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=21, column=3)
	self.check = Checkbutton(self.frameTwo, variable = Var26, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=22, column=3)
	self.check = Checkbutton(self.frameTwo, variable = Var27, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=23, column=3)
	self.check = Checkbutton(self.frameTwo, variable = Var28, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=24, column=3)
	
	self.check = Checkbutton(self.frameTwo, variable = Var29, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=25, column=3)
	self.check = Checkbutton(self.frameTwo, variable = Var30, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=26, column=3)
	self.check = Checkbutton(self.frameTwo, variable = Var31, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=27, column=3)
	self.check = Checkbutton(self.frameTwo, variable = Var32, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=28, column=3)
	
	self.check = Checkbutton(self.frameTwo, variable = Var33, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=29, column=3)
	self.check = Checkbutton(self.frameTwo, variable = Var34, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=30, column=3)
	self.check = Checkbutton(self.frameTwo, variable = Var35, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=31, column=3)


	
	self.textopieza = Label(self.frameTwo, text = "Minimo Numero de Estaciones", justify="left")
        self.textopieza.grid(row=1, column=4)
	self.textopieza = Label(self.frameTwo, text = "Maximo Numero de Estaciones", justify="left")
        self.textopieza.grid(row=2, column=4)
	self.textopieza = Label(self.frameTwo, text = "Latitud Minima", justify="left")
        self.textopieza.grid(row=3, column=4)
	self.textopieza = Label(self.frameTwo, text = "Latitud Maxima", justify="left")
        self.textopieza.grid(row=4, column=4)
	self.textopieza = Label(self.frameTwo, text = "Longitud Minima", justify="left")
        self.textopieza.grid(row=5, column=4)
	self.textopieza = Label(self.frameTwo, text = "Longitud Maxima", justify="left")
        self.textopieza.grid(row=6, column=4)
	self.textopieza = Label(self.frameTwo, text = "Magnitud Minima", justify="left")
        self.textopieza.grid(row=7, column=4)
	self.textopieza = Label(self.frameTwo, text = "Magnitud Maxima", justify="left")
        self.textopieza.grid(row=8, column=4)
	self.textopieza = Label(self.frameTwo, text = "Agencias Magnitiud", justify="left")
        self.textopieza.grid(row=9, column=4)
	self.textopieza = Label(self.frameTwo, text = "Agencias Localizacion", justify="left")
        self.textopieza.grid(row=10, column=4)
	self.textopieza = Label(self.frameTwo, text = "rms Minimo", justify="left")
        self.textopieza.grid(row=11, column=4)
	self.textopieza = Label(self.frameTwo, text = "rms Maximo", justify="left")
        self.textopieza.grid(row=12, column=4)
	self.textopieza = Label(self.frameTwo, text = "Profundidad Minima", justify="left")
        self.textopieza.grid(row=13, column=4)
	self.textopieza = Label(self.frameTwo, text = "Profundidad Maxima", justify="left")
        self.textopieza.grid(row=14, column=4)
	self.textopieza = Label(self.frameTwo, text = "Error en Latitud Minimo", justify="left")
        self.textopieza.grid(row=15, column=4)
	self.textopieza = Label(self.frameTwo, text = "Error en Latitud Maximo", justify="left")
        self.textopieza.grid(row=16, column=4)
	self.textopieza = Label(self.frameTwo, text = "Error en Longitud Minimo", justify="left")
        self.textopieza.grid(row=17, column=4)
	self.textopieza = Label(self.frameTwo, text = "Error en Longitud Maximo", justify="left")
        self.textopieza.grid(row=18, column=4)
	self.textopieza = Label(self.frameTwo, text = "Error en Profundidad Minimo", justify="left")
        self.textopieza.grid(row=19, column=4)
	self.textopieza = Label(self.frameTwo, text = "Error en Profundidad Maximo", justify="left")
        self.textopieza.grid(row=20, column=4)
	self.textopieza = Label(self.frameTwo, text = "Tipo de Magnitud", justify="left")
        self.textopieza.grid(row=21, column=4)
	self.textopieza = Label(self.frameTwo, text = "Distancia (ID)", justify="left")
        self.textopieza.grid(row=22, column=4)
	self.textopieza = Label(self.frameTwo, text = "Tipo de Evento", justify="left")
        self.textopieza.grid(row=23, column=4)
	self.textopieza = Label(self.frameTwo, text = "Minimo Numero de polaridades", justify="left")
        self.textopieza.grid(row=24, column=4)
	self.textopieza = Label(self.frameTwo, text = "Eventos Sentidos", justify="left")
        self.textopieza.grid(row=25, column=4)
	self.textopieza = Label(self.frameTwo, text = "Solucion Plano de Falla", justify="left")
        self.textopieza.grid(row=26, column=4)
	self.textopieza = Label(self.frameTwo, text = "", justify="left")
        self.textopieza.grid(row=27, column=4)
	self.textopieza = Label(self.frameTwo, text = "", justify="left")
        self.textopieza.grid(row=28, column=4)
	self.textopieza = Label(self.frameTwo, text = "Gap Minimo", justify="left")
        self.textopieza.grid(row=29, column=4)
	self.textopieza = Label(self.frameTwo, text = "Gap Maximo", justify="left")
        self.textopieza.grid(row=30, column=4)
	self.textopieza = Label(self.frameTwo, text = "Numero de Fases?", justify="left")
        self.textopieza.grid(row=31, column=4)
	




	#self.E1 = Entry(self.frameTwo,width=14,textvariable=v1)
        #self.E1.grid(row=1, column=2, padx=(0,10))

	v1 = StringVar(self.frameTwo)
	v1.set('OPERA')
	v2 = StringVar(self.frameTwo)
	v2.set('CAT')
	v13 = StringVar(self.frameTwo)
	v13.set('BDRSN')
	v14 = StringVar(self.frameTwo)
	v14.set('BDRSN')
	v25 = StringVar(self.frameTwo)
	v25.set('Ml')
	v26 = StringVar(self.frameTwo)
	v26.set('L')
	v27 = StringVar(self.frameTwo)
	v27.set('E')
	
	
	self.O1 = OptionMenu(self.frameTwo,v1,'OPERA','SSMLG','BDRSNC')
	self.O1.grid(row=14, column=2, padx=(0,10))
	self.O2 = OptionMenu(self.frameTwo,v2,'CAT','SFILES')
	self.O2.grid(row=15, column=2, padx=(0,10))
	
	self.E3 = Entry(self.frameTwo,width=14,textvariable=self.v3)
        self.E3.grid(row=16, column=2, padx=(0,10))
	self.E4 = Entry(self.frameTwo,width=14,textvariable=self.v4)
        self.E4.grid(row=17, column=2, padx=(0,10))

	
	self.E5 = Entry(self.frameTwo,width=14,textvariable=v5)
        self.E5.grid(row=1, column=5, padx=(0,10))
	self.E6 = Entry(self.frameTwo,width=14,textvariable=v6)
        self.E6.grid(row=2, column=5, padx=(0,10))
	self.E7 = Entry(self.frameTwo,width=14,textvariable=self.v7)
        self.E7.grid(row=3, column=5, padx=(0,10))
	self.E8 = Entry(self.frameTwo,width=14,textvariable=self.v8)
        self.E8.grid(row=4, column=5, padx=(0,10))
	self.E9 = Entry(self.frameTwo,width=14,textvariable=self.v9)
        self.E9.grid(row=5, column=5, padx=(0,10))
	self.E10 = Entry(self.frameTwo,width=14,textvariable=self.v10)
        self.E10.grid(row=6, column=5, padx=(0,10))
	self.E11 = Entry(self.frameTwo,width=14,textvariable=v11)
        self.E11.grid(row=7, column=5, padx=(0,10))
	self.E12 = Entry(self.frameTwo,width=14,textvariable=v12)
        self.E12.grid(row=8, column=5, padx=(0,10))
	
	self.O3 = OptionMenu(self.frameTwo,v13,'RSNC','NEIC','FUNVISIS','IGEPN','EMSC')
	self.O3.grid(row=9, column=5, padx=(0,10))
	self.O4 = OptionMenu(self.frameTwo,v14,'RSNC','NEIC','FUNVISIS','IGEPN','EMSC')
	self.O4.grid(row=10, column=5, padx=(0,10))
	
	self.E15 = Entry(self.frameTwo,width=14,textvariable=v15)
        self.E15.grid(row=11, column=5, padx=(0,10))
	self.E16 = Entry(self.frameTwo,width=14,textvariable=v16)
        self.E16.grid(row=12, column=5, padx=(0,10))
	self.E17 = Entry(self.frameTwo,width=14,textvariable=v17)
        self.E17.grid(row=13, column=5, padx=(0,10))
	self.E18 = Entry(self.frameTwo,width=14,textvariable=v18)
        self.E18.grid(row=14, column=5, padx=(0,10))
	self.E19 = Entry(self.frameTwo,width=14,textvariable=v19)
        self.E19.grid(row=15, column=5, padx=(0,10))
	self.E20 = Entry(self.frameTwo,width=14,textvariable=v20)
        self.E20.grid(row=16, column=5, padx=(0,10))
	self.E21 = Entry(self.frameTwo,width=14,textvariable=v21)
        self.E21.grid(row=17, column=5, padx=(0,10))
	self.E22 = Entry(self.frameTwo,width=14,textvariable=v22)
        self.E22.grid(row=18, column=5, padx=(0,10))
	self.E23 = Entry(self.frameTwo,width=14,textvariable=v23)
        self.E23.grid(row=19, column=5, padx=(0,10))
	self.E24 = Entry(self.frameTwo,width=14,textvariable=v24)
        self.E24.grid(row=20, column=5, padx=(0,10))
	
	self.O5 = OptionMenu(self.frameTwo,v25,'Ml','Mw','Mb')
	self.O5.grid(row=21, column=5, padx=(0,10))
	self.O6 = OptionMenu(self.frameTwo,v26,'L','R','D')
	self.O6.grid(row=22, column=5, padx=(0,10))
	self.O7 = OptionMenu(self.frameTwo,v27,'E','V','P')
	self.O7.grid(row=23, column=5, padx=(0,10))
	
	self.E28 = Entry(self.frameTwo,width=14,textvariable=v28)
        self.E28.grid(row=24, column=5, padx=(0,10))
	self.E29 = Entry(self.frameTwo,width=14,textvariable=v29)
        self.E29.grid(row=25, column=5, padx=(0,10))
	self.E30 = Entry(self.frameTwo,width=14,textvariable=v30)
        self.E30.grid(row=26, column=5, padx=(0,10))
	self.E31 = Entry(self.frameTwo,width=14,textvariable=v31)
        self.E31.grid(row=27, column=5, padx=(0,10))
	self.E32 = Entry(self.frameTwo,width=14,textvariable=v32)
        self.E32.grid(row=28, column=5, padx=(0,10))
	self.E33 = Entry(self.frameTwo,width=14,textvariable=v33)
        self.E33.grid(row=29, column=5, padx=(0,10))
	self.E34 = Entry(self.frameTwo,width=14,textvariable=v34)
        self.E34.grid(row=30, column=5, padx=(0,10))
	self.E35 = Entry(self.frameTwo,width=14,textvariable=v35)
        self.E35.grid(row=31, column=5, padx=(0,10))
	
	#self.mostrar=Button(self.frameTwo, text='Mostrar', command=var_states)
	#self.mostrar.grid(row=32, column=2, padx=(0,10))
	#self.mainloop()
	
	
	#print v1.get()
	#print v2.get()
	#print v3.get()
	#print v4.get()

################################Modificar Select.inp#################################
	
	def modificar():
		parametros=glob("/home/camilo/read_select/codigo/select.inp")
		#parametros=glob("/home/Cmunoz/read_select/codigo/select.inp")
		archivo=open(parametros[0],"r")
		print "Nombre del archivo : ", archivo.name
		#print "Cerrado o no : ", archivo.closed
		#print "Modo de apertura : ", archivo.mode
		lines=archivo.readlines()
		#print (lines[0])
		contenido = ''
		
		for line in lines:
			if 'Base or file name' in line:
				if Var1.get() == 1:
					#base_datos=raw_input('Base de datos?    ')
					print v1.get()
					contenido +=  ' Base or file name            : '+v1.get()+'\n'
				else:
					contenido += line
			elif 'Base type' in line:
				if Var2.get() == 1:
					#tipo=raw_input('Tipo?    ')
					print v2.get()
					contenido +=  ' Base type                    : '+v2.get()+'\n'
				else:
					contenido += line
			elif 'Start time' in line:
				if self.Var3.get() == 1:
					#t_ini=raw_input('Tiempo Inicial?    ')
					print self.v3.get()
					contenido +=  ' Start time                   : '+self.v3.get()+'\n'
				else:
					contenido += line
			elif 'End time' in line:
				if Var4.get() == 1:
					#t_end=raw_input('Tiempo Final?    ')
					print self.v4.get()
					contenido +=  ' End time                     : '+self.v4.get()+'\n'
				else:
					contenido += line
	
	
			elif 'Minimum number of stations' in line:
				if Var5.get() == 1:
					#base_datos=raw_input('Base de datos?    ')
					print v5.get()
					contenido +=  ' Minimum number of stations   :              '+v5.get()+'\n'
				else:
					contenido += line
			elif 'Maximum number of stations' in line:
				if Var6.get() == 1:
					#t_end=raw_input('Tiempo Final?    ')
					print v6.get()
					contenido +=  ' Maximum number of stations   :            '+v6.get()+'\n'
				else:
					contenido += line
			elif 'Minimum latitude' in line:
				if self.Var7.get() == 1:
					#t_end=raw_input('Tiempo Final?    ')
					print self.v7.get()
					contenido +=  ' Minimum latitude             :        '+self.v7.get()+'\n'
				else:
					contenido += line
			elif 'Maximum latitude' in line:
				if self.Var8.get() == 1:
					#t_end=raw_input('Tiempo Final?    ')
					print self.v8.get()
					contenido +=  ' Maximum latitude             :         '+self.v8.get()+'\n'
				else:
					contenido += line
			elif 'Minimum longitude' in line:
				if self.Var9.get() == 1:
					#t_end=raw_input('Tiempo Final?    ')
					print self.v9.get()
					contenido +=  ' Minimum longitude            :       '+self.v9.get()+'\n'
				else:
					contenido += line
			elif 'Maximum longitude' in line:
				if self.Var10.get() == 1:
					#t_end=raw_input('Tiempo Final?    ')
					print self.v10.get()
					contenido +=  ' Maximum longitude            :        '+self.v10.get()+'\n'
				else:
					contenido += line
			elif 'Minimum magnitude' in line:
				if Var11.get() == 1:
					#t_end=raw_input('Tiempo Final?    ')
					print v11.get()
					contenido +=  ' Minimum magnitude            :       '+v11.get()+'\n'
				else:
					contenido += line
			elif 'Maximum magnitude' in line:
				if Var12.get() == 1:
					#t_end=raw_input('Tiempo Final?    ')
					print v12.get()
					contenido +=  ' Maximum magnitude            :        '+v12.get()+'\n'
				else:
					contenido += line
			elif 'Magnitude agencies' in line:
				if Var13.get() == 1:
					#t_end=raw_input('Tiempo Final?    ')
					print v13.get()
					contenido +=  ' Magnitude agencies           :                               '+v13.get()+'\n'
				else:
					contenido += line
			elif 'Hypocenter agencies' in line:
				if Var14.get() == 1:
					#t_end=raw_input('Tiempo Final?    ')
					print v14.get()
					contenido +=  ' Hypocenter agencies          :                               '+v14.get()+'\n'
				else:
					contenido += line
			elif 'Minimum rms' in line:
				if Var15.get() == 1:
					#t_end=raw_input('Tiempo Final?    ')
					print v15.get()
					contenido +=  ' Minimum rms                  :          '+v15.get()+'\n'
				else:
					contenido += line
			
			elif 'Maximum rms' in line:
				if Var16.get() == 1:
					#t_end=raw_input('Tiempo Final?    ')
					print v16.get()
					contenido +=  ' Maximum rms                  :        '+v16.get()+'\n'
				else:
					contenido += line
			elif 'Minimum depth' in line:
				if Var17.get() == 1:
					#t_end=raw_input('Tiempo Final?    ')
					print v17.get()
					contenido +=  ' Minimum depth                :        '+v17.get()+'\n'
				else:
					contenido += line
			
			elif 'Maximum depth' in line:
				if Var18.get() == 1:
					#t_end=raw_input('Tiempo Final?    ')
					print v18.get()
					contenido +=  ' Maximum depth                :      '+v18.get()+'\n'
				else:
					contenido += line
			elif 'Minimum error in latitude' in line:
				if Var19.get() == 1:
					#t_end=raw_input('Tiempo Final?    ')
					print v19.get()
					contenido +=  ' Minimum error in latitude    :          '+v19.get()+'\n'
				else:
					contenido += line
			elif 'Maximum error in latitude' in line:
				if Var20.get() == 1:
					#t_end=raw_input('Tiempo Final?    ')
					print v20.get()
					contenido +=  ' Maximum error in latitude    :      '+v20.get()+'\n'
				else:
					contenido += line
			elif 'Minimum error in longitude' in line:
				if Var21.get() == 1:
					#t_end=raw_input('Tiempo Final?    ')
					print v21.get()
					contenido +=  ' Minimum error in longitude   :          '+v21.get()+'\n'
				else:
					contenido += line
			elif 'Maximum error in longitude' in line:
				if Var22.get() == 1:
					#t_end=raw_input('Tiempo Final?    ')
					print v22.get()
					contenido +=  ' Maximum error in longitude   :      '+v22.get()+'\n'
				else:
					contenido += line
			elif 'Minimum error in depth' in line:
				if Var23.get() == 1:
					#t_end=raw_input('Tiempo Final?    ')
					print v23.get()
					contenido +=  ' Minimum error in depth       :        '+v23.get()+'\n'
				else:
					contenido += line
			elif 'Maximum error in depth' in line:
				if Var24.get() == 1:
					#t_end=raw_input('Tiempo Final?    ')
					print v24.get()
					contenido +=  ' Maximum error in depth       :      '+v24.get()+'\n'
				else:
					contenido += line
			elif 'Magnitude types (L,C,B,S,W)' in line:
				if Var25.get() == 1:
					#t_end=raw_input('Tiempo Final?    ')
					print v25.get()
					contenido +=  ' Magnitude types (L,C,B,S,W)  :      '+v25.get()+'\n'
				else:
					contenido += line
			elif 'Distance (ID) types (L,R,D)' in line:
				if Var26.get() == 1:
					#t_end=raw_input('Tiempo Final?    ')
					print v26.get()
					contenido +=  ' Distance (ID) types (L,R,D)  :      '+v26.get()+'\n'
				else:
					contenido += line
			elif 'Event types (e.g. E,V,P)' in line:
				if Var27.get() == 1:
					#t_end=raw_input('Tiempo Final?    ')
					print v27.get()
					contenido +=  ' Event types (e.g. E,V,P)     :      '+v27.get()+'\n'
				else:
					contenido += line
			elif 'Minimum number of polarities' in line:
				if Var28.get() == 1:
					#t_end=raw_input('Tiempo Final?    ')
					print v28.get()
					contenido +=  ' Minimum number of polarities :              '+v28.get()+'\n'
				else:
					contenido += line
			elif 'Felt earthquakes' in line:
				if Var29.get() == 1:
					#t_end=raw_input('Tiempo Final?    ')
					print v29.get()
					contenido +=  ' Felt earthquakes             :              '+v29.get()+'\n'
				else:
					contenido += line
			
			elif 'Fault plane solution' in line:
				if Var30.get() == 1:
					#t_end=raw_input('Tiempo Final?    ')
					print v30.get()
					contenido +=  ' Fault plane solution         :        '+v30.get()+'\n'
				else:
					contenido += line
			elif 'Check all header lines' in line:
				if Var31.get() == 1:
					#t_end=raw_input('Tiempo Final?    ')
					print v31.get()
					contenido +=  ' Check all header lines       :              '+v31.get()+'\n'
				else:
					contenido += line
			elif 'Waveform files to check' in line:
				if Var32.get() == 1:
					#t_end=raw_input('Tiempo Final?    ')
					print v32.get()
					contenido +=  ' Waveform files to check      :                                         '+v32.get()+'\n'
				else:
					contenido += line
			elif 'Minimum gap' in line:
				if Var33.get() == 1:
					#t_end=raw_input('Tiempo Final?    ')
					print v33.get()
					contenido +=  ' Minimum gap                  :          '+v33.get()+'\n'
				else:
					contenido += line
			elif 'Maximum gap' in line:
				if Var34.get() == 1:
					#t_end=raw_input('Tiempo Final?    ')
					print v34.get()
					contenido +=  ' Maximum gap                  :        '+v34.get()+'\n'
				else:
					contenido += line
			elif 'Phases' in line:
				if Var35.get() == 1:
					#t_end=raw_input('Tiempo Final?    ')
					print v35.get()
					contenido +=  ' Phases                       :                         '+v35.get()+'\n'
				else:
					contenido += line
			else:
				contenido += line	
	
		archivo.close()
		archivo=open(parametros[0],"w")
		archivo.write(contenido)
		archivo.close()

	#os.system("/home/Cmunoz/read_select/mapas/mapa1/./mapa")

	
	self.menu=Button(self.frameTwo, text='Menu', command=self.menu_inicial)
	self.menu.grid(row=32, column=4, padx=(0,10))

	self.mostrar=Button(self.frameTwo, text='Cargar Datos', command=modificar)
	self.mostrar.grid(row=32, column=1, padx=(0,10))
	
	self.mostrar1=Button(self.frameTwo, text='Mostrar Cofiguracion', command=inp)
	self.mostrar1.grid(row=32, column=3, padx=(0,10))
	
	self.mostrar2=Button(self.frameTwo, text='Select', command=select)
	self.mostrar2.grid(row=32, column=2, padx=(0,10))

	self.salir=Button(self.frameTwo, text='Salir', command=self.quit)
	self.salir.grid(row=32, column=5, padx=(0,10))
	#self.mainloop()

####################################################################################
################################MAPAS################################################
#####################################################################################


	
    def ir_mapas(self):
	self.frameOne.destroy()
	self.frameThree=Toplevel()
		

	#########seigmt###################

	os.system("./expect_seigmt")
	
	######Variables Mapas############
	
	v36 = StringVar()
	v37 = StringVar()
	v48 = StringVar()
	v50 = StringVar()
	v51 = StringVar()


	v36 = StringVar(self.frameThree)
	v36.set('bati.grd')

	v37 = StringVar(self.frameThree)
	v37.set('bati2.cpt')

	v47 = StringVar(self.frameThree)
	v47.set('.pdf')

	v49 = StringVar(self.frameThree)
	v49.set('a4')

	

	Var36 = IntVar()
	Var37 = IntVar()
	Var38 = IntVar()
	Var38_1 = IntVar()
	Var38_2 = IntVar()
	Var39 = IntVar()
	Var40 = IntVar()
	Var41 = IntVar()
	Var41_2 = IntVar()
	Var41_3 = IntVar()
	Var42 = IntVar()
	Var43 = IntVar()
	Var44 = IntVar()
	Var45 = IntVar()
	Var46 = IntVar()
	Var47 = IntVar()
	Var48 = IntVar()
	Var49 = IntVar()
	Var50 = IntVar()
	Var51 = IntVar()
	

	lat_min = IntVar()

	if self.Var7.get() == 1:
		lat_min=float(self.v7.get())
		lat_min2=lat_min-1
		lat_min3=lat_min-4
		#print lat_min2
		lat_min2str=str(lat_min2)
		lat_min3str=str(lat_min3)
	if self.Var8.get() == 1:
		lat_max=float(self.v8.get())
		lat_max2=lat_max-2
		#print lat_max2
	if self.Var9.get() == 1:
		lon_min=float(self.v9.get())
		lon_min2=lon_min-2
		#print lon_min2
	if self.Var10.get() == 1:
		lon_max=float(self.v10.get())
		lon_max2=lon_max-2
		#print lon_max2

		
	
	
	######################## MENU ELEGIBLE#######################################
	
	self.texto = Label(self.frameThree, height='3', text = "Mapas", justify="center")
        self.texto.grid(row=0, column=2)

	
	
	
	self.check = Checkbutton(self.frameThree, variable=Var36, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=1, column=1)
	self.check = Checkbutton(self.frameThree, variable=Var37, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=2, column=1)
	self.check = Checkbutton(self.frameThree, variable=Var38, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=3, column=1)
	self.check = Checkbutton(self.frameThree, variable=Var38_1, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=4, column=1)
	self.check = Checkbutton(self.frameThree, variable=Var38_2, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=5, column=1)
	self.check = Checkbutton(self.frameThree, variable=Var39, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=6, column=1)
	self.check = Checkbutton(self.frameThree, variable=Var40, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=7, column=1)
	self.check = Checkbutton(self.frameThree, variable=Var41, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=8, column=1)
	self.check = Checkbutton(self.frameThree, variable=Var41_2, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=8, column=3)
	self.check = Checkbutton(self.frameThree, variable=Var41_3, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=8, column=5)

	self.check = Checkbutton(self.frameThree, variable=Var42, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=9, column=1)
	self.check = Checkbutton(self.frameThree, variable=Var43, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=10, column=1)
	self.check = Checkbutton(self.frameThree, variable=Var44, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=11, column=1)
	self.check = Checkbutton(self.frameThree, variable=Var45, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=12, column=1)
	self.check = Checkbutton(self.frameThree, variable=Var46, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=13, column=1)
	
	self.check = Checkbutton(self.frameThree, variable=Var48, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=14, column=3)
	self.check = Checkbutton(self.frameThree, variable=Var49, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=16, column=3)
	self.check = Checkbutton(self.frameThree, variable=Var50, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=18, column=3)
	



	self.check = Checkbutton(self.frameThree, variable=Var47, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=22, column=1)




	
	self.textopieza = Label(self.frameThree, text = "Topografia", justify="left")
        self.textopieza.grid(row=1, column=2)
	self.textopieza = Label(self.frameThree, text = "Colores Topografia", justify="left")
        self.textopieza.grid(row=2, column=2)
	self.textopieza = Label(self.frameThree, text = "Divisiones", justify="left")
        self.textopieza.grid(row=3, column=2)
	self.textopieza = Label(self.frameThree, text = "Rosa de los Vientos", justify="left")
        self.textopieza.grid(row=4, column=2)
	self.textopieza = Label(self.frameThree, text = "Escala", justify="left")
        self.textopieza.grid(row=5, column=2)
	self.textopieza = Label(self.frameThree, text = "Sismos", justify="left")
        self.textopieza.grid(row=6, column=2)
	self.textopieza = Label(self.frameThree, text = "Nombre Estaciones", justify="left")
        self.textopieza.grid(row=7, column=2)
	self.textopieza = Label(self.frameThree, text = "Icono Estaciones", justify="left")
	self.textopieza.grid(row=8, column=2)

	self.textopieza = Label(self.frameThree, text = "Antena", justify="left")
	self.textopieza.grid(row=8, column=4)
	self.textopieza = Label(self.frameThree, text = "Leyenda Estaciones", justify="left")
	self.textopieza.grid(row=8, column=6)

	self.textopieza = Label(self.frameThree, text = "Icono capitales", justify="left")
        self.textopieza.grid(row=9, column=2)
	self.textopieza = Label(self.frameThree, text = "Nombre Capitales", justify="left")
        self.textopieza.grid(row=10, column=2)
	self.textopieza = Label(self.frameThree, text = "Leyenda Profundidad", justify="left")
        self.textopieza.grid(row=11, column=2)
	self.textopieza = Label(self.frameThree, text = "Leyenda Magnitud", justify="left")
        self.textopieza.grid(row=12, column=2)
	self.textopieza = Label(self.frameThree, text = "Hacer Zoom en la Region del Select", justify="left")
	self.textopieza.grid(row=13, column=2)


	self.textopieza = Label(self.frameThree, text = "Modificar Tamano Mapa ", justify="left")
	self.textopieza.grid(row=14, column=4)

	self.ayuda1 = Label(self.frameThree, text = "Ayuda", justify="left")
	self.ayuda1.grid(row=14, column=6)
	
	self.textopieza = Label(self.frameThree, text = "", justify="left")
	self.textopieza.grid(row=15, column=4)

	self.textopieza = Label(self.frameThree, text = "Modificar Tamano Hoja", justify="left")
	self.textopieza.grid(row=16, column=4)

	self.ayuda2 = Label(self.frameThree, text = "Ayuda", justify="left")
	self.ayuda2.grid(row=16, column=6)
	
	self.textopieza = Label(self.frameThree, text = "", justify="left")
	self.textopieza.grid(row=17, column=4)


	self.textopieza = Label(self.frameThree, text = "Valor Proyeccion para el Titulo", justify="left")
	self.textopieza.grid(row=18, column=4)
	
	self.ayuda3 = Label(self.frameThree, text = "Ayuda", justify="left")
	self.ayuda3.grid(row=18, column=6)

	self.textopieza = Label(self.frameThree, text = "", justify="left")
	self.textopieza.grid(row=19, column=4)


	self.textopieza = Label(self.frameThree, text = "Posicion Titulo", justify="left")
	self.textopieza.grid(row=21, column=4)
	
	self.ayuda4 = Label(self.frameThree, text = "Ayuda", justify="left")
	self.ayuda4.grid(row=21, column=6)
	
	
	
	
        
	self.textopieza = Label(self.frameThree, text = "Exportar como", justify="left")
        self.textopieza.grid(row=22, column=2)


	


	self.O5 = OptionMenu(self.frameThree,v36,'bati.grd','Col250m_bat30s.grd','col.grd','gridOne09.grd','NE.grd','NW.grd','SE.grd','SW.grd')
	self.O5.grid(row=1, column=3, padx=(0,20))
	self.O6 = OptionMenu(self.frameThree,v37,'bati.cpt','bati2.cpt','bw.cpt','colores.cpt','gebco_c.cpt','topo.cpt')
	self.O6.grid(row=2, column=3, padx=(0,20))

	self.O6 = OptionMenu(self.frameThree,v47,'.ps','.pdf','.jpg')
	self.O6.grid(row=22, column=3, padx=(0,20))

	self.O7 = OptionMenu(self.frameThree,v49,'a4','a5','a6','a3','a2','a1','a7','a8')
	self.O7.grid(row=16, column=5, padx=(0,20))



	self.E36 = Entry(self.frameThree,width=14,textvariable=v48)
        self.E36.grid(row=14, column=5, padx=(0,10))
	self.E37 = Entry(self.frameThree,width=14,textvariable=v50)
        self.E37.grid(row=18, column=5, padx=(0,10))
	self.E38 = Entry(self.frameThree,width=14,textvariable=v51)
        self.E38.grid(row=21, column=5, padx=(0,10))

	       
   
	def showMenu1(e):
		menu1.post(e.x_root, e.y_root)
	def showMenu2(e):
		menu2.post(e.x_root, e.y_root)
	def showMenu3(e):
		menu3.post(e.x_root, e.y_root)
	def showMenu4(e):
		menu4.post(e.x_root, e.y_root)

	

	menu4 = Menu(self.frameThree, tearoff=0)
	menu4.add_command(label="Este valor corresponde a la proyeccion Jm del mapa,")
	menu4.add_command(label="poner valores cercanos a 0.5 para mapas grandes y")
	menu4.add_command(label="cercanos a 1.5 para mapas pequenos.")
	
	menu3 = Menu(self.frameThree, tearoff=0)
	menu3.add_command(label="a4, a5 y a6 para mapas medianos")
	menu3.add_command(label="a3, a2 y a1 para mapas grandes")
	menu3.add_command(label="a7 y a8 para mapas pequenos.")
	
	menu2 = Menu(self.frameThree, tearoff=0)
	menu2.add_command(label="Este valor corresponde a la proyeccion Jx del titulo,")
	menu2.add_command(label="poner valores entre 0.2 para mapas pequenos hasta")
	menu2.add_command(label="0.5 para mapas grandes.")

	menu1 = Menu(self.frameThree, tearoff=0)
	menu1.add_command(label="En caso de que el titulo se mueva a la izquierda")
	menu1.add_command(label="modificar este valor entre 12 y 20, donde 20 es ")
	menu1.add_command(label="es el mayor valor a la derecha y 12 a la izquierda.")
	
	
	self.ayuda1.bind("<Enter>", showMenu4)
	self.ayuda2.bind("<Enter>", showMenu3)
	self.ayuda3.bind("<Enter>", showMenu2)
	self.ayuda4.bind("<Enter>", showMenu1)
	#self.E38.bind("<Leave>", dellMenu1)

	

	#############################Funciones#######################################
	def mapa():
	   os.system("/home/camilo/read_select/codigo/./mapa")
	   #os.system("/home/Cmunoz/read_select/codigo/./mapa")

	def ps():
	   os.system("display mapa.ps")
	def pdf():
	   os.system("kpdf mapa.pdf")
        def jpg():
	   os.system("display mapa.jpg")
	def conf():
	   os.system("gedit /home/camilo/read_select/codigo/mapa")
	
	######################### Modificar Codigo Mapa################################
	def modificar2():
		parametros2=glob("/home/camilo/read_select/codigo/mapa")
		archivo2=open(parametros2[0],"r")
		print "Nombre del archivo : ", archivo2.name
		#print "Cerrado o no : ", archivo2.closed
		#print "Modo de apertura : ", archivo2.mode
		lines=archivo2.readlines()
		#print (lines[0])
		contenido2 = ''

		if v36.get() == 'bati.grd':
			v36_1 = 'bati.ilu'
		elif v36.get() == 'Col250m_bat30s.grd':
			v36_1 = 'Col250m_bat30s_int.grd'
		elif v36.get() == 'col.grd':
			v36_1 = 'col.ilu'
		elif v36.get() == 'gridOne09.grd':
			v36_1 = 'gridone09_int.grd'
		elif v36.get() == 'NE.grd':
			v36_1 = 'NE.ilu'
		elif v36.get() == 'NW.grd':
			v36_1 = 'NW.ilu'
		elif v36.get() == 'SE.grd':
			v36_1 = 'SE.ilu'
		elif v36.get() == 'SW.grd':
			v36_1 = 'SW.ilu'

		if self.Var7.get() == 1:#check latitud minima
			v7_2=float(self.v7.get())+2
			v8_2=float(self.v8.get())+2
			v9_2=float(self.v9.get())+2
			v10_2=float(self.v10.get())+2
			v7_2str=str(v7_2)
			v8_2str=str(v8_2)
			v9_2str=str(v9_2)
			v10_2str=str(v10_2)
		
		
		for line in lines:

			if 'SISMICIDAD REGISTRADA' in line:
				if self.Var3.get() == 1:
					if Var46.get() == 1:#check zoom
						if Var50.get() == 1:#check modificar Jx
							if Var50.get() == 1:#check proyeccion titulo titulo
								contenido2 +='echo 4.7 50 12 0 3 CM SISMICIDAD REGISTRADA DEL '+self.v3.get()+' AL '+self.v4.get()+' | pstext -R-'+v51.get()+'/40/0/60 -Jx'+v50.get()+' -G0 -P -K  >! mapa.ps\n'
							else:
								contenido2 +='echo 4.7 50 12 0 3 CM SISMICIDAD REGISTRADA DEL '+self.v3.get()+' AL '+self.v4.get()+' | pstext -R-12/40/0/60 -Jx'+v50.get()+' -G0 -P -K  >! mapa.ps\n'
						else:
							contenido2 +='echo 4.7 50 12 0 3 CM SISMICIDAD REGISTRADA DEL '+self.v3.get()+' AL '+self.v4.get()+' | pstext -R-12/40/0/60 -Jx0.5 -G0 -P -K  >! mapa.ps\n'
					else:
						contenido2 +='echo 4.7 50 12 0 3 CM SISMICIDAD REGISTRADA DEL '+self.v3.get()+' AL '+self.v4.get()+' | pstext -R-12/40/0/60 -Jx0.5 -G0 -P -K  >! mapa.ps\n'
				else:
					contenido2 += line


			elif 'grdimage1' in line:
				if Var36.get() == 1:#check topografia
					if self.Var7.get() == 1:#check latitud minima
						if Var46.get() == 1:#check zoom
							if Var48.get() == 1:#check modificar jm
								contenido2 +='grdimage /home/topo/'+v36.get()+' -I/home/topo/'+v36_1+' -C/home/topo/'+v37.get()+' -R'+self.v9.get()+'/'+self.v10.get()+'/'+self.v7.get()+'/'+self.v8.get()+' -Ba2f2 -Jm'+v48.get()+'i -K -O -P -y5 -x0  >> mapa.ps #grdimage1 \n'
							else:
								contenido2 +='grdimage /home/topo/'+v36.get()+' -I/home/topo/'+v36_1+' -C/home/topo/'+v37.get()+' -R'+self.v9.get()+'/'+self.v10.get()+'/'+self.v7.get()+'/'+self.v8.get()+' -Ba2f2 -Jm1.2i -K -O -P -y5 -x0  >> mapa.ps #grdimage1 \n'
						else:
							contenido2 +='grdimage /home/topo/'+v36.get()+' -I/home/topo/'+v36_1+' -C/home/topo/'+v37.get()+' -R-82/-66.7/-4.3/14 -Ba2f2 -Jm0.4i -K -O -P -y5 -x0  >> mapa.ps #grdimage1 \n'			
					else:
						contenido2 +='grdimage /home/topo/'+v36.get()+' -I/home/topo/'+v36_1+' -C/home/topo/'+v37.get()+' -R-82/-66.7/-4.3/14 -Ba2f2 -Jm0.4i -K -O -P -y5 -x0  >> mapa.ps #grdimage1 \n'
				elif self.Var7.get() == 1: #check latitud minima
					if Var46.get() == 1: #check zoom
						if Var48.get() == 1:#check modificar jm
							contenido2 +='grdimage /home/topo/ -I/home/topo/bati.ilu -C/home/topo/bati2.cpt -R'+self.v9.get()+'/'+self.v10.get()+'/'+self.v7.get()+'/'+self.v8.get()+' -Ba2f2 -Jm'+v48.get()+'i -K -O -P -y5 -x0  >> mapa.ps #grdimage1 \n'
						else:
							contenido2 +='grdimage /home/topo/ -I/home/topo/bati.ilu -C/home/topo/bati2.cpt -R'+self.v9.get()+'/'+self.v10.get()+'/'+self.v7.get()+'/'+self.v8.get()+' -Ba2f2 -Jm1.2i -K -O -P -y5 -x0  >> mapa.ps #grdimage1 \n'
				else:
					contenido2 += 'grdimage /home/topo/ -I/home/topo/col.ilu -C/home/topo/bati2.cpt -R-82/-66.7/-4.3/14 -Ba2f2 -Jm0.40i -K -O -P -y5 -x0  >> mapa.ps #grdimage1 \n'
								

							

			elif 'pscoast1' in line:
				if Var38.get() == 1:
					if Var38_1.get() == 1:
						if Var38_2.get() == 1:
							contenido2 +='pscoast -R -Jm -W0.4p/200 -Df -Lf-68/-5.3/4/200 -Tf-68.5/-2/1.5/1.5 -Ba2f2 -N1/0.4p -N2/0.3p -O -P  -K >>mapa.ps #pscoast1 \n'
						else:
							contenido2 +='pscoast -R -Jm -W0.4p/200 -Df -Tf-68.5/-2/1.5/1.5 -Ba2f2 -N1/0.4p -N2/0.3p -O -P  -K >>mapa.ps #pscoast1 \n'
					elif  Var38_2.get() == 1:
						contenido2 +='pscoast -R -Jm -W0.4p/200 -Df -Lf-68/-5.3/4/200 -Ba2f2 -N1/0.4p -N2/0.3p -O -P  -K >>mapa.ps #pscoast1 \n'
					else:
						contenido2 +='pscoast -R -Jm -W0.4p/200 -Df  -Ba2f2 -N1/0.4p -N2/0.3p -O -P  -K >>mapa.ps #pscoast1 \n'
				elif Var38_1.get() == 1:
					if Var38_2.get() == 1:
						contenido2 +='pscoast -R -Jm -W0.4p/200 -Df -Lf-68/-5.3/4/200 -Tf-68.5/-2/1.5/1.5 -Ba2f2 -O -P  -K >>mapa.ps #pscoast1 \n'
					else:
						contenido2 +='pscoast -R -Jm -W0.4p/200 -Df -Tf-68.5/-2/1.5/1.5 -Ba2f2 -O -P  -K >>mapa.ps #pscoast1 \n'
				else:
					if Var38_2.get() == 1:
						contenido2 +='pscoast -R -Jm -W0.4p/200 -Df -Lf-68/-5.3/4/200 -Ba2f2 -O -P  -K >>mapa.ps #pscoast1 \n'
					else:
						contenido2 +='pscoast -R -Jm -W0.4p/200 -Df -Ba2f2 -O -P  -K >>mapa.ps #pscoast1 \n'
						


			
			elif 'Cpaletteluisa.cpt' in line:
				if Var39.get() == 1:
					contenido2 +='psxy -R -Jm -O -K -Cpaletteluisa.cpt gmtxyz.out -Sci -W0.05 >> mapa.ps\n'
				else:
					contenido2 += '#psxy -R -Jm -O -K -Cpaletteluisa.cpt gmtxyz.out -Sci -W0.05 >> mapa.ps\n'
			
			elif 'nombres.txt' in line:
				if Var40.get() == 1: #Check nombre estaciones
					if Var41.get() == 1: #Check icono estaciones
						contenido2 +='pstext nombres.txt -R -Jm -O -G0 -K -y0.2 -x0.2 >> mapa.ps\n'
					else:
						contenido2 +='pstext nombres.txt -R -Jm -O -G0 -K >> mapa.ps\n'	
				else:
					contenido2 += '#pstext nombres.txt -R -Jm -O -G0 -K >> mapa.ps\n'


			elif 'icono_estaciones' in line:
				if Var41.get() == 1: #Check icono estaciones
					if Var41_2.get() == 1: # Check Antena
						if Var40.get() == 1: #Check nombre estaciones
							contenido2 += 'psxy stations_rsnc_all.d -O -R -Jm -K -Cpalettestations.cpt -Skantena/0.15i -W0/0/0 -K -y-0.2 -x-0.2 >>mapa.ps #icono_estaciones \n'
						else:
							contenido2 += 'psxy stations_rsnc_all.d -O -R -Jm -K -Cpalettestations.cpt -Skantena/0.15i -W0/0/0 -K >>mapa.ps #icono_estaciones \n'
					elif  Var40.get() == 1: #Check nombre
						contenido2 += 'psxy -R -Jm -O -K formas.d -St0.2 -G255/255/255 -W1 -y-0.2 -x-0.2 >> mapa.ps #icono_estaciones \n'
					else:
						contenido2 += 'psxy -R -Jm -O -K formas.d -St0.2 -G255/255/255 -W1  >> mapa.ps #icono_estaciones \n'
				else:
					contenido2 += '#psxy -R -Jm -O -K formas.d -St0.2 -G255/255/255 -W1  >> mapa.ps #icono_estaciones \n'



			elif 'icono_capitales' in line:
				if Var42.get() == 1:
					contenido2 += 'psxy -R -Jm -O -K capitales.d -Sc0.04 -G0/0/0 -W1 >> mapa.ps #icono_capitales\n'
				else:
					contenido2 += '#psxy -R -Jm -O -K capitales.d -Sc0.04 -G0/0/0 -W1 >> mapa.ps #icono_capitales\n'

			elif 'nombre_capitales' in line:
				if Var43.get() == 1:
					contenido2 += 'pstext nombresc.d -R -Jm -O -K -G0/0/0 >> mapa.ps #nombre_capitales\n'
				else:
					contenido2 += '#pstext nombresc.d -R -Jm -O -K -G0/0/0 >> mapa.ps #nombre_capitales\n'





			elif 'escalaP.txt' in line:
				if Var44.get() == 1: #check leyenda profundidad
					if self.Var7.get() == 1:#check latitud minima
						if Var46.get() == 1:#check zoom
							contenido2 += 'psxy -R-85/-66.7/-15/-3 -Jm0.4i -O -y-4i -x -K -Cpalette.cpt escalaP.txt -Sci -W0.05 >> mapa.ps\n'
						else:
							contenido2 +='psxy -R-85/-66.7/-15/-3 -Jm -O -y-4i -x -K -Cpalette.cpt escalaP.txt -Sci -W0.05 >> mapa.ps\n'
					else:
						contenido2 +='psxy -R-85/-66.7/-15/-3 -Jm -O -y-4i -x -K -Cpalette.cpt escalaP.txt -Sci -W0.05 >> mapa.ps\n'
				else:
					contenido2 += '#psxy -R-85/-66.7/-15/-3 -Jm -O -y-4i -x -K -Cpalette.cpt escalaP.txt -Sci -W0.05 >> mapa.ps\n'
			



			elif 'textoP.txt' in line:
				if Var44.get() == 1:#check leyenda profundidad
					if self.Var7.get() == 1:#check latitud minima
						if Var46.get() == 1:#check zoom
							contenido2 +='pstext -R-85/-66.7/-15/-3 -Jm0.4i -O  -K textoP.txt -W255/255/255  >> mapa.ps\n'
						else:
							contenido2 += 'pstext -R-85/-66.7/-15/-3 -Jm -O -K textoP.txt -W255/255/255  >> mapa.ps\n'
					else:
						contenido2 += 'pstext -R-85/-66.7/-15/-3 -Jm -O -K textoP.txt -W255/255/255  >> mapa.ps\n'
				else:
					contenido2 += '#pstext -R-85/-66.7/-15/-3 -Jm -O -K textoP.txt -W255/255/255  >> mapa.ps\n'


			elif 'escalaM.txt' in line:
				if Var45.get() == 1:
					contenido2 +='psxy -R-85/-66.7/-15/-3 -Jm -O -K  -Cpalette.cpt escalaM.txt -Sci -W0.5 >> mapa.ps\n'
				else:
					contenido2 += '#psxy -R-85/-66.7/-15/-3 -Jm -O -K  -Cpalette.cpt escalaM.txt -Sci -W0.5 >> mapa.ps\n'

			elif 'textoM.txt' in line:
				if Var45.get() == 1:
					contenido2 +='pstext -R-85/-66.7/-15/-3 -Jm -O  -K textoM.txt  -W255/255/255  >> mapa.ps\n'
				else:
					contenido2 += '#pstext -R-85/-66.7/-15/-3 -Jm -O  -K textoM.txt  -W255/255/255  >> mapa.ps\n'

			elif 'legendaEstaciones_all' in line:
				if Var41.get() == 1: #check icono estaciones
					if Var41_2.get() == 1: #check antena
						if Var41_3.get() == 1: #check leyenda estaciones
							contenido2 += 'psxy -R-85/-66.7/-15/-3 -Jm -O -K -Cpalettestations_all.cpt legendaEstaciones_all.txt -Skantena/0.15i -W0.25 >> mapa.ps\n'
						else:
							contenido2 += '#psxy -R-85/-66.7/-15/-3 -Jm -O -K -Cpalettestations_all.cpt legendaEstaciones_all.txt -Skantena/0.15i -W0.25 >> mapa.ps\n'
					else:
						contenido2 += '#psxy -R-85/-66.7/-15/-3 -Jm -O -K -Cpalettestations_all.cpt legendaEstaciones_all.txt -Skantena/0.15i -W0.25 >> mapa.ps\n'
				else:
					contenido2 += '#psxy -R-85/-66.7/-15/-3 -Jm -O -K -Cpalettestations_all.cpt legendaEstaciones_all.txt -Skantena/0.15i -W0.25 >> mapa.ps\n'

			elif 'textolegenda_all.txt' in line:
				if Var41.get() == 1: #check icono estaciones
					if Var41_2.get() == 1: #check antena
						if Var41_3.get() == 1: #check leyenda estaciones
							contenido2 += 'pstext -R-85/-66.7/-15/-3 -Jm -O -K  textolegenda_all.txt  >> mapa.ps \n'
						else:
							contenido2 += '#pstext -R-85/-66.7/-15/-3 -Jm -O -K  textolegenda_all.txt  >> mapa.ps \n'
					else:
						contenido2 += '#pstext -R-85/-66.7/-15/-3 -Jm -O -K  textolegenda_all.txt  >> mapa.ps \n'
				else:
					contenido2 += '#pstext -R-85/-66.7/-15/-3 -Jm -O -K  textolegenda_all.txt  >> mapa.ps \n'


			elif 'grdimage_mapa_zoom' in line:
				if self.Var7.get() == 1:#check latitud minima
					if Var46.get() == 1:#check zoom
						if Var44.get() == 1: #check leyenda profundidad
							if Var40.get() == 1: #Check nombre estaciones
								if Var41.get() == 1: #Check icono estaciones
									contenido2 += 'grdimage /home/topo/bati.grd -C/home/topo/bati2.cpt -R-82/-66.7/-4.3/14 -Bf7 -Jm0.08i -O -y4i -x0.2 -P -K -I/home/topo/bati.ilu >> mapa.ps #grdimage_mapa_zoom\n'
								else:
									contenido2 += 'grdimage /home/topo/bati.grd -C/home/topo/bati2.cpt -R-82/-66.7/-4.3/14 -Bf7 -Jm0.08i -O -y4i  -P -K -I/home/topo/bati.ilu >> mapa.ps #grdimage_mapa_zoom\n'
							else:
								contenido2 += 'grdimage /home/topo/bati.grd -C/home/topo/bati2.cpt -R-82/-66.7/-4.3/14 -Bf7 -Jm0.08i -O -y4i  -P -K -I/home/topo/bati.ilu >> mapa.ps #grdimage_mapa_zoom\n'
						else:
							contenido2 += 'grdimage /home/topo/bati.grd -C/home/topo/bati2.cpt -R-82/-66.7/-4.3/14 -Bf7 -Jm0.08i -O -P -K -I/home/topo/bati.ilu >> mapa.ps #grdimage_mapa_zoom\n'
					else:
						contenido2 += '#grdimage /home/topo/bati.grd -C/home/topo/bati2.cpt -R-82/-66.7/-4.3/14 -Bf7 -Jm0.08i -O -P -K -I/home/topo/bati.ilu >> mapa.ps #grdimage_mapa_zoom\n'
				else:
					contenido2 += '#grdimage /home/topo/bati.grd -C/home/topo/bati2.cpt -R-82/-66.7/-4.3/14 -Bf7 -Jm0.08i -O -P -K -I/home/topo/bati.ilu >> mapa.ps #grdimage_mapa_zoom\n'
			
			elif 'pscoast2_mapa_zoom' in line:
				if self.Var7.get() == 1:#check latitud minima
					if Var46.get() == 1:#check zoom
						contenido2 += 'pscoast -R-82/-66.7/-4.3/14 -Jm0.08i -W0.3p/200 -Di  -N1/0.4p -O -P -K >> mapa.ps #pscoast2_mapa_zoom \n'
					else:
						contenido2 += '#pscoast -R-82/-66.7/-4.3/14 -Jm0.08i -W0.3p/200 -Di  -N1/0.4p -O -P -K  >> mapa.ps #pscoast2_mapa_zoom \n'
				else:
					contenido2 += '#pscoast -R-82/-66.7/-4.3/14 -Jm0.08i -W0.3p/200 -Di  -N1/0.4p -O -P -K  >> mapa.ps #pscoast2_mapa_zoom \n'

			elif 'cuadrado_zoom' in line:
				if self.Var7.get() == 1:#check latitud minima
					if Var46.get() == 1:#check zoom
						contenido2 += './getrect -Jm0.08i -222 222 -222 222 '+v7_2str+' '+v8_2str+' '+v9_2str+' '+v10_2str+' | psxy -R -Jm0.08i -O -P -W1p/0/0/0 -L -N -A >> mapa.ps #cuadrado_zoom \n'
					else:
						contenido2 += '#./getrect -Jm0.08i -222 222 -222 222 '+v7_2str+' '+v8_2str+' '+v9_2str+' '+v10_2str+' | psxy -R -Jm0.08i -O -P -W1p/0/0/0 -L -N -A >> mapa.ps #cuadrado_zoom \n'
				else:
					contenido2 += '#./getrect -Jm0.08i -222 222 -222 222 2 2 2 2 | psxy -R -Jm0.08i -O -P -W1p/0/0/0 -L -N -A >> mapa.ps #cuadrado_zoom \n'

			
			elif 'PAPER_MEDIA' in line:
				if Var49.get() ==1:#check tamano de hoja
					contenido2 += 'gmtset PAPER_MEDIA '+v49.get()+'\n'
				else:
					contenido2 += 'gmtset PAPER_MEDIA a4 \n'



				
			elif 'ps2pdf' in line:
				if v47.get() == '.pdf':
					contenido2 += 'ps2pdf mapa.ps\n'
				else:
					contenido2 += '#ps2pdf mapa.ps\n'
			elif 'convert' in line:
				if v47.get() == '.jpg':
					contenido2 += 'convert mapa.ps mapa.jpg\n'
				else:
					contenido2 += '#convert mapa.ps mapa.jpg\n'
			else:
				contenido2 += line
			
		archivo2.close()
		archivo2=open(parametros2[0],"w")
		archivo2.write(contenido2)
		archivo2.close()
		




	

	

	############################ Menu Mapas ##########################
	self.menu=Button(self.frameThree, text='Menu', command=self.menu_inicial)
	self.menu.grid(row=23, column=5, padx=(0,10))
	
	self.menu=Button(self.frameThree, text='Mapa', command=mapa)
	self.menu.grid(row=23, column=2, padx=(0,10))
	
	self.menu=Button(self.frameThree, text='Cargar Conf.', command=modificar2)
	self.menu.grid(row=23, column=1, padx=(0,10))

	self.menu=Button(self.frameThree, text='Archivo Configuracion', command=conf)
	self.menu.grid(row=24, column=2, padx=(0,10))

	self.menu=Button(self.frameThree, text='Ver .PDF', command=pdf)
	self.menu.grid(row=23, column=4, padx=(0,10))

	self.menu=Button(self.frameThree, text='Ver .PS', command=ps)
	self.menu.grid(row=23, column=3, padx=(0,10))

	self.menu=Button(self.frameThree, text='Ver .JPG', command=jpg)
	self.menu.grid(row=24, column=1, padx=(0,10))
	
	self.salir=Button(self.frameThree, text='Salir', command=self.quit)
	self.salir.grid(row=24, column=5, padx=(0,10))
####################################################################################
################################GRAFICAS################################################
#####################################################################################
###############################GNUPLOT##########################################

    def ir_graficas(self):
	self.frameOne.destroy()
	self.frameFour=Toplevel()
	#######################hace el report1################################
	os.system("./expect_report")
	os.system("mv report.out report2.out")
	#######################borra la primera linea del report################################	
	report1=glob("/home/camilo/read_select/codigo/report2.out")
	archivo3=open(report1[0],"r")
	lines=archivo3.readlines()
	contenido3 = ''
	for line in lines:
		if 'Latitud' in line:
			contenido3 += ''
		else:
			contenido3 += line
	archivo3.close()
	archivo3=open(report1[0],"w")
	archivo3.write(contenido3)
	archivo3.close()

######################## MENU ELEGIBLE#######################################
	
	v52 = StringVar()
	v53 = StringVar()
	v54 = StringVar()
	v55 = StringVar()
	v55 = StringVar()
	v56 = StringVar()
	v57 = StringVar()
	v58 = StringVar()
	v59 = StringVar()
	v60 = StringVar()
	v61 = StringVar()
	v62 = StringVar()
	v63 = StringVar()
	v64 = StringVar()
	v65 = StringVar()
	v66 = StringVar()
	v67 = StringVar()
	v68 = StringVar()
	v69 = StringVar()
	v70 = StringVar()
	v71 = StringVar()
	v72 = StringVar()
	v73 = StringVar()
	v74 = StringVar()
	v75 = StringVar()
	v76 = StringVar()
	v77 = StringVar()
	v78 = StringVar()
	v79 = StringVar()
	v80 = StringVar()
	v81 = StringVar()
	v82 = StringVar()
	v83 = StringVar()
	v84 = StringVar()
	v85 = StringVar()
	v86 = StringVar()
	v87 = StringVar()
	v88 = StringVar()
	v89 = StringVar()
	v90 = StringVar()
	v91 = StringVar()
	v92 = StringVar()
	v93 = StringVar()
	v94 = StringVar()
	v95 = StringVar()
	v96 = StringVar()
	v97 = StringVar()
	v98 = StringVar()
	v99 = StringVar()
	v100 = StringVar()
	v101 = StringVar()
	v102 = StringVar()
	v103 = StringVar()
	v104 = StringVar()
	v105 = StringVar()
	v106 = StringVar()
	v107 = StringVar()
	v108 = StringVar()
	v109 = StringVar()
	v110 = StringVar()
	v111 = StringVar()

		

	Var52 = IntVar()
	Var53 = IntVar()
	Var54 = IntVar()
	Var55 = IntVar()
	Var56 = IntVar()
	Var57 = IntVar()
	Var58 = IntVar()
	Var59 = IntVar()
	Var60 = IntVar()
	Var61 = IntVar()
	Var62 = IntVar()
	Var63 = IntVar()
	Var64 = IntVar()
	Var65 = IntVar()
	Var65 = IntVar()
	Var66 = IntVar()
	Var67 = IntVar()
	Var68 = IntVar()
	Var69 = IntVar()
	Var70 = IntVar()
	Var71 = IntVar()
	Var72 = IntVar()
	Var73 = IntVar()
	Var74 = IntVar()
	Var75 = IntVar()

	self.texto = Label(self.frameFour, height='3', text = "GRAFICAS", justify="center")
        self.texto.grid(row=0, column=2)
	
	self.texto = Label(self.frameFour, height='3', text = "2D", justify="center")
        self.texto.grid(row=1, column=2)

	self.texto = Label(self.frameFour, height='3', text = "3D", justify="center")
        self.texto.grid(row=10, column=2)
	self.texto = Label(self.frameFour, height='3', text = "Rangos", justify="center")
        self.texto.grid(row=2, column=3)
        self.texto = Label(self.frameFour, height='3', text = "de   los", justify="center")
        self.texto.grid(row=2, column=4)
        self.texto = Label(self.frameFour, height='3', text = "Ejes", justify="center")
        self.texto.grid(row=2, column=5)
	self.texto = Label(self.frameFour, height='3', text = "Xmin", justify="center")
        self.texto.grid(row=3, column=3)
        self.texto = Label(self.frameFour, height='3', text = "Xmax", justify="center")
        self.texto.grid(row=3, column=4)
	self.texto = Label(self.frameFour, height='3', text = "Ymin", justify="center")
        self.texto.grid(row=3, column=5)
        self.texto = Label(self.frameFour, height='3', text = "Ymax", justify="center")
        self.texto.grid(row=3, column=6)
	
	self.texto = Label(self.frameFour, height='3', text = "Rangos ", justify="center")
        self.texto.grid(row=11, column=4)
        self.texto = Label(self.frameFour, height='3', text = "de  los", justify="center")
        self.texto.grid(row=11, column=5)
        self.texto = Label(self.frameFour, height='3', text = "Ejes", justify="center")
        self.texto.grid(row=11, column=6)
        
        
	self.texto = Label(self.frameFour, height='3', text = "Xmin", justify="center")
        self.texto.grid(row=12, column=3)
        self.texto = Label(self.frameFour, height='3', text = "Xmax", justify="center")
        self.texto.grid(row=12, column=4)
	self.texto = Label(self.frameFour, height='3', text = "Ymin", justify="center")
        self.texto.grid(row=12, column=5)
        self.texto = Label(self.frameFour, height='3', text = "Ymax", justify="center")
        self.texto.grid(row=12, column=6)
	self.texto = Label(self.frameFour, height='3', text = "Zmin", justify="center")
        self.texto.grid(row=12, column=7)
        self.texto = Label(self.frameFour, height='3', text = "Zmax", justify="center")
        self.texto.grid(row=12, column=8)
	
	
	
	self.check = Checkbutton(self.frameFour, variable=Var52, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=4, column=0)
	self.check = Checkbutton(self.frameFour, variable=Var53, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=5, column=0)
	self.check = Checkbutton(self.frameFour, variable=Var54, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=6, column=0)
	self.check = Checkbutton(self.frameFour, variable=Var55, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=7, column=0)
	self.check = Checkbutton(self.frameFour, variable=Var56, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=8, column=0)
	self.check = Checkbutton(self.frameFour, variable=Var57, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=9, column=0)

	
	self.check = Checkbutton(self.frameFour, variable=Var58, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=13, column=0)
	self.check = Checkbutton(self.frameFour, variable=Var59, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=14, column=0)
	self.check = Checkbutton(self.frameFour, variable=Var60, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=15, column=0)
	self.check = Checkbutton(self.frameFour, variable=Var61, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=16, column=0)
	self.check = Checkbutton(self.frameFour, variable=Var62, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=17, column=0)
	self.check = Checkbutton(self.frameFour, variable=Var63, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=18, column=0)


	self.check = Checkbutton(self.frameFour, variable=Var64, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=4, column=2)
	self.check = Checkbutton(self.frameFour, variable=Var65, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=5, column=2)
	self.check = Checkbutton(self.frameFour, variable=Var66, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=6, column=2)
	self.check = Checkbutton(self.frameFour, variable=Var67, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=7, column=2)
	self.check = Checkbutton(self.frameFour, variable=Var68, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=8, column=2)
	self.check = Checkbutton(self.frameFour, variable=Var69, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=9, column=2)
	

	
	

	self.check = Checkbutton(self.frameFour, variable=Var70, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=13, column=2)
	self.check = Checkbutton(self.frameFour, variable=Var71, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=14, column=2)
	self.check = Checkbutton(self.frameFour, variable=Var72, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=15, column=2)
	self.check = Checkbutton(self.frameFour, variable=Var73, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=16, column=2)
	self.check = Checkbutton(self.frameFour, variable=Var74, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=17, column=2)
	self.check = Checkbutton(self.frameFour, variable=Var75, onvalue =1, offvalue = 0, height=1, width = 5)
	self.check.grid(row=18, column=2)


	
	

	self.E39 = Entry(self.frameFour,width=4,textvariable=v52)
        self.E39.grid(row=4, column=3, padx=(0,10))
	self.E39 = Entry(self.frameFour,width=4,textvariable=v53)
        self.E39.grid(row=5, column=3, padx=(0,10))
	self.E39 = Entry(self.frameFour,width=4,textvariable=v54)
        self.E39.grid(row=6, column=3, padx=(0,10))
	self.E39 = Entry(self.frameFour,width=4,textvariable=v55)
        self.E39.grid(row=7, column=3, padx=(0,10))
	self.E39 = Entry(self.frameFour,width=4,textvariable=v56)
        self.E39.grid(row=8, column=3, padx=(0,10))
	self.E39 = Entry(self.frameFour,width=4,textvariable=v57)
        self.E39.grid(row=9, column=3, padx=(0,10))

	self.E39 = Entry(self.frameFour,width=4,textvariable=v58)
        self.E39.grid(row=4, column=4, padx=(0,10))
	self.E39 = Entry(self.frameFour,width=4,textvariable=v59)
        self.E39.grid(row=5, column=4, padx=(0,10))
	self.E39 = Entry(self.frameFour,width=4,textvariable=v60)
        self.E39.grid(row=6, column=4, padx=(0,10))
	self.E39 = Entry(self.frameFour,width=4,textvariable=v61)
        self.E39.grid(row=7, column=4, padx=(0,10))
	self.E39 = Entry(self.frameFour,width=4,textvariable=v62)
        self.E39.grid(row=8, column=4, padx=(0,10))
	self.E39 = Entry(self.frameFour,width=4,textvariable=v63)
        self.E39.grid(row=9, column=4, padx=(0,10))
	
	self.E39 = Entry(self.frameFour,width=4,textvariable=v64)
        self.E39.grid(row=4, column=5, padx=(0,10))
	self.E39 = Entry(self.frameFour,width=4,textvariable=v65)
        self.E39.grid(row=5, column=5, padx=(0,10))
	self.E39 = Entry(self.frameFour,width=4,textvariable=v66)
        self.E39.grid(row=6, column=5, padx=(0,10))
	self.E39 = Entry(self.frameFour,width=4,textvariable=v67)
        self.E39.grid(row=7, column=5, padx=(0,10))
	self.E39 = Entry(self.frameFour,width=4,textvariable=v68)
        self.E39.grid(row=8, column=5, padx=(0,10))
	self.E39 = Entry(self.frameFour,width=4,textvariable=v69)
        self.E39.grid(row=9, column=5, padx=(0,10))

	self.E39 = Entry(self.frameFour,width=4,textvariable=v70)
        self.E39.grid(row=4, column=6, padx=(0,10))
	self.E39 = Entry(self.frameFour,width=4,textvariable=v71)
        self.E39.grid(row=5, column=6, padx=(0,10))
	self.E39 = Entry(self.frameFour,width=4,textvariable=v72)
        self.E39.grid(row=6, column=6, padx=(0,10))
	self.E39 = Entry(self.frameFour,width=4,textvariable=v73)
        self.E39.grid(row=7, column=6, padx=(0,10))
	self.E39 = Entry(self.frameFour,width=4,textvariable=v74)
        self.E39.grid(row=8, column=6, padx=(0,10))
	self.E39 = Entry(self.frameFour,width=4,textvariable=v75)
        self.E39.grid(row=9, column=6, padx=(0,10))
	
	
	self.E39 = Entry(self.frameFour,width=4,textvariable=v76)
        self.E39.grid(row=13, column=3, padx=(0,10))
	self.E39 = Entry(self.frameFour,width=4,textvariable=v77)
        self.E39.grid(row=14, column=3, padx=(0,10))
	self.E39 = Entry(self.frameFour,width=4,textvariable=v78)
        self.E39.grid(row=15, column=3, padx=(0,10))
	self.E39 = Entry(self.frameFour,width=4,textvariable=v79)
        self.E39.grid(row=16, column=3, padx=(0,10))
	self.E39 = Entry(self.frameFour,width=4,textvariable=v80)
        self.E39.grid(row=17, column=3, padx=(0,10))
	self.E39 = Entry(self.frameFour,width=4,textvariable=v81)
        self.E39.grid(row=18, column=3, padx=(0,10))

	self.E39 = Entry(self.frameFour,width=4,textvariable=v82)
        self.E39.grid(row=13, column=4, padx=(0,10))
	self.E39 = Entry(self.frameFour,width=4,textvariable=v83)
        self.E39.grid(row=14, column=4, padx=(0,10))
	self.E39 = Entry(self.frameFour,width=4,textvariable=v84)
        self.E39.grid(row=15, column=4, padx=(0,10))
	self.E39 = Entry(self.frameFour,width=4,textvariable=v85)
        self.E39.grid(row=16, column=4, padx=(0,10))
	self.E39 = Entry(self.frameFour,width=4,textvariable=v86)
        self.E39.grid(row=17, column=4, padx=(0,10))
	self.E39 = Entry(self.frameFour,width=4,textvariable=v87)
        self.E39.grid(row=18, column=4, padx=(0,10))

	self.E39 = Entry(self.frameFour,width=4,textvariable=v88)
        self.E39.grid(row=13, column=5, padx=(0,10))
	self.E39 = Entry(self.frameFour,width=4,textvariable=v89)
        self.E39.grid(row=14, column=5, padx=(0,10))
	self.E39 = Entry(self.frameFour,width=4,textvariable=v90)
        self.E39.grid(row=15, column=5, padx=(0,10))
	self.E39 = Entry(self.frameFour,width=4,textvariable=v91)
        self.E39.grid(row=16, column=5, padx=(0,10))
	self.E39 = Entry(self.frameFour,width=4,textvariable=v92)
        self.E39.grid(row=17, column=5, padx=(0,10))
	self.E39 = Entry(self.frameFour,width=4,textvariable=v93)
        self.E39.grid(row=18, column=5, padx=(0,10))
	
	self.E39 = Entry(self.frameFour,width=4,textvariable=v94)
        self.E39.grid(row=13, column=6, padx=(0,10))
	self.E39 = Entry(self.frameFour,width=4,textvariable=v95)
        self.E39.grid(row=14, column=6, padx=(0,10))
	self.E39 = Entry(self.frameFour,width=4,textvariable=v96)
        self.E39.grid(row=15, column=6, padx=(0,10))
	self.E39 = Entry(self.frameFour,width=4,textvariable=v97)
        self.E39.grid(row=16, column=6, padx=(0,10))
	self.E39 = Entry(self.frameFour,width=4,textvariable=v98)
        self.E39.grid(row=17, column=6, padx=(0,10))
	self.E39 = Entry(self.frameFour,width=4,textvariable=v99)
        self.E39.grid(row=18, column=6, padx=(0,10))
        
        self.E39 = Entry(self.frameFour,width=4,textvariable=v100)
        self.E39.grid(row=13, column=7, padx=(0,10))
	self.E39 = Entry(self.frameFour,width=4,textvariable=v101)
        self.E39.grid(row=14, column=7, padx=(0,10))
	self.E39 = Entry(self.frameFour,width=4,textvariable=v102)
        self.E39.grid(row=15, column=7, padx=(0,10))
	self.E39 = Entry(self.frameFour,width=4,textvariable=v103)
        self.E39.grid(row=16, column=7, padx=(0,10))
	self.E39 = Entry(self.frameFour,width=4,textvariable=v104)
        self.E39.grid(row=17, column=7, padx=(0,10))
	self.E39 = Entry(self.frameFour,width=4,textvariable=v105)
        self.E39.grid(row=18, column=7, padx=(0,10))
        
        self.E39 = Entry(self.frameFour,width=4,textvariable=v106)
        self.E39.grid(row=13, column=8, padx=(0,10))
	self.E39 = Entry(self.frameFour,width=4,textvariable=v107)
        self.E39.grid(row=14, column=8, padx=(0,10))
	self.E39 = Entry(self.frameFour,width=4,textvariable=v108)
        self.E39.grid(row=15, column=8, padx=(0,10))
	self.E39 = Entry(self.frameFour,width=4,textvariable=v109)
        self.E39.grid(row=16, column=8, padx=(0,10))
	self.E39 = Entry(self.frameFour,width=4,textvariable=v110)
        self.E39.grid(row=17, column=8, padx=(0,10))
	self.E39 = Entry(self.frameFour,width=4,textvariable=v111)
        self.E39.grid(row=18, column=8, padx=(0,10))

	self.texto = Label(self.frameFour, height='3', text = "Latitud vs Error", justify="center")
        self.texto.grid(row=4, column=1)
	self.texto = Label(self.frameFour, height='3', text = "Longitud vs Error", justify="center")
        self.texto.grid(row=5, column=1)
	self.texto = Label(self.frameFour, height='3', text = "Profundidad vs Error", justify="center")
        self.texto.grid(row=6, column=1)
	self.texto = Label(self.frameFour, height='3', text = "Profundidad vs No de Sismos", justify="center")
        self.texto.grid(row=7, column=1)
	self.texto = Label(self.frameFour, height='3', text = "RMS vs No de Sismos", justify="center")
        self.texto.grid(row=8, column=1)
	self.texto = Label(self.frameFour, height='3', text = "Ml vs No de Sismos", justify="center")
        self.texto.grid(row=9, column=1)

	self.texto = Label(self.frameFour, height='3', text = "Profundidad vs No de Sismos", justify="center")
        self.texto.grid(row=13, column=1)
	self.texto = Label(self.frameFour, height='3', text = "RMS vs No de Sismos", justify="center")
        self.texto.grid(row=14, column=1)
	self.texto = Label(self.frameFour, height='3', text = "Ml vs No de Sismos", justify="center")
        self.texto.grid(row=15, column=1)
	self.texto = Label(self.frameFour, height='3', text = "No Sismos vs RMS-Profundidad", justify="center")
        self.texto.grid(row=16, column=1)
	self.texto = Label(self.frameFour, height='3', text = "No Sismos vs Ml-Profundidad", justify="center")
        self.texto.grid(row=17, column=1)
	self.texto = Label(self.frameFour, height='3', text = "No Sismos vs RMS-Ml", justify="center")
        self.texto.grid(row=18, column=1)


	
###################################Codigo Graficas################################
	def codigo_graficas():

		report=glob("/home/camilo/read_select/codigo/report2.out")
		archivo4=open(report[0],"r")
		lines=archivo4.readlines()
		#print (lines[0])


		sum_prof=[0 for i in range(21)]

		sum_rms=[0 for i in range(21)]

		sum_mag=[0 for i in range(21)]

		sum_magM=numpy.zeros((21, 21))

		sum_profM=numpy.zeros((21, 21))

		sum_profM2=numpy.zeros((21, 21))

		#print sum_magM
		#print sum_magM[1][:]

		sum_magT=[0 for i in range(21)]
		sum_profT=[0 for i in range(21)]

		vec_prof = numpy.arange(0,210,10)
		vec_rms = numpy.arange(0.1,2.2,0.1)
		vec_mag = numpy.arange(0,10.5,0.5)

		#f = os.fdopen(filename1, 'w')

			##################SUMA PROFUNDIDAD###########################
		def func_prof():
			if prof == 0:
				sum_prof[0] += 1
			if prof > 0:
				if prof <= 10:
					sum_prof[1] += 1
			if prof > 10:
				if prof <= 20:
					sum_prof[2] += 1
			if prof > 20:
				if prof <= 30:
					sum_prof[3] += 1
			if prof > 30:
				if prof <= 40:
					sum_prof[4] += 1
			if prof > 40:
				if prof <= 50:
					sum_prof[5]  += 1
			if prof > 50:
				if prof <= 60:
					sum_prof[6] += 1	
			if prof > 60:
				if prof <= 70:
					sum_prof[7] += 1
			if prof > 70:
				if prof <= 80:
					sum_prof[8] += 1
			if prof > 80:
				if prof <= 90:
					sum_prof[9] += 1
			if prof > 90:
				if prof <= 100:
					sum_prof[10]  += 1
			if prof > 100:
				if prof <= 110:
					sum_prof[11]  += 1
			if prof > 110:
				if prof <= 120:
					sum_prof[12] += 1
			if prof > 120:
				if prof <= 130:
					sum_prof[13] += 1
			if prof > 130:
				if prof <= 140:
					sum_prof[14] += 1
			if prof > 140:
				if prof <= 150:
					sum_prof[15] += 1
			if prof > 150:
				if prof <= 160:
					sum_prof[16] += 1
			if prof > 160:
				if prof <= 170:
					sum_prof[17] += 1
			if prof > 170:
				if prof <= 180:
					sum_prof[18] += 1
			if prof > 180:
				if prof <= 190:
					sum_prof[19] += 1
			if prof > 190:
				if prof <= 200:
					sum_prof[20] += 1

			######################SUMA RMS###############################
		def func_rms():	
			if rms == 0.1:
				sum_rms[0] += 1
			if rms == 0.2:
				sum_rms[1] += 1
			if rms == 0.3:
				sum_rms[2] += 1
			if rms == 0.4:
				sum_rms[3] += 1
			if rms == 0.5:
				sum_rms[4] += 1
			if rms == 0.6:
				sum_rms[5] += 1
			if rms == 0.7:
				sum_rms[6] += 1
			if rms == 0.8:
				sum_rms[7] += 1
			if rms == 0.9:
				sum_rms[8] += 1
			if rms == 1.0:
				sum_rms[9] += 1
			if rms == 1.1:
				sum_rms[10] += 1
			if rms == 1.2:
				sum_rms[11] += 1
			if rms == 1.3:
				sum_rms[12] += 1
			if rms == 1.4:
				sum_rms[13] += 1
			if rms == 1.5:
				sum_rms[14] += 1
			if rms == 1.6:
				sum_rms[15] += 1
			if rms == 1.7:
				sum_rms[16] += 1
			if rms == 1.8:
				sum_rms[17] += 1
			if rms == 1.9:
				sum_rms[18] += 1
			if rms == 2.0:
				sum_rms[19] += 1
			if rms > 2:
				sum_rms[20] += 1
			#####################SUMA MAGNITUD###########################
		def func_mag():
			if mag == 0:
				sum_mag[0] += 1
			if mag > 0:
				if mag <= 0.5:
					sum_mag[1] += 1
			if mag > 0.5:
				if mag <= 1.0:
					sum_mag[2] += 1
			if mag > 1.0:
				if mag <= 1.5:
					sum_mag[3] += 1
			if mag > 1.5:
				if mag <= 2.0:
					sum_mag[4] += 1
			if mag > 2.0:
				if mag <= 2.5:
					sum_mag[5] += 1
			if mag > 2.5:
				if mag <= 3.0:
					sum_mag[6] += 1
			if mag > 3.0:
				if mag <= 3.5:
					sum_mag[7] += 1
			if mag > 3.5:
				if mag <= 4.0:
					sum_mag[8] += 1
			if mag > 4.0:
				if mag <= 4.5:
					sum_mag[9] += 1
			if mag > 4.5:
				if mag <= 5.0:
					sum_mag[10] += 1
			if mag > 5.0:
				if mag <= 5.5:
					sum_mag[11] += 1
			if mag > 5.5:
				if mag <= 6.0:
					sum_mag[12] += 1
			if mag > 6.0:
				if mag <= 6.5:
					sum_mag[13] += 1
			if mag > 6.5:
				if mag <= 7.0:
					sum_mag[14] += 1
			if mag > 7.0:
				if mag <= 7.5:
					sum_mag[15] += 1
			if mag > 7.5:
				if mag <= 8.0:
					sum_mag[16] += 1
			if mag > 8.0:
				if mag <= 8.5:
					sum_mag[17] += 1
			if mag > 8.5:
				if mag <= 9.0:
					sum_mag[18] += 1
			if mag > 9.0:
				if mag <= 9.5:
					sum_mag[19] += 1
			if mag > 9.5:
				if mag <= 10.0:
					sum_mag[20] += 1
		##############################Valores de Sumas Total#################
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			func_prof()
			func_rms()
			func_mag()

		#print sum_prof	
		#print sum_rms
		#print sum_mag
		sum_magT[:]=sum_mag[:]
		sum_profT[:]=sum_prof[:]
		#print sum_magT
		#print sum_mag
		##############################Valores de Sumas Magnitud por RMS#####
		#del sum_mag
		sum_mag=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if rms==0.1:
				func_mag()
		sum_magM[0][:]=sum_mag[:]
		#del sum_mag
		sum_mag=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if rms==0.2:
				func_mag()
		sum_magM[1][:]=sum_mag[:]
		#del sum_mag
		sum_mag=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if rms==0.3:
				func_mag()
		sum_magM[2][:]=sum_mag[:]
		#del sum_mag
		sum_mag=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if rms==0.4:
				func_mag()
		sum_magM[3][:]=sum_mag[:]
		#del sum_mag
		sum_mag=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if rms==0.5:
				func_mag()
		sum_magM[4][:]=sum_mag[:]
		#del sum_mag
		sum_mag=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if rms==0.6:
				func_mag()
		sum_magM[5][:]=sum_mag[:]
		#del sum_mag
		sum_mag=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if rms==0.7:
				func_mag()
		sum_magM[6][:]=sum_mag[:]
		#del sum_mag
		sum_mag=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if rms==0.8:
				func_mag()
		sum_magM[7][:]=sum_mag[:]
		#del sum_mag
		sum_mag=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if rms==0.9:
				func_mag()
		sum_magM[8][:]=sum_mag[:]
		#del sum_mag
		sum_mag=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if rms==1.0:
				func_mag()
		sum_magM[9][:]=sum_mag[:]
		#del sum_mag
		sum_mag=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if rms==1.1:
				func_mag()
		sum_magM[10][:]=sum_mag[:]
		#del sum_mag
		sum_mag=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if rms==1.2:
				func_mag()
		sum_magM[11][:]=sum_mag[:]
		#del sum_mag
		sum_mag=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if rms==1.3:
				func_mag()
		sum_magM[12][:]=sum_mag[:]
		#del sum_mag
		sum_mag=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if rms==1.4:
				func_mag()
		sum_magM[13][:]=sum_mag[:]
		#del sum_mag
		sum_mag=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if rms==1.5:
				func_mag()
		sum_magM[14][:]=sum_mag[:]
		#del sum_mag
		sum_mag=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if rms==1.6:
				func_mag()
		sum_magM[15][:]=sum_mag[:]
		#del sum_mag
		sum_mag=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if rms==1.7:
				func_mag()
		sum_magM[16][:]=sum_mag[:]
		#del sum_mag
		sum_mag=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if rms==1.8:
				func_mag()
		sum_magM[17][:]=sum_mag[:]
		#del sum_mag
		sum_mag=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if rms==1.9:
				func_mag()
		sum_magM[18][:]=sum_mag[:]
		#del sum_mag
		sum_mag=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if rms==2.0:
				func_mag()
		sum_magM[19][:]=sum_mag[:]
		#del sum_mag
		sum_mag=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if rms>2.0:
				func_mag()
		sum_magM[20][:]=sum_mag[:]
		#del sum_mag

		##############################Valores de Sumas Profundidad por RMS###
		#del sum_prof
		sum_prof=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if rms==0.1:
				func_prof()
		sum_profM[0][:]=sum_prof[:]
		#del sum_prof
		sum_prof=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if rms==0.2:
				func_prof()
		sum_profM[1][:]=sum_prof[:]
		#del sum_prof
		sum_prof=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if rms==0.3:
				func_prof()
		sum_profM[2][:]=sum_prof[:]
		#del sum_prof
		sum_prof=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if rms==0.4:
				func_prof()
		sum_profM[3][:]=sum_prof[:]
		#del sum_prof
		sum_prof=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if rms==0.5:
				func_prof()
		sum_profM[4][:]=sum_prof[:]
		#del sum_prof
		sum_prof=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if rms==0.6:
				func_prof()
		sum_profM[5][:]=sum_prof[:]
		#del sum_prof
		sum_prof=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if rms==0.7:
				func_prof()
		sum_profM[6][:]=sum_prof[:]
		#del sum_prof
		sum_prof=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if rms==0.8:
				func_prof()
		sum_profM[7][:]=sum_prof[:]
		#del sum_prof
		sum_prof=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if rms==0.9:
				func_prof()
		sum_profM[8][:]=sum_prof[:]
		#del sum_prof
		sum_prof=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if rms==1.0:
				func_prof()
		sum_profM[9][:]=sum_prof[:]
		#del sum_prof
		sum_prof=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if rms==1.1:
				func_prof()
		sum_profM[10][:]=sum_prof[:]
		#del sum_prof
		sum_prof=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if rms==1.2:
				func_prof()
		sum_profM[11][:]=sum_prof[:]
		#del sum_prof
		sum_prof=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if rms==1.3:
				func_prof()
		sum_profM[12][:]=sum_prof[:]
		#del sum_prof
		sum_prof=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if rms==1.4:
				func_prof()
		sum_profM[13][:]=sum_prof[:]
		#del sum_prof
		sum_prof=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if rms==1.5:
				func_prof()
		sum_profM[14][:]=sum_prof[:]
		#del sum_prof
		sum_prof=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if rms==1.6:
				func_prof()
		sum_profM[15][:]=sum_prof[:]
		#del sum_prof
		sum_prof=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if rms==1.7:
				func_prof()
		sum_profM[16][:]=sum_prof[:]
		#del sum_prof
		sum_prof=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if rms==1.8:
				func_prof()
		sum_profM[17][:]=sum_prof[:]
		#del sum_prof
		sum_prof=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if rms==1.9:
				func_prof()
		sum_profM[18][:]=sum_prof[:]
		#del sum_prof
		sum_prof=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if rms==2.0:
				func_prof()
		sum_profM[19][:]=sum_prof[:]
		#del sum_prof
		sum_prof=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if rms > 2.0:
				func_prof()
		sum_profM[20][:]=sum_prof[:]

		##############################Valores de Profundidad por Magnitud####

		#del sum_prof
		sum_prof=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if mag == 0:
				func_prof()
		sum_profM2[0][:]=sum_prof[:]
		#del sum_prof
		sum_prof=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if mag > 0:
				if mag <= 0.5:
					func_prof()
		sum_profM2[1][:]=sum_prof[:]
		#del sum_prof
		sum_prof=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if mag > 0.5:
				if mag <= 1.0:
					func_prof()
		sum_profM2[2][:]=sum_prof[:]
		#del sum_prof
		sum_prof=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if mag > 1.0:
				if mag <= 1.5:
					func_prof()
		sum_profM2[3][:]=sum_prof[:]
		#del sum_prof
		sum_prof=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if mag > 1.5:
				if mag <= 2.0:
					func_prof()
		sum_profM2[4][:]=sum_prof[:]
		#del sum_prof
		sum_prof=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if mag > 2.0:
				if mag <= 2.5:
					func_prof()
		sum_profM2[5][:]=sum_prof[:]
		#del sum_prof
		sum_prof=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if mag > 2.5:
				if mag <= 3.0:
					func_prof()
		sum_profM2[6][:]=sum_prof[:]
		#del sum_prof
		sum_prof=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if mag > 3.0:
				if mag <= 3.5:
					func_prof()
		sum_profM2[7][:]=sum_prof[:]
		#del sum_prof
		sum_prof=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if mag > 3.5:
				if mag <= 4.0:
					func_prof()
		sum_profM2[8][:]=sum_prof[:]
		#del sum_prof
		sum_prof=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if mag > 4.0:
				if mag <= 4.5:
					func_prof()
		sum_profM2[9][:]=sum_prof[:]
		#del sum_prof
		sum_prof=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if mag > 4.5:
				if mag <= 5.0:
					func_prof()
		sum_profM2[10][:]=sum_prof[:]
		#del sum_prof
		sum_prof=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if mag > 5.0:
				if mag <= 5.5:
					func_prof()
		sum_profM2[11][:]=sum_prof[:]
		#del sum_prof
		sum_prof=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if mag > 5.5:
				if mag <= 6.0:
					func_prof()
		sum_profM2[12][:]=sum_prof[:]
		#del sum_prof
		sum_prof=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if mag > 6.0:
				if mag <= 6.5:
					func_prof()
		sum_profM2[13][:]=sum_prof[:]
		#del sum_prof
		sum_prof=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if mag > 6.5:
				if mag <= 7.0:
					func_prof()
		sum_profM2[14][:]=sum_prof[:]
		#del sum_prof
		sum_prof=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if mag > 7.0:
				if mag <= 7.5:
					func_prof()
		sum_profM2[15][:]=sum_prof[:]
		#del sum_prof
		sum_prof=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if mag > 7.5:
				if mag <= 8.0:
					func_prof()
		sum_profM2[16][:]=sum_prof[:]
		#del sum_prof
		sum_prof=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if mag > 8.0:
				if mag <= 8.5:
					func_prof()
		sum_profM2[17][:]=sum_prof[:]
		#del sum_prof
		sum_prof=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if mag > 8.5:
				if mag <= 9.0:
					func_prof()
		sum_profM2[18][:]=sum_prof[:]
		#del sum_prof
		sum_prof=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if mag > 9.0:
				if mag <= 9.5:
					func_prof()
		sum_profM2[19][:]=sum_prof[:]
		#del sum_prof
		sum_prof=[0 for i in range(21)]
		for line in lines:
			campo = line.split(' ')
			prof = float(line[30:35])
			rms = float(line[43:46])
			mag = float(line[48:51])
			if mag > 9.5:
				if mag <= 10.0:
					func_prof()
		sum_profM2[20][:]=sum_prof[:]



		#print sum_prof
		#print sum_profM[5][:]
		#print sum_profT
		#print sum_profM
		g = Gnuplot.Gnuplot()
		#########################Grafias 2D Localizacion vs Errores#########
		if Var52.get() ==1:
			g('set autoscale')
			g.title('LATITUD VS ERROR EN LATITUD')
			g('set terminal jpeg')
			g('set output "late.jpg"')
			g('set style fill transparent solid 0.5 border lc rgb "black"')
			g.xlabel('LATITUD')
			g.ylabel('ERROR')
			if Var64.get() ==1:
				g('set xrange ['+v52.get()+':'+v58.get()+']')
				g('set yrange ['+v64.get()+':'+v70.get()+']')
			
			g('unset key')
			g('set grid')
			g('plot "report2.out" u 1:2:(0.075) with circles lc rgb "gray"' )
			#raw_input('Please press return to continue...\n')
		if Var53.get() ==1:
			g('set autoscale')
			g.title('LONGITUD VS ERROR EN LONGITUD')
			if Var65.get() ==1:
				g('set xrange ['+v53.get()+':'+v59.get()+']')
				g('set yrange ['+v65.get()+':'+v71.get()+']')
			g('set terminal jpeg')
			g('set output "lone.jpg"')
			g.xlabel('LONGITUD')
			g.ylabel('ERROR')
			g('unset key')
			g('plot "report2.out" u 3:4:(0.075) with circles lc rgb "blue"')
			#raw_input('Please press return to continue...\n')
		if Var54.get() ==1:
			g('set autoscale')
			g.title('PROFUNDIDAD VS ERROR EN PROFUNDIDAD')
			g('set terminal jpeg')
			g('set output "profe.jpg"')
			g('set style fill transparent solid 0.5 border lc rgb "black"')
			if Var66.get() ==1:
				g('set xrange ['+v54.get()+':'+v60.get()+']')
				g('set yrange ['+v66.get()+':'+v72.get()+']')
			g('set grid')
			g('unset key')
			#g('set xrange [-10:200]')
			g.xlabel('PROFUNDIDAD')
			g.ylabel('ERROR')
			g('plot "report2.out" u 5:6:(2) with circles lc rgb "red"')
			#raw_input('Please press return to continue...\n')
			
		#########################Grafias 2D Prof,Mag,RMS###################

		if Var55.get() ==1:
			g('set autoscale')
			#g('set xrange [0:200]')
			#g('set yrange [0.1:20]')
			g.title('PROFUNDIDAD')
			g('set terminal jpeg')
			g('set output "prof.jpg"')
			g.xlabel('Profundidad')
			g.ylabel('Numero de Sismos')
			g.plot(Gnuplot.Data(vec_prof,sum_profT,inline=1, with_='linespoints'))
			#raw_input('Please press return to continue...\n')

			g('set autoscale')
			g('set boxwidth 0.9 relative')
			g('set terminal jpeg')
			g('set output "profb.jpg"')
			g('set style fill solid 1')
			g.plot(Gnuplot.Data(vec_prof,sum_profT,inline=1, with_='boxes'))
			#raw_input('Please press return to continue...\n')

		if Var56.get() ==1:
			g('set autoscale')
			#g('set xrange [0:2.0]')
			#g('set yrange [0.1:20]')
			g('set terminal jpeg')
			g('set output "rms.jpg"')
			g.title('RMS')
			g.xlabel('RMS')
			g.ylabel('Numero de Sismos')
			g.plot(Gnuplot.Data(vec_rms,sum_rms,inline=1, with_='linespoints'))
			#raw_input('Please press return to continue...\n')
			#print vec_mag
			g('set autoscale')
			g('set boxwidth 0.9 relative')
			g('set style fill solid 1')
			g('set terminal jpeg')
			g('set output "rmsb.jpg"')
			g.plot(Gnuplot.Data(vec_rms,sum_rms,inline=1, with_='boxes'))
			#raw_input('Please press return to continue...\n')

		if Var57.get() ==1:
			g('set autoscale')
			#g('set xrange [0:9.0]')
			#g('set yrange [0.1:20]')
			g('set terminal jpeg')
			g('set output "mag.jpg"')
			g.title('MAGNITUD')
			g.xlabel('Magnitud Ml')
			g.ylabel('Numero de Sismos')
			g.plot(Gnuplot.Data(vec_mag,sum_magT,inline=1, with_='linespoints'))
			#raw_input('Please press return to continue...\n')
			g('set autoscale')
			g('set boxwidth 0.9 relative')
			g('set style fill solid 1')
			g('set terminal jpeg')
			g('set output "magb.jpg"')
			g.plot(Gnuplot.Data(vec_mag,sum_magT,inline=1, with_='boxes'))
			#raw_input('Please press return to continue...\n')


		xm = vec_rms[:,numpy.newaxis]
		ym = vec_mag[numpy.newaxis,:]
		zm = vec_prof[numpy.newaxis,:]

		######################Grafica 3D Profundidad########################
		m = (sum_profT+zm-zm+xm-xm)
		if Var58.get() ==1:
			g('set terminal jpeg')
			g('set output "prof3d.jpg"')
			g('set pm3d')
			g.title('Profundidad')
			g('set zlabel "Numero de sismos" rotate parallel ')
			g.xlabel('')
			g.ylabel('Profundidad')
			g('unset xtics')
			g('set view 75,75')
			g('set palette defined (0 "blue", 4 "white", 9 "red")')
			g.splot(Gnuplot.GridData(m,vec_rms,vec_prof, binary=0, inline=0, with_='pm3d'))
			#raw_input('Please press return to continue...\n')
		############################Grafica 3D RMS#########################
		del m
		m = (sum_rms+ym-ym+xm-xm)
		if Var59.get() ==1:
			g('set pm3d')
			g('set terminal jpeg')
			g('set output "rms3d.jpg"')
			g.title('RMS')
			g('set zlabel "Numero de sismos" rotate parallel ')
			g.xlabel('')
			g.ylabel('RMS')
			g('unset xtics')
			g('set view 75,75')
			g('set palette defined (0 "blue", 4 "white", 9 "red")')
			g.splot(Gnuplot.GridData(m,vec_mag,vec_rms, binary=0, inline=0, with_='pm3d'))
			#raw_input('Please press return to continue...\n')
		######################Grafica 3D Magnitud###########################
		del m
		m = (sum_magT+ym-ym+xm-xm)
		if Var60.get() ==1:
			#print m
			#g('set dgrid3d 50,50')
			#g('set isosample 100')
			#g('set contour base')
			#g('set hidden3d')
			g('set terminal jpeg')
			g('set output "mag3d.jpg"')
			g('set pm3d')
			#g('set palette gray')
			g.title('Magnitud')
			g('set zlabel "Numero de sismos" rotate parallel ')
			g.xlabel('')
			g.ylabel('Magnitud ML')
			#g('set zlabel "Nuemro de Sismos"')
			g('unset xtics')
			g('set view 75,75')
			#g('set xrange [0.1:2.1]')
			#g('set yrange [0.0:10.0]')
			#g('set zrange [0:10]')
			g('set palette defined (0 "blue", 4 "white", 9 "red")')
			g.splot(Gnuplot.GridData(m,vec_rms,vec_mag, binary=0, inline=0, with_='pm3d'))
			#raw_input('Please press return to continue...\n')
		############################Grafica RMS-PROFUNDIDAD-#Sismos##########
		if Var61.get() ==1:
			g('set autoscale')
			g('set terminal jpeg')
			g('set output "rms-prof-num.jpg"')
			g.xlabel('RMS')
			g.ylabel('PROFUNDIDAD')
			g.title('RMS vs PROFUNDIDAD')
			g('set xtics auto')
			g('set zlabel "Numero de sismos" rotate parallel ')
			g('set xrange [0:1.5]')
			g('set yrange [0:200]')
			#g('set zrange [:]')
			if Var73.get() ==1:
				g('set xrange ['+v79.get()+':'+v85.get()+']')
				g('set yrange ['+v91.get()+':'+v97.get()+']')
				g('set zrange ['+v103.get()+':'+v109.get()+']')
			g('set grid ytics')
			g('set grid xtics')
			g('set contour base')
			g('set view 60,60')  
			g('set cntrparam bspline')
			g('set cntrparam order 10')
			g('set cntrparam levels auto 10')
			g('unset pm3d')
			g('set pm3d at b')
			g('set palette model RGB rgbformulae 7,5,15')
			g.splot(Gnuplot.GridData(sum_profM,vec_rms,vec_prof, binary=0, inline=0, with_='lines'))			
			#raw_input('Please press return to continue...\n')
		############################Grafica Magnitud-PROFUNDIDAD-#Sismos#####
		if Var62.get() ==1:
			g('set autoscale')
			g.xlabel('MAGNITUD Ml')
			g('set terminal jpeg')
			g('set output "mag-prof-num.jpg"')
			g.ylabel('PROFUNDIDAD')
			g.title('Magnitud vs Profundidad')
			g('set xtics auto')
			g('set zlabel "Numero de sismos" rotate parallel ')
			g('set xrange [0:3.5]')
			g('set yrange [0:200]')
			#g('set zrange [:]')
			if Var74.get() ==1:
				g('set xrange ['+v80.get()+':'+v86.get()+']')
				g('set yrange ['+v92.get()+':'+v98.get()+']')
				g('set zrange ['+v104.get()+':'+v110.get()+']')
			g('set grid ytics')
			g('set grid xtics')
			g('set contour base')
			g('set view 60,60')  
			g('set cntrparam bspline')
			g('set cntrparam order 10')
			g('set cntrparam levels auto 10')
			g('unset pm3d')
			g('set pm3d at b')
			g('set palette model RGB rgbformulae 7,5,15')
			g.splot(Gnuplot.GridData(sum_profM2,vec_mag,vec_prof, binary=0, inline=0, with_='lines'))
			#raw_input('Please press return to continue...\n')

		############################Grafica RMS-MAGNITUD-#Sismos#############
		if Var63.get() ==1:
			g('set autoscale')
			g.xlabel('RMS')
			g('set terminal jpeg')
			g('set output "rms-mag-num.jpg"')
			g.ylabel('MAGNITUD Ml')
			g.title('RMS vs Magnitud')
			g('set xtics auto')
			g('set zlabel "Numero de sismos" rotate parallel ')
			g('set xrange [0:1.5]')
			g('set yrange [0:3.5]')
			#g('set zrange [:]')
			if Var74.get() ==1:
				g('set xrange ['+v81.get()+':'+v87.get()+']')
				g('set yrange ['+v93.get()+':'+v99.get()+']')
				g('set zrange ['+v105.get()+':'+v111.get()+']')
			g('set grid ytics')
			g('set grid xtics')
			g('set contour base')
			g('set view 60,60')  
			g('set cntrparam bspline')
			g('set cntrparam order 10')
			g('set cntrparam levels auto 10')
			g('unset pm3d')
			g('set pm3d at b')
			g('set palette model RGB rgbformulae 7,5,15')
			g.splot(Gnuplot.GridData(sum_magM,vec_rms,vec_mag, binary=0, inline=0, with_='lines'))
			#raw_input('Please press return to continue...\n')
		
		archivo4.close()
		

		############################Grafica Sismos-Tiempo###################

#######################hace el report2################################
		os.system("./expect_report2")
		#######################borra la primera linea del report################################	
		report2=glob("/home/camilo/read_select/codigo/report.out")
		archivo5=open(report2[0],"r")
		lines=archivo5.readlines()
		contenido5 = ''
		for line in lines:
			if 'Year' in line:
				contenido5 += ''
			else:
				contenido5 += line
		archivo5.close()
		archivo5=open(report2[0],"w")
		archivo5.write(contenido5)
		archivo5.close()
	
	

		dat1=glob("appear_mes.dat")
		archivo1=open(dat1[0],"r")
		contenido1 = ''


		report3=glob("report.out")
		archivo6=open(report3[0],"r")
		lines=archivo6.readlines()


		vec_years = numpy.arange(1993,2016,1)
		#print vec_years
		count_mes=numpy.zeros((23, 12))
		#print count_mes
		meses=numpy.arange(1,14,1)
		size = numpy.zeros((2))

		year = []
		mes = []
		dia = []
		appear_year = []
		appear_count_mes = []
		appear_count_mes2 = []
		appear_mes = []
		appear_mes2 = []

		for line in lines:
			campo = line.split(' ')
			year.append(int(line[1:5]))
			mes.append(int(line[6:8]))
			dia.append(int(line[8:10]))
		#print year.buffer_info()
		#print mes.buffer_info()
		#print dia.buffer_info()
		#print len (year)
		for i in range (0, len(mes)):
			for y in range (0, 23):
				if year[i]==vec_years[y]:
					#appear_year.append(year[i])
					for j in range (0, 13):
						if mes[i]-1==int(j):
							count_mes[y,j] += 1 
							if mes[i] != mes[i-1]:
								appear_mes.append(' '+str(year[i])+'-'+str(mes[i])+' ')
							if i == 0:
								appear_mes.append(' '+str(year[i])+'-'+str(mes[i])+' ')
		size=count_mes.shape
		for i in range (0, size[0]):
			for j in range (0, size[1]):
				if count_mes[i,j] != 0:
					appear_count_mes.append(count_mes[i,j])
		for i in range (0, len(appear_count_mes)):
			appear_count_mes2 = str(appear_count_mes[i])
			appear_mes2 = str(appear_mes[i])
			print appear_count_mes2 
			contenido1 += ''+appear_count_mes2+' '+appear_mes2+'\n'

		print appear_count_mes
		print appear_mes
		print len(appear_count_mes)
		print len(meses)


		archivo1.close()
		archivo1=open(dat1[0],"w")
		archivo1.write(contenido1)
		archivo1.close()
		
		g('set ylabel "Numero de sismos" rotate parallel ')
		g('set xlabel "Tiempo en Meses"')
		g('set autoscale')
		g('set terminal jpeg')
		g('unset pm3d')
		g('set output "sismos_vs_tiempo.jpg"')
		g('unset key')
		g('set boxwidth 0.9 relative')
		g('set xtics rotate')
		g('set style fill solid 1')
		g('plot "appear_mes.dat" u 1:xticlabels(2) with boxes')
		#raw_input('Please press return to continue...\n')

		archivo6.close()	

		############################ Menu Graficas ##########################
	def ver_graficas():
		if Var52.get() ==1:
			os.system("display late.jpg")
		if Var53.get() ==1:
			os.system("display lone.jpg")
		if Var54.get() ==1:
			os.system("display profe.jpg")
		if Var55.get() ==1:
			os.system("display profb.jpg")
		if Var56.get() ==1:
			os.system("display rmsb.jpg")
		if Var57.get() ==1:
			os.system("display magb.jpg")
			
			
		if Var61.get() ==1:
			os.system("display rms-prof-num.jpg")
		if Var62.get() ==1:
			os.system("display mag-prof-num.jpg")
		if Var63.get() ==1:
			os.system("display rms-mag-num.jpg")
			
		os.system("display sismos_vs_tiempo.jpg")
		
	self.menu=Button(self.frameFour, text='Hacer Graficas', command=codigo_graficas)
	self.menu.grid(row=19, column=0, padx=(0,10))
	self.menu=Button(self.frameFour, text='Ver Graficas', command=ver_graficas)
	self.menu.grid(row=19, column=1, padx=(0,10))
	self.menu=Button(self.frameFour, text='Menu', command=self.menu_inicial)
	self.menu.grid(row=19, column=2, padx=(0,10))
	self.salir=Button(self.frameFour, text='Salir', command=self.quit)
	self.salir.grid(row=19, column=8, padx=(0,10))
	
###############################PYTHON##########################################
    def ir_graficas2(self):
    	os.system("./histo_graf.py")


if __name__ == "__main__":
    	root = Tk()
    	aplicacion = Planificador(root)
	root.mainloop()
