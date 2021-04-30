WINNING_SCORE = 11


class ScoreBoard:

    def __init__(self):
        self._player1_score = 0
        self._player2_score = 0

    def player1_score(self):
        return self._player1_score

    def player2_score(self):
        return self._player2_score

    def is_player1_won(self):
        return self._player1_score >= WINNING_SCORE

    def is_player2_won(self):
        return self._player2_score >= WINNING_SCORE

    def add_player1_score(self):
        self._player1_score += 1

    def add_player2_score(self):
        self._player2_score += 1

    def reset(self):
        self._player1_score = 0
        self._player2_score = 0
