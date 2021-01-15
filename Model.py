from typing import Optional, List, Tuple
from ex12_utils import *
from boggle_board_randomizer import *

DICT_FILE_PATH = "boggle_dict.txt"


class Model:
    def __init__(self):
        self.start: bool = False
        self.board: List[List[str]] = randomize_board()
        self.__points: int = 0
        self.__words_dict: Dict[str, bool] = load_words_dict(DICT_FILE_PATH)
        self.__found_words: List[str] = []
        self.cur_path: Optional[List[Tuple[int]]] = []

    def handle_word(self) -> bool:
        word = is_valid_path(self.board, self.cur_path, self.__words_dict)
        if not word:
            return False
        else:
            if not self.__words_dict[word]:
                self.cur_path = []
                return False
            else:
                self.__words_dict[word] = False
                self.update_points(len(word))
                self.__found_words.append(word)
                self.cur_path = []
                return True

    def update_points(self, n) -> None:
        self.__points += n ** 2

    def restart(self):
        self.__points = 0
        self.board = randomize_board()
        self.__words_dict = load_words_dict(DICT_FILE_PATH)
        self.__found_words = []

    def get_points(self):
        return self.__points

    def get_found_words(self):
        return self.__found_words


import tkinter as tki
from datetime import datetime

H24_MODE = 24
H12_MODE = 12


class ClockGUI:

    def __init__(self, clock_model):
        self._clock_model = clock_model
        self._root = tki.Tk()
        self._clock_display = tki.Label(font=("Courier", 30), width=11)
        self._clock_display.pack()

        # just to demo binding on the label:
        self._clock_display.bind("<Button-1>", self._label_clicked)

        self._button = tki.Button(text="mode", font=("Courier", 30))
        self._button.pack()
        self._button["command"] = self._clock_model.switch_mode

    def _label_clicked(self, event):
        print(event.x, event.y)
        print(dir(event))

    def _animate(self):
        self._clock_display["text"] = self._clock_model.get_time_str()
        self._root.after(10, self._animate)

    def run(self):
        self._animate()
        self._root.mainloop()


class ClockModel:
    def __init__(self, mode=H24_MODE):
        self._mode = mode

    def switch_mode(self):
        if self._mode is H12_MODE:
            self._mode = H24_MODE
        else:
            self._mode = H12_MODE

    def get_time_str(self):
        now = datetime.now()
        if self._mode is H24_MODE:
            return now.strftime("%H:%M:%S:%f")[:-4]
        else:
            return now.strftime("%p %I:%M:%S")

