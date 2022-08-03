import pygame

from player import Player, PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_MAX_Y_SPEED
from ball import Ball, BALL_RADIUS
from score_board import ScoreBoard

from tkinter import Tk, messagebox

# hide tk window to use message box only
Tk().withdraw()

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
FPS = 60

BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

pygame.font.init()

pygame.display.set_caption("Pong")
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

PLAYER_1 = Player(window=WINDOW, x_pos=0, y_pos=WINDOW_HEIGHT / 2 - PLAYER_HEIGHT / 2, color=RED)
PLAYER_2 = Player(window=WINDOW, x_pos=WINDOW_WIDTH - PLAYER_WIDTH, y_pos=WINDOW_HEIGHT / 2 - PLAYER_HEIGHT / 2, color=BLUE)
BALL = Ball(window=WINDOW, x_pos=WINDOW_WIDTH / 2, y_pos=WINDOW_HEIGHT / 2, color=GREEN)
SCORE_BOARD = ScoreBoard(window=WINDOW)


def update_window() -> None:
    """
    Draw the game objects
    """
    WINDOW.fill(BLACK)

    SCORE_BOARD.draw()

    PLAYER_1.draw()
    PLAYER_2.draw()

    BALL.draw()

    pygame.display.update()


def handle_collision(player: Player) -> None:
    """
    Handles collision between the given player and the ball
    :param player: The player who is collided with the ball
    """
    if (player is PLAYER_1 and BALL.is_moving_left()) or (player is PLAYER_2 and BALL.is_moving_right()):
        BALL.invert_x_speed()

    # bounce the ball upward if the ball was hit when the player was moving up
    if player.is_moving_up() and BALL.is_moving_down():
        BALL.invert_y_speed()

    # bounce the ball downward if the ball was hit when the player was moving down
    elif player.is_moving_down() and BALL.is_moving_up():
        BALL.invert_y_speed()

    # accelerate the ball depending on the speed of the player
    factor = 1 + abs(player.y_speed()) / PLAYER_MAX_Y_SPEED
    BALL.accelerate(factor)


def reset_game() -> None:
    """
    Reset the game to the initial state
    """
    PLAYER_1.reset()
    PLAYER_2.reset()
    SCORE_BOARD.reset()
    BALL.reset()


def main() -> None:
    """
    Run the game
    """
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            # exit the while loop when the window is closed
            if event.type == pygame.QUIT:
                running = False

        # check keyboard inputs
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w] and PLAYER_1.y_pos() > 0:
            PLAYER_1.move_up()
        elif pressed[pygame.K_s] and PLAYER_1.y_pos() + PLAYER_HEIGHT < WINDOW_HEIGHT:
            PLAYER_1.move_down()
        else:
            PLAYER_1.stop()

        if pressed[pygame.K_UP] and PLAYER_2.y_pos() > 0:
            PLAYER_2.move_up()
        elif pressed[pygame.K_DOWN] and PLAYER_2.y_pos() + PLAYER_HEIGHT < WINDOW_HEIGHT:
            PLAYER_2.move_down()
        else:
            PLAYER_2.stop()

        if pressed[pygame.K_ESCAPE]:
            messagebox.showinfo(message="The game is paused. Press OK to continue.")

        # check if the ball collided with player1
        if PLAYER_1.is_collided(BALL.x_pos() - BALL_RADIUS, BALL.y_pos()):
            handle_collision(PLAYER_1)

        # check if the ball collided with player2
        elif PLAYER_2.is_collided(BALL.x_pos() + BALL_RADIUS, BALL.y_pos()):
            handle_collision(PLAYER_2)

        # check if the ball collided with the top or bottom wall
        if BALL.y_pos() - BALL_RADIUS <= 0 or BALL.y_pos() + BALL_RADIUS >= WINDOW_HEIGHT:
            BALL.invert_y_speed()

        # check if player1 missed the ball
        if BALL.x_pos() - BALL_RADIUS < 0:
            SCORE_BOARD.add_player2_score()
            BALL.reset()

        # check if player2 missed the ball
        elif BALL.x_pos() + BALL_RADIUS > WINDOW_WIDTH:
            SCORE_BOARD.add_player1_score()
            BALL.reset()

        BALL.move()
        update_window()

        # check if player1 has won
        if SCORE_BOARD.is_player1_won():
            messagebox.showinfo(message="Player 1 won!")
            reset_game()

        # check if player 2 has won
        if SCORE_BOARD.is_player2_won():
            messagebox.showinfo(message="Player 2 won!")
            reset_game()

    pygame.quit()


if __name__ == "__main__":
    main()
