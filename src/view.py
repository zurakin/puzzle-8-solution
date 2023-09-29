import cv2

from presenter import Presenter
import numpy as np


class View:

    def __init__(self):
        self.presenter = Presenter(self)
        self.tile_size = 200
        self.canvas_size = self.tile_size * 3
        self.canvas_color = (192, 192, 192)
        self.canvas = np.zeros((self.canvas_size, self.canvas_size, 3), dtype=np.uint8)
        self.canvas[:] = self.canvas_color
        self.window_name = "puzzle-8"
        self.init_window()
        self.set_mouse_callback()

    def init_window(self):
        cv2.namedWindow(self.window_name)
        cv2.imshow(self.window_name, self.canvas)

    def display_tile(self, i, j, value, im_array):
        tile_color = (255, 255, 255)
        border_color = (0, 0, 0)
        font_scale = 2
        font_thickness = 3
        font_color = (0, 0, 0)

        x1, y1 = i * self.tile_size, j * self.tile_size
        x2, y2 = x1 + self.tile_size, y1 + self.tile_size

        tile = np.zeros((self.tile_size, self.tile_size, 3), dtype=np.uint8)
        tile[:] = tile_color
        cv2.rectangle(tile, (0, 0), (self.tile_size - 1, self.tile_size - 1), border_color, 2)

        font = cv2.FONT_HERSHEY_SIMPLEX
        text_size = cv2.getTextSize(str(value), font, font_scale, font_thickness)[0]
        text_x = (self.tile_size - text_size[0]) // 2
        text_y = (self.tile_size + text_size[1]) // 2
        cv2.putText(tile, str(value), (text_x, text_y), font, font_scale, font_color, font_thickness)

        im_array[y1:y2, x1:x2] = tile

    def display_grid(self, grid):
        im_array = np.copy(self.canvas)
        for i in range(3):
            for j in range(3):
                value = grid[i][j]
                if value is None:
                    continue
                self.display_tile(j, i, value, im_array)
        cv2.imshow(self.window_name, im_array)

    def set_mouse_callback(self):
        def mouse_callback(event, x, y, flags, param):
            if event == cv2.EVENT_LBUTTONDOWN:
                tile_x = x // self.tile_size
                tile_y = y // self.tile_size
                self.move(tile_x, tile_y)

        cv2.setMouseCallback(self.window_name, mouse_callback)

    def move(self, tile_x, tile_y):
        self.presenter.move(tile_x, tile_y)

    def play(self):
        self.presenter.play()

    @staticmethod
    def close_window():
        cv2.destroyAllWindows()

    def refresh(self):
        self.presenter.play()

    def run(self):
        while True:
            key = cv2.waitKeyEx(0)
            if key == 13:  # Enter key
                self.refresh()
            elif key == 2490368: # Up key
                self.presenter.key_up()
            elif key == 2555904: # Right key
                self.presenter.key_right()
            elif key == 2621440: # Down key
                self.presenter.key_down()
            elif key == 2424832: # Left key
                self.presenter.key_left()
            elif key == 104: # H key (Help)
                self.presenter.help()
            elif key == 27:  # Escape key
                break
