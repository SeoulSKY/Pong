import pygame

WINNING_SCORE = 11


class ScoreBoard:

    _WHITE = (255, 255, 255)

    def __init__(self, window: pygame.Surface):
        """
        Create a score board
        """
        self._window: pygame.Surface = window
        self._player1_score: int = 0
        self._player2_score: int = 0

    def is_player1_won(self) -> bool:
        """
        Check if the score of player 1 has reached the winning score
        :return: True if it has reached, False otherwise
        """
        return self._player1_score >= WINNING_SCORE

    def is_player2_won(self) -> bool:
        """
        Check if the score of player 2 has reached the winning score
        :return: True if it has reached, False otherwise
        """
        return self._player2_score >= WINNING_SCORE

    def add_player1_score(self) -> None:
        """
        Increment player 1's score by 1
        """
        self._player1_score += 1

    def add_player2_score(self) -> None:
        """
        Increment player 2's score by 1
        """
        self._player2_score += 1

    def reset(self) -> None:
        """
        Reset the score board to the initial state
        """
        self._player1_score = 0
        self._player2_score = 0

    def draw(self) -> None:
        """
        Draw the score board
        """
        ver_margin = self._window.get_height() * 0.05
        hor_margin = self._window.get_width() * 0.1

        font_size = int(self._window.get_width() / 12)
        arial_font = pygame.font.SysFont("arial", font_size)

        player1_score = arial_font.render(str(self._player1_score), False, self._WHITE)
        player2_score = arial_font.render(str(self._player2_score), False, self._WHITE)

        self._window.blit(player1_score, (self._window.get_width() / 2 - font_size / 2 - hor_margin, ver_margin))
        self._window.blit(player2_score, (self._window.get_width() / 2 + hor_margin, ver_margin))
