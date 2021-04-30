import pygame

import Player
import Ball
import ScoreBoard

from tkinter import Tk, messagebox

# hide tk window to use message box only
Tk().withdraw()

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

pygame.font.init()
FONT_SIZE = int(WINDOW_WIDTH / 12)
arial_font = pygame.font.SysFont("arial", FONT_SIZE)

pygame.display.set_caption("Ping Pong")
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

player1 = Player.Player(x_pos=0, y_pos=WINDOW_HEIGHT / 2 - Player.HEIGHT / 2, color=RED)
player2 = Player.Player(x_pos=WINDOW_WIDTH - Player.WIDTH, y_pos=WINDOW_HEIGHT / 2 - Player.HEIGHT / 2, color=BLUE)
ball = Ball.Ball(x_pos=WINDOW_WIDTH / 2, y_pos=WINDOW_HEIGHT / 2, color=GREEN)
score_board = ScoreBoard.ScoreBoard()


def update_window():
    WINDOW.fill(BLACK)

    # draw the score board
    ver_margin = WINDOW_HEIGHT * 0.05
    hor_margin = WINDOW_WIDTH * 0.1

    player1_score = arial_font.render(str(score_board.player1_score()), False, WHITE)
    player2_score = arial_font.render(str(score_board.player2_score()), False, WHITE)
    WINDOW.blit(player1_score, (WINDOW_WIDTH / 2 - FONT_SIZE / 2 - hor_margin, ver_margin))
    WINDOW.blit(player2_score, (WINDOW_WIDTH / 2 + hor_margin, ver_margin))

    # draw the players
    pygame.draw.rect(WINDOW, player1.color(), player1.rect())
    pygame.draw.rect(WINDOW, player2.color(), player2.rect())

    # draw the ball
    pygame.draw.circle(WINDOW, ball.color(), ball.center(), Ball.RADIUS)

    pygame.display.update()


def handle_collision(player):
    if (player is player1 and ball.is_moving_left()) or (player is player2 and ball.is_moving_right()):
        ball.invert_x_speed()

    # bounce the ball upward if the ball was hit when the player was moving up
    if player.is_moving_up() and ball.is_moving_down():
        ball.invert_y_speed()
    # bounce the ball downward if the ball was hit when the player was moving down
    elif player.is_moving_down() and ball.is_moving_up():
        ball.invert_y_speed()

    # accelerate the ball depending on the speed of the player
    factor = 1 + player.y_speed() / Player.MAX_Y_SPEED
    ball.accelerate(factor)


def reset_game():
    player1.reset()
    player2.reset()
    score_board.reset()
    ball.reset()


def main():
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
        if pressed[pygame.K_w] and player1.y_pos() > 0:
            player1.move_up()
        elif pressed[pygame.K_s] and player1.y_pos() + Player.HEIGHT < WINDOW_HEIGHT:
            player1.move_down()
        else:
            player1.stop()

        if pressed[pygame.K_UP] and player2.y_pos() > 0:
            player2.move_up()
        elif pressed[pygame.K_DOWN] and player2.y_pos() + Player.HEIGHT < WINDOW_HEIGHT:
            player2.move_down()
        else:
            player2.stop()

        if pressed[pygame.K_ESCAPE]:
            messagebox.showinfo(message="The game is paused. Press OK to continue.")

        # check if the ball collided with player1
        if player1.is_collided(ball.x_pos() - Ball.RADIUS, ball.y_pos()):
            handle_collision(player1)

        # check if the ball collided with player2
        elif player2.is_collided(ball.x_pos() + Ball.RADIUS, ball.y_pos()):
            handle_collision(player2)

        # check if the ball collided with the top or bottom wall
        if ball.y_pos() - Ball.RADIUS <= 0 or ball.y_pos() + Ball.RADIUS >= WINDOW_HEIGHT:
            ball.invert_y_speed()

        # check if player1 missed the ball
        if ball.x_pos() - Ball.RADIUS < 0:
            score_board.add_player2_score()
            ball.reset()

        # check if player2 missed the ball
        elif ball.x_pos() + Ball.RADIUS > WINDOW_WIDTH:
            score_board.add_player1_score()
            ball.reset()

        ball.move()
        update_window()

        # check if player1 has won
        if score_board.is_player1_won():
            messagebox.showinfo(message="Player 1 won!")
            reset_game()

        # check if player 2 has won
        if score_board.is_player2_won():
            messagebox.showinfo(message="Player 2 won!")
            reset_game()

    pygame.quit()


if __name__ == "__main__":
    main()
