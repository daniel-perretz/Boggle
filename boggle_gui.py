import tkinter as tki
from typing import Callable, Dict, List, Any

class BoggleGui:
    def __init__(self):
        self.root = tki.Tk()
        self.title = tki.Label(text="Boggle")
        self.start_button = tki.Button(text="START ", bg="black", fg="white")
        self.start_button.pack()
        self.title.pack()


    def run(self) -> None:
        self.root.mainloop()

if __name__ == "__main__":
    cg = BoggleGui()
    cg.run()

