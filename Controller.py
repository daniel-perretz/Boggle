from boggle_gui import *
from ex12_utils import *
from Model import *

class BoggleController:

    def __init__(self):
        self.gui = BoggleGui()
        self.model = Model()

        self.gui.set_button_text(self.model.board)

    def run(self) -> None:
        self.gui.run()



if __name__ == "__main__":
    BoggleController().run()