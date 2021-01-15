import tkinter as tki
from typing import Callable, Dict, List, Any

NUM_COLS = 4
NUM_ROWS = 4


class BoggleGui:
    def __init__(self):
        self.root = tki.Tk()
        self.upper_frame = tki.Frame()
        self.lower_frame = tki.Frame()
        self.mid_frame = tki.Frame()
        self.title = tki.Label(text="Boggle" , master=self.lower_frame)
        self.start_button = tki.Button(text="START ", bg="red", fg="white",master=self.upper_frame)
        self.buttons_dic = []
        for i in range(NUM_COLS):
            for j in range(NUM_ROWS):
                frame = tki.Frame(
                    master=self.mid_frame,
                    relief=tki.RAISED,
                )
                frame.grid(row=i, column=j)
                button = tki.Button(master=frame)
                self.buttons_dic.append(button)
                button.pack()
        self.pack()

    def set_button_text(self, board):
        count = 0
        for row in board:
            for col in row:
                self.buttons_dic[count]["text"] = board[row][col]
                count += 1

    def pack(self):
        self.upper_frame.pack(side=tki.TOP)
        self.mid_frame.pack()
        self.lower_frame.pack(side=tki.BOTTOM)
        self.start_button.pack()
        self.title.pack()


    def create_buttons(self):
        for i in range(NUM_COLS):
            tki.Grid.columnconfigure(self._lower_frame, i, weight=1)  # type: ignore

        for i in range(NUM_ROWS):
            tki.Grid.rowconfigure(self._lower_frame, i, weight=1)

    def run(self) -> None:
        self.root.mainloop()


if __name__ == "__main__":
    cg = BoggleGui()
    cg.run()
