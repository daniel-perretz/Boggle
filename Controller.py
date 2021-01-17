from boggle_gui import *
from ex12_utils import *
from Model import *

class BoggleController:

    def __init__(self):
        self.gui = BoggleGui()
        self.model = Model()

        self.gui.set_button_text(self.model.board)
        self.gui.show_label_score(self.model.get_points())

    def run(self) -> None:
        self.gui.run()

    def handle_button_press(self, button):
        coor = self.get_button_location(button)
        self.model.update_cur_path(coor)

    def get_button_location(self, button):
        return self.gui.buttons_dict[button]

    def submit_word(self, word):
        self.model.handle_word()

if __name__ == "__main__":
    BoggleController().run()