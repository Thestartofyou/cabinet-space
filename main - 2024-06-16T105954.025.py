import tkinter as tk
from tkinter import colorchooser

class CabinetCountertopWidget:
    def __init__(self, root):
        self.root = root
        self.root.title("Custom Cabinet and Countertop Visualizer")
        
        self.cabinet_color = "#ffffff"
        self.countertop_color = "#ffffff"
        
        self.canvas = tk.Canvas(root, width=400, height=300)
        self.canvas.pack()
        
        self.cabinet_button = tk.Button(root, text="Select Cabinet Color", command=self.choose_cabinet_color)
        self.cabinet_button.pack()
        
        self.countertop_button = tk.Button(root, text="Select Countertop Color", command=self.choose_countertop_color)
        self.countertop_button.pack()
        
        self.update_visualization()

    def choose_cabinet_color(self):
        color = colorchooser.askcolor(title="Choose Cabinet Color")
        if color:
            self.cabinet_color = color[1]
            self.update_visualization()

    def choose_countertop_color(self):
        color = colorchooser.askcolor(title="Choose Countertop Color")
        if color:
            self.countertop_color = color[1]
            self.update_visualization()
    
    def update_visualization(self):
        self.canvas.delete("all")
        self.canvas.create_rectangle(50, 50, 350, 150, fill=self.cabinet_color, outline="black")
        self.canvas.create_rectangle(50, 150, 350, 250, fill=self.countertop_color, outline="black")
        self.canvas.create_text(200, 25, text="Cabinet", font=("Arial", 14))
        self.canvas.create_text(200, 275, text="Countertop", font=("Arial", 14))

if __name__ == "__main__":
    root = tk.Tk()
    app = CabinetCountertopWidget(root)
    root.mainloop()
