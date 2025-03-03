import tkinter as tk


racine = tk.Tk() 
cercle = tk.Button(racine, text='cercle')
cercle.grid(row= 1, column= 0)
carré = tk.Button(racine, text='carré')
carré.grid(row= 2, column = 0)
croix = tk.Button(racine, text='croix')
croix.grid(row = 3, column = 0)
couleur = tk.Button(racine, text='choisir une couleur')
couleur.grid(row=0, column = 1)
can = tk.Canvas(racine, background="black", width= 800, height= 600)
can.grid(row=1, column=1, rowspan=3)
racine.mainloop()


