# app.py

import pygame
import time
import random
import os

# Initialize Pygame
pygame.init()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (200, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 255)

# Window size
width, height = 600, 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("🐍 Snake Game with Login & Scoreboard")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)

# Global file for saving scores
SCORE_FILE = "scores.txt"


def draw_text(text, color, x, y):
    screen_text = font.render(text, True, color)
    win.blit(screen_text, [x, y])


def login_screen():
    user = ""
    input_active = True

    while input_active:
        win.fill(black)
        draw_text("Enter your name: " + user, white, 100, 150)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    user = user[:-1]
                else:
                    user += event.unicode
    return user


def save_score(username, score):
    with open(SCORE_FILE, "a") as f:
        f.write(f"{username}:{score}\n")


def show_scoreboard():
    if not os.path.exists(SCORE_FILE):
        return []

    with open(SCORE_FILE, "r") as f:
        scores = [line.strip().split(":") for line in f.readlines()]
    scores = sorted(scores, key=lambda x: int(x[1]), reverse=True)
    return scores[:5]


def game_loop(username):
    exit_game = False
    game_over = False

    snake_x = 300
    snake_y = 200
    snake_size = 15
    velocity_x = 0
    velocity_y = 0
    snake_list = []
    snake_length = 1
    score = 0

    food_x = random.randint(20, width-20)
    food_y = random.randint(20, height-20)

    while not exit_game:
        if game_over:
            win.fill(black)
            draw_text("Game Over! Press Enter to Restart", red, 100, 150)
            draw_text(f"Your Score: {score}", green, 100, 190)
            draw_text("Top Scores:", blue, 100, 230)

            top_scores = show_scoreboard()
            for i, s in enumerate(top_scores):
                draw_text(f"{i+1}. {s[0]}: {s[1]}", white, 100, 260 + i * 25)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    game_loop(username)

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = 10
                        velocity_y = 0
                    elif event.key == pygame.K_LEFT:
                        velocity_x = -10
                        velocity_y = 0
                    elif event.key == pygame.K_UP:
                        velocity_y = -10
                        velocity_x = 0
                    elif event.key == pygame.K_DOWN:
                        velocity_y = 10
                        velocity_x = 0

            snake_x += velocity_x
            snake_y += velocity_y

            win.fill(black)
            pygame.draw.rect(win, red, [food_x, food_y, snake_size, snake_size])

            head = [snake_x, snake_y]
            snake_list.append(head)

            if len(snake_list) > snake_length:
                del snake_list[0]

            for block in snake_list[:-1]:
                if block == head:
                    game_over = True
                    save_score(username, score)

            if snake_x < 0 or snake_x > width or snake_y < 0 or snake_y > height:
                game_over = True
                save_score(username, score)

            for x, y in snake_list:
                pygame.draw.rect(win, green, [x, y, snake_size, snake_size])

            if abs(snake_x - food_x) < 15 and abs(snake_y - food_y) < 15:
                score += 10
                food_x = random.randint(20, width - 20)
                food_y = random.randint(20, height - 20)
                snake_length += 1

            draw_text(f"Player: {username}  Score: {score}", white, 10, 10)

            pygame.display.update()
            clock.tick(15)

    pygame.quit()
    quit()


# ---- Entry point ----
if __name__ == "__main__":
    username = login_screen()
    game_loop(username)
