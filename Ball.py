RADIUS = 15
DEFAULT_X_SPEED = 7
DEFAULT_Y_SPEED = 5


class Ball:
    def __init__(self, x_pos, y_pos, color):
        self._DEFAULT_X_POS = x_pos
        self._DEFAULT_Y_POS = y_pos
        self._x_pos = self._DEFAULT_X_POS
        self._y_pos = self._DEFAULT_Y_POS
        self._color = color
        self._x_speed = DEFAULT_X_SPEED
        self._y_speed = DEFAULT_Y_SPEED

    def x_pos(self):
        return self._x_pos

    def y_pos(self):
        return self._y_pos

    def center(self):
        return self._x_pos, self._y_pos

    def color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def invert_x_speed(self):
        self._x_speed = -self._x_speed

    def invert_y_speed(self):
        self._y_speed = -self._y_speed

    def reset(self):
        self._x_pos = self._DEFAULT_X_POS
        self._y_pos = self._DEFAULT_Y_POS
        self._x_speed = DEFAULT_X_SPEED
        self._y_speed = DEFAULT_Y_SPEED

    def move(self):
        self._x_pos += self._x_speed
        self._y_pos += self._y_speed

    def change_speed(self, factor):
        self._x_speed = DEFAULT_X_SPEED * factor
        self._y_speed = DEFAULT_Y_SPEED * factor
