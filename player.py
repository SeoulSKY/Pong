from typing import Tuple

import pygame
from pygame import Rect, draw

PLAYER_WIDTH = 25
PLAYER_HEIGHT = 150
PLAYER_MAX_Y_SPEED = 20


class Player:

    def __init__(self, window: pygame.Surface, x_pos: float, y_pos: float, color: Tuple[int, int, int]):
        """
        Create a player
        :param window: The pygame window that player will be displayed
        :param x_pos: Player's initial x position
        :param y_pos: Player's initial y position
        :param color: The color of the player
        """
        self._window: pygame.Surface = window
        self._DEFAULT_X_POS: float = x_pos
        self._DEFAULT_Y_POS: float = y_pos
        self._rect = Rect(self._DEFAULT_X_POS, self._DEFAULT_Y_POS, PLAYER_WIDTH, PLAYER_HEIGHT)
        self._color: Tuple[int, int, int] = color
        self._y_speed: float = 0

    def x_pos(self) -> int:
        """
        Return the x position of the player
        :return: x position of the player
        """
        return self._rect.x

    def y_pos(self) -> int:
        """
        Return the y position of the player
        :return: y position of the player
        """
        return self._rect.y

    def y_speed(self) -> float:
        """
        Returns the y speed of the player
        :return: The y speed of the player
        """
        return self._y_speed

    def is_moving_up(self) -> bool:
        """
        Check if the player is moving up
        :return: True if the player is, False otherwise
        """
        return self._y_speed < 0

    def is_moving_down(self) -> bool:
        """
        Check if the player is moving down
        :return: True if the player is, False otherwise
        """
        return self._y_speed > 0

    def move_up(self) -> None:
        """
        Move the player upward based on the current speed
        """
        # check if the player is moving down
        if self.is_moving_down():
            self.stop()

        self._move()

        # accelerate upward
        if self._y_speed > -PLAYER_MAX_Y_SPEED:
            self._y_speed -= 0.7

            # make sure the current speed doesn't exceed the maximum speed
            if self._y_speed < -PLAYER_MAX_Y_SPEED:
                self._y_speed = -PLAYER_MAX_Y_SPEED

    def move_down(self) -> None:
        """
        Move the player downward based on the current speed
        """
        # check if the player is moving up
        if self.is_moving_up():
            self.stop()

        self._move()

        # accelerate downward
        if self._y_speed < PLAYER_MAX_Y_SPEED:
            self._y_speed += 0.7

            # make sure the current speed doesn't exceed the maximum speed
            if self._y_speed > PLAYER_MAX_Y_SPEED:
                self._y_speed = PLAYER_MAX_Y_SPEED

    def _move(self) -> None:
        """
        Move the player based on the current speed
        """
        self._rect.move_ip(0, self._y_speed)

    def stop(self) -> None:
        """
        Stop the player's movement
        """
        self._y_speed = 0

    def is_collided(self, x_pos: float, y_pos: float) -> bool:
        """
        Check if the given positions are within the player's area
        :param x_pos: The x position to check
        :param y_pos: The y position to check
        :return: True if the given positions are within the player's area, False otherwise
        """
        return self.x_pos() <= x_pos <= self.x_pos() + PLAYER_WIDTH and self.y_pos() <= y_pos <= self.y_pos() + PLAYER_HEIGHT

    def reset(self) -> None:
        """
        Reset the player to the initial state
        """
        self._rect.x = self._DEFAULT_X_POS
        self._rect.y = self._DEFAULT_Y_POS
        self.stop()

    def draw(self) -> None:
        """
        Draw the player
        """
        draw.rect(self._window, self._color, self._rect)
