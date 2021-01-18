import tkinter as tki
from typing import Callable, Dict, List, Any
import time
import time as t

T = 180

NUM_COLS = 4
NUM_ROWS = 4


class BoggleGui:
    def __init__(self):
        self.root = tki.Tk()
        self.root.resizable(False, False)
        self.count_label = tki.Label(self.root,relief= tki.RIDGE,font= ('helvetica', 40))
        self.mid_frame = tki.Frame()
        self.score_label = tki.Label(text= "0",relief=tki.RIDGE)
        self.buttons_list = []
        self.start_button = tki.Button(self.root, text='Start Game',
                                       command=self.game_countdown ,padx=30, pady=30, relief=tki.RIDGE)

        for i in range(NUM_COLS):
            for j in range(NUM_ROWS):
                frame = tki.Frame(
                    master=self.mid_frame,
                    relief=tki.RAISED,
                )
                frame.grid(row=i, column=j)
                button = tki.Button(master=frame,text ='?',padx=30, pady=30,relief=tki.RIDGE)
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

    # def start_timer(self,timer):
    #     self.count_label.configure(text=f"{timer}")


    def show_label_score(self, points):
        self.score_label.configure(text=f"score: {points}")

    def pack(self):
        self.count_label.pack(side=tki.TOP )
        self.start_button.pack(side=tki.TOP)
        self.mid_frame.pack(padx=40 , pady=0)
        self.score_label.pack(padx=10 ,pady=50)

    def countdown(self,t):
        if t <= 0:
            self.count_label.configure(text="time's up!")
        else:
            m,s = divmod(t, 60)
            self.count_label['text'] = f"{m}:{s}"

        self.root.after(1000, self.countdown,(t-1))

    def game_countdown(self):
        self.countdown(T)

    def run(self) -> None:
        self.root.mainloop()


if __name__ == "__main__":
    cg = BoggleGui()
    cg.run()
    # init_game()
