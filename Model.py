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

    def update_cur_path(self, coor):
        self.cur_path.append(coor)

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
