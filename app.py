from kivy.app import App

from board import Board
from controller import GameController
from themes import Theme
from layout import TicTacToeLayout

# ------------------------------------------------------------------ #
def create_game(element: str = "wood") -> TicTacToeLayout:
    board      = Board()
    controller = GameController(board)
    theme      = Theme(element)
    return TicTacToeLayout(controller, theme)

# ------------------------------------------------------------------ #
class TicTacToeApp(App):
    def build(self):
        return create_game()

    def on_stop(self):
        # dọn nhạc nền nếu còn chạy
        root = self.root
        if hasattr(root, "_sounds") and root._sounds.bg:
            root._sounds.bg.stop()
