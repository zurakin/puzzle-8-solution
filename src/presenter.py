from model import Model


class Presenter:
    def __init__(self, view):
        self.view = view
        self.model = None

    def play(self):
        self.model = Model()
        self.model.shuffle()
        self.view.display_grid(self.model.get_grid())

    def move(self, tile_x, tile_y):
        self.model.move(tile_x, tile_y)
        self.view.display_grid(self.model.get_grid())
        print(self.model.get_counter())

    def help(self):
        solution = self.model.help()
        if len(solution) > 0:
            self.model.move(*solution[0][::-1])
            self.view.display_grid(self.model.get_grid())

    def key_up(self):
        self.model.move_up()
        self.view.display_grid(self.model.get_grid())

    def key_down(self):
        self.model.move_down()
        self.view.display_grid(self.model.get_grid())

    def key_right(self):
        self.model.move_right()
        self.view.display_grid(self.model.get_grid())

    def key_left(self):
        self.model.move_left()
        self.view.display_grid(self.model.get_grid())
