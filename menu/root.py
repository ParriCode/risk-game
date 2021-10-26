import tkinter as tk
class RootMenu:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("RISK")
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        self.root.geometry("%dx%d" % (width, height))
        self.menu_start = menu_start(self.root)
        self.menu_start.show_menu()
        self.root.mainloop()
class menu_start:
    def __init__(self,root):
        self.my_frame = tk.Frame(root)
        one_player = tk.Button(self.my_frame,text = "Un jugador")
        multiplayer = tk.Button(self.my_frame,text = "multijugador")
        one_player.grid(row = 0,column = 0)
        multiplayer.grid(row = 1,column = 0)
    def hide_menu(self):
      self.my_frame.pack_forget()
    def show_menu(self):
      self.my_frame.pack()
class one_player_menu:
    pass
class multiplayer_menu:
    pass
