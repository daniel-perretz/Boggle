from boggle_gui import *
from Model import *


class BoggleController:

    def __init__(self):
        """ Initializes the model and graphic user interface of the game"""
        self.model = Model()
        self.gui = BoggleGui()
        self.gui.set_label_score(self.model.get_points())
        self.gui.set_start_button_command(self.start_game)
        self.gui.set_submit_button_command(self.submit)

    def start_game(self):
        """ Starts or restart the game, depending on the state of the game"""
        if not self.gui.is_counting:
            if self.gui.ask_for_a_break() is True:
                return
            self.model.create_board()
            self.gui.game_countdown()
            self.gui.set_buttons_text(self.model.board)
            self.gui.set_game_started_btn()
            self.gui.initiate_buttons_actions()

            if self.gui.games_played > 0:
                self.gui.update_highscore(self.model.get_points())
                self.model.reset()
                self.gui.reset()
                self.gui.set_label_score(self.model.get_points())
            self.gui.reset_buttons_color()

    def submit(self):
        """ Takes a submitted word from the GUI, checks if it is valid,
        and updates the game accordingly"""
        if self.gui.is_counting:
            self.gui.change_to_pressed()
            self.model.cur_path = self.gui.current_path
            if self.model.handle_word() is True:
                word = self.model.get_found_words()[-1]
                self.gui.show_found_word(word)
                self.gui.set_label_score(self.model.get_points())
                self.gui.reset_current_path_and_word()
            else:
                self.gui.reset_current_path_and_word()
            self.gui.reset_buttons_color()

    def run(self) -> None:
        self.gui.run()


if __name__ == "__main__":
    BoggleController().run()
