from boggle_gui import *
from ex12_utils import *
from Model import *
import tkinter as tk
import time

class BoggleController:

    def __init__(self):
        self.gui = BoggleGui()
        self.model = Model()

        self.gui.set_button_text(self.model.board)
        self.gui.show_label_score(self.model.get_points())

    def run(self) -> None:
        self.gui.run()


if __name__ == "__main__":
    BoggleController().run()