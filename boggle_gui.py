import tkinter as tki
from typing import Callable, Dict, List, Any

class BoggleGui:
    def __init__(self):
        root = tki.Tk()
        self._main_window = root
        self._display_label = tki.Label(self._outer_frame, font=("Courier", 30),
                                        bg=REGULAR_COLOR, width=23, relief="ridge")
        self._display_label.pack(side=tki.TOP, fill=tki.BOTH)

    def run(self) -> None:
        self._main_window.mainloop()

if __name__ == "__main__":
    cg = BoggleGui()
    cg.run()

