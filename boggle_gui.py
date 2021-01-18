import tkinter as tki
from typing import Callable, Dict, Tuple, List, Any

GAME_LENGTH = 180  # in seconds
NUM_COLS = 4
NUM_ROWS = 4
MAIN_COLOR = "grey"
LOGO_PATH = "boggle_logo.png"


class BoggleGui:
    def __init__(self):
        self.root = tki.Tk()
        self.root.resizable(False, False)

        # self.lower_frame = tki.Frame()
        self.mid_frame = tki.Frame()

        self.found_word_label = tki.Label(text="Word list: ", relief=tki.GROOVE, font=('helvetica', 15))
        self.current_word_label = tki.Label(text=" Current Word: ", relief=tki.GROOVE)
        self.count_label = tki.Label(relief=tki.RIDGE,
                                     font=('helvetica', 40))
        self.logo = tki.PhotoImage(file=LOGO_PATH)
        self.logo_label = tki.Label(image=self.logo)
        self.start_button = tki.Button(
            self.root, text='Start Game', command=self.game_countdown,
            padx=37, pady=20, relief=tki.RIDGE)
        self.submit_button = tki.Button(text='Submit',
                                        padx=10, pady=10, relief=tki.RIDGE)
        self.score_label = tki.Label(text="Score: 0", relief=tki.RIDGE)

        self.is_counting: bool = False
        self.buttons_list = []
        self.buttons_loc_letter_dict: Dict = {}
        self.current_path: list = []
        self.current_word: List[str] = []
        self.found_words = []

        for i in range(NUM_COLS):
            for j in range(NUM_ROWS):
                frame = tki.Frame(
                    master=self.mid_frame,
                    relief=tki.RAISED,
                )
                frame.grid(row=i, column=j)
                button = tki.Button(master=frame, text='?', padx=30, pady=30,
                                    relief=tki.RIDGE, bg=MAIN_COLOR)
                self.buttons_list.append(button)
                button.grid(padx=0, pady=0)
        self.pack()

    def pack(self):
        self.logo_label.pack(side=tki.TOP)
        self.count_label.pack(side=tki.TOP)
        self.start_button.pack(side=tki.TOP)
        self.mid_frame.pack(padx=40, pady=0)
        self.current_word_label.pack()
        self.submit_button.pack()
        self.score_label.pack(padx=10, pady=10)
        self.found_word_label.pack(pady=10)

    def set_submit_button_command(self, func: Callable):
        self.submit_button.configure(command=func)

    def set_start_button_command(self, func: Callable):
        self.start_button.configure(command=func)

    def set_current_word_label(self):
        output = ""
        for letter in self.current_word:
            output += letter
        self.current_word_label.configure(text =f" Current Word: {output}")


    def set_buttons_text(self, board):
        count = 0
        for row in range(len(board)):
            for col in range(len(board[row])):
                button = self.buttons_list[count]
                letter = board[row][col]
                self.buttons_loc_letter_dict[button] = ((row, col), letter)
                button.configure(height=1, width=1, text=letter)
                count += 1

    def show_found_word(self, word):
        self.found_words.append(word)
        output = " Found words: "
        for i in range(len(self.found_words)):
            output += f" {self.found_words[i]}"
            if i != (len(self.found_words) - 1):
                output += ","
            else:
                output += "."
        self.found_word_label.configure(text=output)

    def create_button_command(self, coor, button) -> Callable:
        def cmd():
            if coor not in self.current_path:
                self.current_path.append(coor)
                letter: str = self.buttons_loc_letter_dict[button][1]
                self.current_word.append(letter)
            else:
                self.current_path.remove(coor)
                self.current_word.remove(
                    self.buttons_loc_letter_dict[button][1])  # the letter
            self.set_current_word_label()
            button["bg"] = "red"

        return cmd

    def initiate_buttons_actions(self):
        for button in self.buttons_list:
            coor = self.buttons_loc_letter_dict[button][0]
            func = self.create_button_command(coor, button)
            button.configure(command=func)

    def set_label_score(self, points):
        self.score_label.configure(text=f"score: {points}")

    def countdown(self, t):
        if t <= 0:
            self.is_counting = False
            if not self.is_counting:
                self.count_label.configure(text="time's up!")
            self.start_button.configure(text="Play again?")
        else:
            m, s = divmod(t, 60)
            if s // 10 == 0 and m // 10 == 0:
                self.count_label.configure(text=f"0{m}:0{s}")
            elif s // 10 == 0:
                self.count_label.configure(text=f"{m}:0{s}")
            elif m // 10 == 0:
                self.count_label.configure(text=f"0{m}:{s}")
            else:
                self.count_label.configure(text=f"{m}:{s}")

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
