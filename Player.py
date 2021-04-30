from pygame import Rect

WIDTH = 25
HEIGHT = 150
MAX_Y_SPEED = 20


class Player:

    def __init__(self, x_pos, y_pos, color):
        self._DEFAULT_X_POS = x_pos
        self._DEFAULT_Y_POS = y_pos
        self._rect = Rect(self._DEFAULT_X_POS, self._DEFAULT_Y_POS, WIDTH, HEIGHT)
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

    def y_speed(self):
        return self._y_speed

    def is_moving_up(self):
        return self._y_speed < 0

    def is_moving_down(self):
        return self._y_speed > 0

    def move_up(self):
        # check if the player is moving down
        if self.is_moving_down():
            self.stop()

        self._move()

        # accelerate upward
        if self._y_speed > -MAX_Y_SPEED:
            self._y_speed -= 0.7

            # make sure the current speed doesn't exceed the maximum speed
            if self._y_speed < -MAX_Y_SPEED:
                self._y_speed = -MAX_Y_SPEED

    def move_down(self):
        # check if the player is moving up
        if self.is_moving_up():
            self.stop()

        self._move()

        # accelerate downward
        if self._y_speed < MAX_Y_SPEED:
            self._y_speed += 0.7

            # make sure the current speed doesn't exceed the maximum speed
            if self._y_speed > MAX_Y_SPEED:
                self._y_speed = MAX_Y_SPEED

    def _move(self):
        self._rect.move_ip(0, self._y_speed)

    def stop(self):
        self._y_speed = 0

    def is_collided(self, x_pos, y_pos):
        return self.x_pos() <= x_pos <= self.x_pos() + WIDTH and self.y_pos() <= y_pos <= self.y_pos() + HEIGHT

    def reset(self):
        self._rect.x = self._DEFAULT_X_POS
        self._rect.y = self._DEFAULT_Y_POS
        self.stop()
