import firecall
from tkinter import *
from tkinter import messagebox
from ClasseMapa import *



my_firebase = firecall.Firebase("https://resplendent-inferno-7886.firebaseio.com/")

def SubmmitScore (nome,pontuação, turnos):
    name = "edufm"
    dicio = {"Info": [pontuação , turnos]}
    a = True
    records = eval(my_firebase.get_sync(point="/records"))
    
    lista = []
    for i in records:
        lista.append(i)
        print(lista)
    if "edufm" in lista:
        a = False
    if a == True:
        my_firebase.put_sync(point="/records/edufm" , data = dicio)
        ConstruirRank(name,pontuação,turnos)
    if a == False:
        messagebox.showinfo("Attention", "This name already exists!")
        
def ConstruirRank (nome,pontuação,turnos):
    records = eval(my_firebase.get_sync(point="/records"))
    ranquear = []
    for i in records:
        ranquear.append((i,records[i]['Info'][0],records[i]['Info'][1]))
    wmax = 0
    tmax = 100
    primeiro = ("hugo",1,0)
    for i in range(len(ranquear)):
        if ranquear[i][1] >= wmax and ranquear[i][2] < tmax :
            wmax = ranquear[i][1]
            tmax=  ranquear[i][2]
            primeiro = (ranquear[i][0],ranquear[i][1],ranquear[i][2])
            print(primeiro)
    mostrardados = Tk()
    mostrardados.config(bg="black")
    mostrardados.title("Magic Trap Scores")
    recordemundial = Label(mostrardados)
    recordemundial.config(text=" Recorde mundial : {0} : {1} waves : {2} turns".format(primeiro[0],primeiro[1],primeiro[2]) ,font = ("Impact",20),bg="black",foreground="red")
    recordemundial.grid(row=0,column =0)
    seuscore= Label(mostrardados)
    seuscore.config(text= "Seu Score : {0} : {1} waves : {2} turns".format(nome,pontuação,turnos),font = ("Impact",20),bg="black",foreground="red")
    seuscore.grid(row=1,column=0)
    
    mostrardados.mainloop()
   
    
    
    
            
            

        

#a = my_firebase.get_sync(point="/records/{0}".format(dicio["Nome"]), data = dicio)
