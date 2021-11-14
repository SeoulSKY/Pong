import random
from typing import Tuple

import pygame
from pygame import draw

BALL_RADIUS = 15
BALL_DEFAULT_X_SPEED = 7
BALL_DEFAULT_Y_SPEED = 5


class Ball:
    def __init__(self, window: pygame.Surface, x_pos: float, y_pos: float, color: Tuple[int, int, int]):
        """
        Create a ball
        :param window: The pygame window that the ball will be displayed
        :param x_pos: The initial x position of the ball
        :param y_pos: The initial y position of the ball
        :param color: The color of the ball
        """
        self._window: pygame.Surface = window
        self._DEFAULT_X_POS: float = x_pos
        self._DEFAULT_Y_POS: float = y_pos
        self._x_pos: float = self._DEFAULT_X_POS
        self._y_pos: float = self._DEFAULT_Y_POS
        self._color: Tuple[int, int, int] = color
        self._x_speed: float = BALL_DEFAULT_X_SPEED
        self._y_speed: float = BALL_DEFAULT_Y_SPEED

    def x_pos(self) -> float:
        """
        Return the current x position of the ball
        :return: The current x position of the ball
        """
        return self._x_pos

    def y_pos(self) -> float:
        """
        Return the current y position of the ball
        :return: The current y position of the ball
        """
        return self._y_pos

    def is_moving_up(self) -> bool:
        """
        Check if the ball is moving up
        :return: True if it is, False otherwise
        """
        return self._y_speed < 0

    def is_moving_down(self) -> bool:
        """
        Check if the ball is moving down
        :return: True if it is, False otherwise
        """
        return self._y_speed > 0

    def is_moving_left(self) -> bool:
        """
        Check if the ball is moving left
        :return: True if it is, False otherwise
        """
        return self._x_speed < 0

    def is_moving_right(self) -> bool:
        """
        Check if the ball is moving right
        :return: True if it is, False otherwise
        """
        return self._x_speed > 0

    def invert_x_speed(self) -> None:
        """
        Invert the x speed of the ball
        """
        self._x_speed = -self._x_speed

    def invert_y_speed(self) -> None:
        """
        Invert the y speed of the ball
        """
        self._y_speed = -self._y_speed

    def reset(self) -> None:
        """
        Reset the ball to the initial state
        """
        self._x_pos = self._DEFAULT_X_POS
        self._y_pos = self._DEFAULT_Y_POS
        self._x_speed = BALL_DEFAULT_X_SPEED
        self._y_speed = BALL_DEFAULT_Y_SPEED

        # randomly invert the starting direction of the ball
        if random.randint(0, 1) == 0:
            self._x_speed = -self._x_speed
        if random.randint(0, 1) == 0:
            self._y_speed = -self._y_speed

    def move(self) -> None:
        """
        Move the ball based on the current speed
        """
        self._x_pos += self._x_speed
        self._y_pos += self._y_speed

    def accelerate(self, factor: float) -> None:
        """
        Accelerate the ball to the given factor
        :param factor: The factor of the acceleration
        """
        if factor < 1:
            factor = 1

        if self.is_moving_left():
            self._x_speed = -BALL_DEFAULT_X_SPEED * factor
        else:   # ball is moving right
            self._x_speed = BALL_DEFAULT_X_SPEED * factor

        if self.is_moving_up():
            self._y_speed = -BALL_DEFAULT_Y_SPEED * factor
        else:   # ball is moving down
            self._y_speed = BALL_DEFAULT_Y_SPEED * factor

    def draw(self) -> None:
        """
        Draw the ball
        """
        draw.circle(self._window, self._color, (self._x_pos, self._y_pos), BALL_RADIUS)
