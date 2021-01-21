import tkinter as tki
from tkinter import messagebox
from typing import Callable, Dict, Tuple

# game preferences:
HIGHSCORE_INTRO = "HIGHSCORE: "
TEXT_COLOR = "white"
GAME_LENGTH = 180  # in seconds
NUM_COLS = 4
NUM_ROWS = 4
ASK_FOR_BREAK_INTERVAL = 3  # ask user to take a break after # games

# texts:
START_BTN_MSG = 'Start Game'
MID_GAME_MSG = "Game Started..."
GAME_OVER_MSG = "TIME'S UP!"
PLAY_AGAIN_MSG = "Play again?"
SUBMIT_BTN_MSG = 'Submit'
BREAK_PROMPT_TITLE = "Time for a break?"

# labels' intros:
SCORE_INTRO = "SCORE: "
CUR_WORD_INTRO = " CURRENT WORD: "
FOUND_WORDS_INTRO = "FOUND WORDS: "

# design:
TITLE = "~ Boggle ~  by Daniel and Tamir"
FONT = 'Courier'
BG_COLOR = "#482B4F"  # other choices: 54325D, #331E38", "light slate blue"
PRESSED_BUTTON = "chocolate1"  # other choice: #e05215
LABEL_COLOR = "#F4E8C1"  # other choice: "navajo white"
BUTTON_COLOR = "sandy brown"  # other choice: #EF8354
LOGO_PATH = "boggle_logo.png"
GAME_START_PATH = "GAME_START.png"
GAME_STARTED_PATH = "GAME_STARTED.png"
PLAY_AGAIN_PATH = "PLAY_AGAIN!.png"
SUBMIT_PATH = "SUBMIT.png"
PRESSED_SUBMIT_PATH = "PRESSED_SUMBIT.png"


# MediumPurple1 - normal button background
# BlueViolet - Pressed
# tan1,peach puff,sandy brown
# Turquoise1 / CadeBlue2 / PaleTurquoise1 - general background

