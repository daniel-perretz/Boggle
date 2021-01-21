from ex12_utils import is_valid_path, load_words_dict
from typing import Optional, List, Tuple, Dict
from boggle_board_randomizer import *

DICT_FILE_PATH = "boggle_dict.txt"


class Model:
    """ This class is responsible for the logics behind the game, that
    do not have an obvious visual representations"""
    def __init__(self):
        """ Initializes the game's utilities"""
        self.board: Optional[List[List[str]]] = []
        self.__points: int = 0
        self.__words_dict: Dict[str, bool] = load_words_dict(DICT_FILE_PATH)
        self.__found_words: List[str] = []
        self.cur_path: Optional[List[Tuple[int]]] = []

    def create_board(self):
        """ Randomizes the board"""
        self.board = randomize_board()

    def handle_word(self) -> bool:
        """ Checks if a given word is valid or not"""
        word = is_valid_path(self.board, self.cur_path, self.__words_dict)
        if not word:
            return False
        else:
            if not self.__words_dict[word]\
                    or word in self.__found_words:  # meaning already found
                self.cur_path = []
                return False
            else:  # meaning word is valid
                self.update_points(len(word))
                self.__found_words.append(word)
                self.cur_path = []
                return True

    def update_points(self, len) -> None:
        """Updates points according to length of the word"""
        self.__points += len ** 2

    def reset(self):
        """Resets the model"""
        self.__points = 0
        self.cur_path = []
        self.__found_words = []

    def get_points(self):
        """ Returns points"""
        return self.__points

    def get_found_words(self):
        """ Returns found words"""
        return self.__found_words
