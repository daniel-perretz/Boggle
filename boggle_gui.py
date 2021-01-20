import tkinter as tki
from typing import Callable, Dict, Tuple, List, Any

# game preferences:
GAME_LENGTH = 180  # in seconds
NUM_COLS = 4
NUM_ROWS = 4

# buttons' texts:
START_BTN_MSG = 'Start Game'
MID_GAME_MSG = "Game Started..."
GAME_OVER_MSG = "time's up!"
PLAY_AGAIN_MSG = "Play again?"
SUBMIT_BTN_MSG = 'Submit'

# labels' intros:
SCORE_INTRO = "Score: "
CUR_WORD_INTRO = " Current Word: "
FOUND_WORDS_INTRO = "Word list: "

# design:
FONT = 'helvetica'
MAIN_COLOR = "grey"
LOGO_PATH = "boggle_logo.png"

class BoggleGui:
    def __init__(self):
        self.root = tki.Tk()
        self.root.resizable(False, False)

        # self.lower_frame = tki.Frame()
        self.mid_frame = tki.Frame(padx=40, pady=30)

        self.found_word_label = tki.Label(text=FOUND_WORDS_INTRO,
                                          relief=tki.GROOVE,
                                          font=(FONT, 15))
        self.current_word_label = tki.Label(text=CUR_WORD_INTRO,
                                            relief=tki.GROOVE, padx=10,
                                            pady=10)
        self.count_label = tki.Label(font=(FONT, 40))
        self.show_formatted_time(GAME_LENGTH)
        self.logo = tki.PhotoImage(file=LOGO_PATH)
        self.logo_label = tki.Label(image=self.logo)
        self.start_button = tki.Button(
            self.root, text=START_BTN_MSG, command=self.game_countdown,
            padx=37, pady=20, relief=tki.RIDGE)
        self.submit_button = tki.Button(text=SUBMIT_BTN_MSG,
                                        padx=10, pady=10, relief=tki.RIDGE)
        self.score_label = tki.Label(padx=32, pady=10, text=f"{SCORE_INTRO}0",
                                     relief=tki.RIDGE,
                                     font=(FONT, 15))

        self.is_counting: bool = False
        self.games_played: int = 0
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
        self.logo_label.grid()
        self.count_label.grid()
        self.start_button.grid()
        self.mid_frame.grid(padx=40, pady=50)
        self.current_word_label.place(relx=0.176, rely=0.910, anchor='sw')
        self.submit_button.place(relx=0.83, rely=0.9155, anchor='se')
        self.score_label.place(relx=0.5, rely=0.335, anchor="n")
        self.found_word_label.grid()

    def set_submit_button_command(self, func: Callable):
        self.submit_button.configure(command=func)

    def set_start_button_command(self, func: Callable):
        self.start_button.configure(command=func)

    def set_current_word_label(self):
        output = ""
        for letter in self.current_word:
            output += letter
        self.current_word_label.configure(text=f"{CUR_WORD_INTRO}{output}")

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
        output = FOUND_WORDS_INTRO
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
                button["bg"] = "red"
                self.current_path.append(coor)
                letter: str = self.buttons_loc_letter_dict[button][1]
                self.current_word.append(letter)
            else:
                button["bg"] = MAIN_COLOR

                self.current_path.remove(coor)
                self.current_word.remove(
                    self.buttons_loc_letter_dict[button][1])  # the letter
            self.set_current_word_label()

        return cmd

    def initiate_buttons_actions(self):
        for button in self.buttons_list:
            coor = self.buttons_loc_letter_dict[button][0]
            func = self.create_button_command(coor, button)
            button.configure(command=func)

    def set_label_score(self, points):
        self.score_label.configure(text=f"{SCORE_INTRO}{points}")

    def game_countdown(self):
        self.is_counting = True
        self.countdown(GAME_LENGTH)
        self.start_button["text"] = MID_GAME_MSG

    def countdown(self, time):
        if time <= 0:
            self.is_counting = False
            if not self.is_counting:
                self.count_label.configure(text=GAME_OVER_MSG)
            self.start_button.configure(text=PLAY_AGAIN_MSG)
            self.games_played += 1
            return
        else:
            self.show_formatted_time(time)

        self.root.after(1000, self.countdown, (time - 1))

    def show_formatted_time(self, time):
        min, sec = divmod(time, 60)
        if sec // 10 == 0 and min // 10 == 0:
            self.count_label.configure(text=f"0{min}:0{sec}")
        elif sec // 10 == 0:
            self.count_label.configure(text=f"{min}:0{sec}")
        elif min // 10 == 0:
            self.count_label.configure(text=f"0{min}:{sec}")
        else:
            self.count_label.configure(text=f"{min}:{sec}")

    def reset(self):
        self.current_word = []
        self.found_words = []
        self.current_path = []

    def run(self) -> None:
        self.root.mainloop()


if __name__ == "__main__":
    cg = BoggleGui()
    cg.run()
    # init_game()
