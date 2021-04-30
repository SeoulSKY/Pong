from pygame import Rect

WIDTH = 25
HEIGHT = 150
MAX_Y_SPEED = 20


class Player:

    def __init__(self, x_pos, y_pos, color):
        self._rect = Rect(x_pos, y_pos, WIDTH, HEIGHT)
        self._color = color
        self._y_speed = 0

    def rect(self):
        return self._rect

    def x_pos(self):
        return self._rect.x

    def y_pos(self):
        return self._rect.y

    def color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def move_up(self):
        # check if the player is moving down
        if self._y_speed > 0:
            self.stop()

        self._move()

        # accelerate upward
        if self._y_speed >= -MAX_Y_SPEED:
            self._y_speed -= 0.5

    def move_down(self):
        # check if the player is moving up
        if self._y_speed < 0:
            self.stop()

        self._move()

        # accelerate downward
        if self._y_speed <= MAX_Y_SPEED:
            self._y_speed += 0.5

    def _move(self):
        self._rect.move_ip(0, self._y_speed)

    def stop(self):
        self._y_speed = 0

    def is_collided(self, x_pos, y_pos):
        return self.x_pos() <= x_pos <= self.x_pos() + WIDTH and self.y_pos() <= y_pos < self.y_pos() + HEIGHT
