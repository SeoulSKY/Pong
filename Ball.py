import random

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

    def is_moving_up(self):
        return self._y_speed < 0

    def is_moving_down(self):
        return self._y_speed > 0

    def is_moving_left(self):
        return self._x_speed < 0

    def is_moving_right(self):
        return self._x_speed > 0

    def invert_x_speed(self):
        self._x_speed = -self._x_speed

    def invert_y_speed(self):
        self._y_speed = -self._y_speed

    def reset(self):
        self._x_pos = self._DEFAULT_X_POS
        self._y_pos = self._DEFAULT_Y_POS
        self._x_speed = DEFAULT_X_SPEED
        self._y_speed = DEFAULT_Y_SPEED

        # randomly invert the starting direction of the ball
        if random.randint(0, 1) == 0:
            self._x_speed = -self._x_speed
        if random.randint(0, 1) == 0:
            self._y_speed = -self._y_speed

    def move(self):
        self._x_pos += self._x_speed
        self._y_pos += self._y_speed

    def accelerate(self, factor):
        if factor < 1:
            factor = 1

        if self.is_moving_left():
            self._x_speed = -DEFAULT_X_SPEED * factor
        else:   # ball is moving right
            self._x_speed = DEFAULT_X_SPEED * factor

        if self.is_moving_up():
            self._y_speed = -DEFAULT_Y_SPEED * factor
        else:   # ball is moving down
            self._y_speed = DEFAULT_Y_SPEED * factor
