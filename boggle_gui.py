import tkinter as tki
from typing import Callable, Dict, List, Any

GAME_LENGTH = 180  # in seconds

NUM_COLS = 4
NUM_ROWS = 4


class BoggleGui:
    def __init__(self):
        self.root = tki.Tk()
        self.root.resizable(False, False)
        self.count_label = tki.Label(self.root, relief=tki.RIDGE,
                                     font=('helvetica', 40))
        self.mid_frame = tki.Frame()
        self.buttons_list = []
        self.buttons_loc_dict: Dict = {}
        self.current_path: list = []
        self.start_button = tki.Button(
            self.root, text='Start Game', command=self.game_countdown,
            padx=30, pady=30, relief=tki.RIDGE)
        self.submit_button = tki.Button(
            self.root, text='Submit',
            padx=10, pady=10, relief=tki.RIDGE)
        self.score_label = tki.Label(text="Score: 0", relief=tki.RIDGE)
        self.is_counting: bool = False

        for i in range(NUM_COLS):
            for j in range(NUM_ROWS):
                frame = tki.Frame(
                    master=self.mid_frame,
                    relief=tki.RAISED,
                )
                frame.grid(row=i, column=j)
                button = tki.Button(master=frame, text='?', padx=30, pady=30,
                                    relief=tki.RIDGE)
                self.buttons_list.append(button)
                button.grid(padx=0, pady=0)
        self.pack()

    def pack(self):
        self.count_label.pack(side=tki.TOP)
        self.start_button.pack(side=tki.TOP)
        self.mid_frame.pack(padx=40, pady=0)
        self.submit_button.pack()
        self.score_label.pack(padx=10, pady=20)

    def set_submit_button_command(self, func: Callable):
        self.submit_button.configure(command=func)

    def set_start_button_command(self, func: Callable):
        self.start_button.configure(command=func)

    def set_buttons_text(self, board):
        count = 0
        for row in range(len(board)):
            for col in range(len(board[row])):
                button = self.buttons_list[count]
                letter = board[row][col]
                self.buttons_loc_dict[button] = (row, col)
                button.configure(height=1, width=1, text=letter)
                count += 1

    def create_button_command(self, coor) -> Callable:
        def cmd():
            if coor not in self.current_path:
                self.current_path.append(coor)
            else:
                self.current_path.remove(coor)
        return cmd

    def initiate_buttons_actions(self):
        for button in self.buttons_list:
            coor = self.buttons_loc_dict[button]
            func = self.create_button_command(coor)
            button.configure(command=func)

    def set_label_score(self, points):
        self.score_label.configure(text=f"score: {points}")

    def countdown(self, t):
        if t <= 0:
            self.count_label.configure(text="time's up!")
            self.is_counting = False
        else:
            m, s = divmod(t, 60)
            self.count_label['text'] = f"{m}:{s}"

        self.root.after(1000, self.countdown, (t - 1))

    def game_countdown(self):
        self.is_counting = True
        self.countdown(GAME_LENGTH)
        self.start_button["text"] = "Game Started..."

    def run(self) -> None:
        self.root.mainloop()


if __name__ == "__main__":
    cg = BoggleGui()
    cg.count_label["text"] = "3:00"
    cg.run()
    # init_game()
