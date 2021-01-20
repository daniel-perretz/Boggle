from boggle_gui import *
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
        else:
            self.model.restart()
            self.gui.reset()
            self.gui.set_label_score(self.model.get_points())

    def submit(self):
        self.model.cur_path = self.gui.current_path
        if self.model.handle_word() is True:
            word = self.model.get_found_words()[-1]
            self.gui.show_found_word(word)
            self.gui.set_label_score(self.model.get_points())
            self.reset_current_path_and_word()
        else:
            self.reset_current_path_and_word()
        for button in self.gui.buttons_list:
            button["bg"] = MAIN_COLOR

    def reset_current_path_and_word(self):
        self.gui.current_path = []
        self.gui.current_word = []
        self.gui.set_current_word_label()

    def run(self) -> None:
        self.gui.run()


if __name__ == "__main__":
    BoggleController().run()
