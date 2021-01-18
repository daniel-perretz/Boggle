from boggle_gui import *
from ex12_utils import *
from Model import *

class BoggleController:

    def __init__(self):
        self.model = Model()
        self.gui = BoggleGui()
        self.gui.set_label_score(self.model.get_points())
        self.gui.set_start_button_command(self.start_game)
        self.gui.set_submit_button_command(self.submit)

    def start_game(self):
        if not self.gui.is_counting:
            self.model.create_board()
            self.gui.game_countdown()
            self.gui.set_buttons_text(self.model.board)
            self.gui.initiate_buttons_actions()

    def submit(self):
        self.model.cur_path = self.gui.current_path
        if self.model.handle_word() == True:
            word = "banana"
            self.gui.show_correct_word(word)
            self.gui.set_label_score(self.model.get_points())

        else:
            self.gui.current_path = []
        for button in self.gui.buttons_list:
            button["bg"] = MAIN_COLOR


    def run(self) -> None:
        self.gui.run()


if __name__ == "__main__":
    BoggleController().run()
