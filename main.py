import pygame
import Player
import Ball

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

pygame.display.set_caption("Ping Pong")
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

player1 = Player.Player(x_pos=0, y_pos=WINDOW_HEIGHT / 2 - Player.HEIGHT / 2, color=RED)
player2 = Player.Player(x_pos=WINDOW_WIDTH - Player.WIDTH, y_pos=WINDOW_HEIGHT / 2 - Player.HEIGHT / 2, color=BLUE)

ball = Ball.Ball(x_pos=WINDOW_WIDTH / 2, y_pos=WINDOW_HEIGHT / 2, color=GREEN)


def update_window():
    WINDOW.fill(BLACK)

    # draw the players
    pygame.draw.rect(WINDOW, player1.color(), player1.rect())
    pygame.draw.rect(WINDOW, player2.color(), player2.rect())

    # draw the ball
    pygame.draw.circle(WINDOW, ball.color(), ball.center(), Ball.RADIUS)

    pygame.display.update()


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

        # check if the ball collided with player1
        if player1.is_collided(ball.x_pos() - Ball.RADIUS, ball.y_pos()):
            ball.invert_x_speed()

        # check if the ball collided with player2
        if player2.is_collided(ball.x_pos() + Ball.RADIUS, ball.y_pos()):
            ball.invert_x_speed()

        # check if the ball collided with the top or bottom wall
        if ball.y_pos() - Ball.RADIUS <= 0 or ball.y_pos() + Ball.RADIUS >= WINDOW_HEIGHT:
            ball.invert_y_speed()

        # check if player1 missed the ball
        if ball.x_pos() - Ball.RADIUS < 0:
            ball.reset()

        # check if player2 missed the ball
        if ball.x_pos() + Ball.RADIUS > WINDOW_WIDTH:
            ball.reset()

        ball.move()
        update_window()

    pygame.quit()


if __name__ == "__main__":
    main()
