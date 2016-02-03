import tkinter as tk
import random

__author__ = 'nattefrost'

class TkPlot:
    def __init__(self, data=[('Hemingway', 3), ('Shakespeare', 6), ('Simenon',12), ('Poe', 7)]):
        self.root = tk.Tk()
        self.data = data
        self.root.title('Biblio Stats')
        self.root.geometry("750x700")
        self.root.resizable(0,0)
        self.CAN_SIZE = (600, 450)
        self.list = tk.Listbox(self.root, height=10)
        self.list.pack()
        self.can = tk.Canvas(self.root, bg = 'white',width=600,height=450)
        self.can.pack()
        
        
        self.draw_grid()
        self.draw_chart(self.data)
        self.populate_listbox()
        self.root.mainloop()
    
    
    def populate_listbox(self):
        for item in self.data:
            self.list.insert(tk.END,"{} : {}".format(item[0],item[1]))
        
    def draw_grid(self):
        for i in range(30): 
            self.can.create_line(20 * i, 0, 20 * i, 450, fill="gray") # corresponds to canvas height
            self.can.create_line(0, 20 * i, 600, 20 * i, fill="gray") # corresponds to canvas width

    def draw_chart(self, data):
        """
        The data arg must be a list of tuples or it will fail
        example : [('Hemingway', 5), ('Shakespeare', 6)]
        """
        i = 0
        position = 20
        colours = ['yellow', 'darkblue','cyan','olivedrab','firebrick','dark green', '#E13500', '#FF284E', '#4EEC09', '#4C00B5', '#D1E39C']
        while i < len(data):
            chosen_colour = random.choice(colours)
            print(chosen_colour)
            colours.remove(chosen_colour)
            self.can.create_rectangle(position, self.CAN_SIZE[0], 
                                      position+20, self.CAN_SIZE[0]-((data[i][1]*20)+160), # Proper setup to scale on img
                                        fill=chosen_colour)
            
            position+=60
            i+=1
    
    


