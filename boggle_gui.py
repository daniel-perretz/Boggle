import tkinter as tki
from typing import Callable, Dict, List, Any

NUM_COLS = 4
NUM_ROWS = 4


class BoggleGui:
    def __init__(self):
        self.root = tki.Tk()
        self.root.resizable(False, False)
        self.upper_frame = tki.Frame()
        self.lower_frame = tki.Frame()
        self.mid_frame = tki.Frame()
        self.title = tki.Label(text="Boggle" , master=self.lower_frame)
        self.start_button = tki.Button(text="START ", bg="red", fg="white",master=self.upper_frame)
        self.buttons_list = []
        for i in range(NUM_COLS):
            for j in range(NUM_ROWS):
                frame = tki.Frame(
                    master=self.mid_frame,
                    relief=tki.RAISED,
                )

                frame.grid(row=i, column=j)
                button = tki.Button(master=frame,text ='',padx=30, pady=30,relief=tki.RIDGE)
                self.buttons_list.append(button)
                button.grid(padx=0, pady=0)
        self.pack()

    def set_button_text(self, board):
        count = 0
        for row in range(len(board)):
            for col in range(len(board[row])):
                button = self.buttons_list[count]
                button.configure(height = 1, width = 1 ,text= board[row][col])
                count += 1

    def pack(self):
        self.upper_frame.pack(side=tki.TOP )
        self.mid_frame.pack(padx=40 , pady=0)
        self.lower_frame.pack(side=tki.BOTTOM)
        self.start_button.pack()
        self.title.pack()


    def run(self) -> None:
        self.root.mainloop()


if __name__ == "__main__":
    cg = BoggleGui()
    cg.run()
    # init_game()
