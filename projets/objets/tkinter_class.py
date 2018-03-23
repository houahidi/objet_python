"""exercice tkinter"""

from tkinter import Canvas, Button, Tk, LEFT, BOTTOM
from random import randrange


class DrawWindow(Tk):
    """version de la popup en classe"""

    def __init__(self, x1=10, y1=190, x2=190, y2=10, height=200, width=200):
        """constructeur"""
        Tk.__init__(self)
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.coul = 'dark green'  # couleur de la ligne
        # creation des widgets "esclaves" :
        self.can1 = Canvas(self, bg='dark grey', height=height, width=width)
        self.bou1 = Button(self, text='Quitter', command=self.quit)
        self.bou2 = Button(self, text='Tracer une ligne', command=self.drawline)
        self.bou3 = Button(self, text='Autre couleur', command=self.changecolor)



    def display(self):
        """afficher la fenetre et ecouter pour les evenements"""
        self.can1.pack(side=LEFT)
        self.bou1.pack(side=BOTTOM)
        self.bou2.pack()
        self.bou3.pack()
        self.mainloop()  # demarrage du receptionnaire d'evenements


    def drawline(self):
        """Trace d'une ligne dans le canevas can1"""
        self.can1.create_line(self.x1,self.y1,self.x2,self.y2,width=2,fill=self.coul)
        # modification des coordonnees pour la ligne suivante :
        self.y2, self.y1 = self.y2+10, self.y1-10


    def changecolor(self):
        """Changement aleatoire de la couleur du trace"""
        pal = ['purple', 'cyan', 'maroon', 'green', 'red', 'blue', 'orange', 'yellow']
        c = randrange(8)# => genere un nombre aleatoire de 0 a 7
        self.coul = pal[c]


if __name__ == "__main__":

    POPUP = DrawWindow()
    POPUP.display()
    POPUP.destroy()