class BoggleGui:
    """
    This class is responsible for the graphic user interface of the game, and
    their basic visual processes
    """

    def __init__(self):
        # initialize gui:
        self.root = tki.Tk()
        self.root.resizable(False, False)
        self.root.title(TITLE)
        self.root.configure(bg=BG_COLOR)
        self.mid_frame = tki.Frame(padx=40, pady=30, bg=BG_COLOR)

        # set gui attributes:
        self.is_counting: bool = False
        self.games_played: int = 0
        self.highscore: int = 0
        self.buttons_list = []
        self.buttons_loc_letter_dict: Dict = {}
        self.current_path: list = []
        self.coor_letter_dict: Dict[Tuple[int, int], str] = {}
        self.found_words = []
        self.took_a_break = False

        # load images:
        self.logo = tki.PhotoImage(file=LOGO_PATH)
        self.ph_start = tki.PhotoImage(file=GAME_START_PATH)
        self.ph_game_started = tki.PhotoImage(file=GAME_STARTED_PATH)
        self.ph_play_again = tki.PhotoImage(file=PLAY_AGAIN_PATH)
        self.ph_submit = tki.PhotoImage(file=SUBMIT_PATH)
        self.ph_pressed_submit = tki.PhotoImage(file=PRESSED_SUBMIT_PATH)

        # resize images:
        self.bn_start = self.ph_start.subsample(5, 5)
        self.bn_game_started = self.ph_game_started.subsample(6, 6)
        self.bn_play_again = self.ph_play_again.subsample(5, 5)
        self.bh_submit = self.ph_submit.subsample(9, 9)
        self.bh_pressed_submit = self.ph_pressed_submit.subsample(9, 9)

        # show labels:
        self.found_word_label = tki.Label(text=FOUND_WORDS_INTRO,
                                          relief=tki.GROOVE,
                                          font=(FONT, 15), bg=LABEL_COLOR)
        self.current_word_label = tki.Label \
            (text=CUR_WORD_INTRO, pady=5, font=(FONT, 13), bg=BG_COLOR,
             fg=TEXT_COLOR)
        self.count_label = tki.Label(font=(FONT, 40), bg=BG_COLOR,
                                     fg=TEXT_COLOR)
        self.show_formatted_time(GAME_LENGTH)
        self.score_label = tki.Label(padx=10, pady=10,
                                     text=f"{SCORE_INTRO}0   "
                                          f"{HIGHSCORE_INTRO}{self.highscore}",
                                     relief=tki.RIDGE, font=(FONT, 20),
                                     bg=LABEL_COLOR)
        self.logo_label = tki.Label(image=self.logo, bg=BG_COLOR)
        self.display_word_label = tki.Label \
            (bg=BG_COLOR, font=(FONT, 13, "bold"), fg=TEXT_COLOR)
        # show buttons:
        self.start_button = tki.Button(
            self.root, text=START_BTN_MSG, command=self.game_countdown,
            image=self.bn_start, bg=BG_COLOR)
        self.submit_button = tki.Button(text=SUBMIT_BTN_MSG, bg=BG_COLOR,
                                        image=self.bh_submit)
        self.create_and_place_buttons()

        self.pack()

    def create_and_place_buttons(self):
        """ This function creates buttons and places them in a grid
        note: it does not activates an action when they are pressed"""
        for i in range(NUM_COLS):
            for j in range(NUM_ROWS):
                frame = tki.Frame(
                    master=self.mid_frame,
                    relief=tki.RAISED,
                )
                frame.grid(row=i, column=j)
                button = tki.Button(master=frame, text='?', padx=31, pady=31,
                                    relief=tki.RAISED, bg=BUTTON_COLOR)
                self.buttons_list.append(button)
                button.grid(padx=0, pady=0)

    def pack(self):
        """this function organizes widgets frames and
         labels in blocks, before finally placing them in the parent window"""
        self.logo_label.grid()
        self.count_label.grid()
        self.start_button.grid()
        self.mid_frame.grid(padx=40, pady=50)
        self.current_word_label.place(relx=0.150, rely=0.860, anchor='sw')
        self.submit_button.place(relx=0.82, rely=0.880, anchor='se')
        self.score_label.place(relx=0.5, rely=0.310, anchor="n")
        self.found_word_label.grid(row=4, pady=10, padx=10)
        self.display_word_label.place(relx=0.150, rely=0.880, anchor='sw')
        white_space = tki.Label(bg=BG_COLOR)
        white_space.grid(row=5)

    def set_submit_button_command(self, func: Callable):
        """this function uses the configure method to
         make for the method to be
        called
        when the button is clicked. """
        self.submit_button.configure(command=func)

    def set_start_button_command(self, func: Callable):
        self.start_button.configure(command=func)

    def set_label_score(self, points):
        self.score_label.configure(text=f"{SCORE_INTRO}{points}   "
                                        f"{HIGHSCORE_INTRO}{self.highscore}")

    def set_game_started_btn(self):
        self.start_button.configure(image=self.bn_game_started)

    def set_play_again_btn(self):
        self.start_button.configure(image=self.bn_play_again)

    def revert_submit(self):
        self.submit_button.configure(image=self.bh_submit)

    def change_to_pressed(self):
        """ Changes the submit button's image to look like it is 'pressed'"""
        self.submit_button["image"] = self.bh_pressed_submit
        self.root.after(200, self.revert_submit)

    def set_current_word_label(self):
        """ Calculates which letters to show, based on the coordinates
        chosen"""
        output = ""
        for i, coor in enumerate(self.coor_letter_dict):
            output += self.coor_letter_dict[coor]
        self.display_word_label.configure(text=f"{output}")

    def set_buttons_text(self, board):
        """ Iterates through all the letters' buttons and sets their text
         according to a given board"""
        count = 0
        for row in range(len(board)):
            for col in range(len(board[row])):
                button = self.buttons_list[count]
                letter = board[row][col]
                self.buttons_loc_letter_dict[button] = ((row, col), letter)
                button.configure(height=1, width=1, text=letter)
                count += 1

    def create_button_command(self, coor, button) -> Callable:
        """ Creates a suitable command for each button according to its
        letter and returns it if the game should be running. The command also
         takes care of the button's normal / pressed color"""

        def cmd():
            if not self.is_counting:
                return
            if coor not in self.current_path:
                button["bg"] = PRESSED_BUTTON
                self.current_path.append(coor)
                letter: str = self.buttons_loc_letter_dict[button][1]
                self.coor_letter_dict[coor] = letter
            else:
                button["bg"] = BUTTON_COLOR

                self.current_path.remove(coor)
                del self.coor_letter_dict[coor]
            self.set_current_word_label()

        return cmd

    def initiate_buttons_actions(self):
        """ Sets each letter button with its appropriate action"""
        for button in self.buttons_list:
            coor = self.buttons_loc_letter_dict[button][0]
            func = self.create_button_command(coor, button)
            button.configure(command=func)

    def show_found_word(self, word):
        """ Formats the found word's list and shows it in the appropriate
        label"""
        self.found_words.append(word)
        output = FOUND_WORDS_INTRO
        for i in range(len(self.found_words)):
            output += f" {self.found_words[i]}"
            if i != 0 and i % 15 == 0:
                output += "\n"
            if i != (len(self.found_words) - 1):
                output += ","
            else:
                output += "."
        self.found_word_label.configure(text=output)

    def show_formatted_time(self, time):
        """ Formats a time in second to minutes:seconds and shows it in the
        appropriate label"""
        min, sec = divmod(time, 60)
        if sec // 10 == 0 and min // 10 == 0:
            self.count_label.configure(text=f"0{min}:0{sec}")
        elif sec // 10 == 0:
            self.count_label.configure(text=f"{min}:0{sec}")
        elif min // 10 == 0:
            self.count_label.configure(text=f"0{min}:{sec}")
        else:
            self.count_label.configure(text=f"{min}:{sec}")

    def update_highscore(self, score):
        """Updates the highscore if necessary"""
        if score > self.highscore:
            self.highscore = score

    def reset_buttons_color(self):
        """ Changes all buttons to their default color"""
        for button in self.buttons_list:
            button["bg"] = BUTTON_COLOR

    def game_countdown(self):
        """Starts the countdown in the appropriate game time"""
        self.is_counting = True
        self.countdown(GAME_LENGTH)

    def countdown(self, time):
        """Counts down to a given time in seconds and updates the count label
        with an appropriate message telling that it is over. Also updates
        the number of games played"""
        if time <= 0:
            self.is_counting = False
            if not self.is_counting:
                self.count_label.configure(text=GAME_OVER_MSG)
            self.set_play_again_btn()
            self.games_played += 1
            return
        else:
            self.show_formatted_time(time)
            self.root.after(1000, self.countdown, (time - 1))

    def ask_for_a_break(self) -> bool:
        """Asks the user to take a break after a certain amount of games.
        After he takes a break, he would not be asked to take another one,
        but if he refuses the message will pop up after the same number of
        games
        :returns a bool stating whether user took a break or not"""
        break_prompt_msg = f"Games are fun, but can be addictive." \
                           f" You already played" \
                           f" {self.games_played} games, would you like to " \
                           "take a break? \n" \
                           "Don't worry, Boggle will save your score and" \
                           " wait for you here when you get back!"
        if self.took_a_break is False and self.games_played != 0 and \
                self.games_played % ASK_FOR_BREAK_INTERVAL == 0:
            if messagebox.askquestion(BREAK_PROMPT_TITLE, break_prompt_msg) \
                    == "yes":
                self.took_a_break = True
                return True
            else:
                return False

    def reset_current_path_and_word(self):
        """Empties the current path and word saved"""
        self.current_path = []
        self.coor_letter_dict = {}
        self.set_current_word_label()

    def reset(self):
        """Resets the entire GUI, not including highscore and games played"""
        self.reset_current_path_and_word()
        self.found_words = []
        self.found_word_label.configure(text=FOUND_WORDS_INTRO)

    def run(self) -> None:
        """Runs the Graphic User Interface"""
        self.root.mainloop()

