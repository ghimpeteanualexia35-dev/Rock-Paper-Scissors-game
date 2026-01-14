from gui import RPSApp
import tkinter as tk

def main():
    root = tk.Tk() #creează fereastra
    app = RPSApp(root) #pune aplicatia in fereastra
    root.mainloop() #porneste aplicatia

if __name__ == "__main__":
    main()
