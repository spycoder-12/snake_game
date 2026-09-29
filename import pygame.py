import pygame
import random

pygame.init()

# ---------- Screen ----------
WIDTH, HEIGHT = 600, 460
GRID_TOP = 60          # space reserved at the top for the HUD bar
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

# ---------- Settings ----------
BLOCK = 20
BASE_SPEED = 10
MAX_SPEED = 22

# ---------- Colors ----------
WHITE = (245, 245, 245)
BLACK = (20, 20, 20)
YELLOW = (255, 213, 79)
RED = (220, 70, 70)
GREEN = (76, 187, 91)
DARK_GREEN = (46, 140, 60)
BLUE_BG = (24, 32, 46)
GRID_LINE = (33, 43, 60)
HUD_BG = (18, 24, 36)
ACCENT = (90, 170, 255)

# ---------- Fonts ----------
font_small = pygame.font.SysFont("bahnschrift", 22)
font_medium = pygame.font.SysFont("bahnschrift", 30)
font_big = pygame.font.SysFont("comicsansms", 44)

HS_FILE = "highscore.txt"


# ---------- High Score persistence ----------
def load_high_score():
    try:
        with open(HS_FILE, "r") as f:
            return int(f.read())
    except Exception:
        return 0


def save_high_score(score):
    try:
        with open(HS_FILE, "w") as f:
            f.write(str(score))
    except Exception:
        pass


# ---------- Drawing helpers ----------
def draw_grid():
    for x in range(0, WIDTH, BLOCK):
        pygame.draw.line(screen, GRID_LINE, (x, GRID_TOP), (x, HEIGHT))
    for y in range(GRID_TOP, HEIGHT, BLOCK):
        pygame.draw.line(screen, GRID_LINE, (0, y), (WIDTH, y))


def draw_snake(snake):
    for i, (x, y) in enumerate(snake):
        color = ACCENT if i == len(snake) - 1 else GREEN
        rect = pygame.Rect(x + 1, y + 1, BLOCK - 2, BLOCK - 2)
        pygame.draw.rect(screen, color, rect, border_radius=6)
        if i == len(snake) - 1:  # head accent border
            pygame.draw.rect(screen, DARK_GREEN, rect, width=2, border_radius=6)


def draw_food(food_x, food_y):
    cx, cy = food_x + BLOCK // 2, food_y + BLOCK // 2
    pygame.draw.circle(screen, YELLOW, (cx, cy), BLOCK // 2 - 2)
    pygame.draw.circle(screen, (255, 240, 180), (cx, cy), BLOCK // 2 - 2, width=2)


def draw_hud(score, high_score, length):
    pygame.draw.rect(screen, HUD_BG, (0, 0, WIDTH, GRID_TOP))
    pygame.draw.line(screen, ACCENT, (0, GRID_TOP), (WIDTH, GRID_TOP), 2)

    score_surf = font_medium.render(f"Score: {score}", True, WHITE)
    high_surf = font_small.render(f"Best: {high_score}", True, YELLOW)
    len_surf = font_small.render(f"Length: {length}", True, (170, 200, 230))

    screen.blit(score_surf, (16, 14))
    screen.blit(high_surf, (WIDTH - high_surf.get_width() - 16, 10))
    screen.blit(len_surf, (WIDTH - len_surf.get_width() - 16, 34))


def draw_centered_text(text, font, color, y):
    surf = font.render(text, True, color)
    screen.blit(surf, (WIDTH // 2 - surf.get_width() // 2, y))


def flush_events():
    """Clear the event queue so stray key presses don't leak between states."""
    pygame.event.clear()


# ---------- Game state ----------
def new_game_state():
    x = (WIDTH // BLOCK // 2) * BLOCK
    y = GRID_TOP + ((HEIGHT - GRID_TOP) // BLOCK // 2) * BLOCK
    return {
        "x": x, "y": y,
        "dx": BLOCK, "dy": 0,
        "direction": "RIGHT",
        "snake": [],
        "length": 1,
        "food": spawn_food([]),
    }


def spawn_food(snake):
    while True:
        fx = random.randrange(0, WIDTH - BLOCK, BLOCK)
        fy = random.randrange(GRID_TOP, HEIGHT - BLOCK, BLOCK) // BLOCK * BLOCK
        if [fx, fy] not in snake:
            return (fx, fy)


def current_speed(length):
    return min(MAX_SPEED, BASE_SPEED + (length // 4))


# ---------- Screens ----------
def menu_screen(high_score):
    flush_events()
    while True:
        screen.fill(BLUE_BG)
        draw_grid()
        draw_hud(0, high_score, 1)
        draw_centered_text("SNAKE", font_big, ACCENT, 130)
        draw_centered_text("Press SPACE or ENTER to start", font_medium, WHITE, 220)
        draw_centered_text("Arrow keys to move  |  Q to quit", font_small, (170, 200, 230), 270)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_SPACE, pygame.K_RETURN):
                    return True
                if event.key == pygame.K_q:
                    return False
        clock.tick(30)


def game_over_screen(score, high_score, new_record):
    flush_events()
    while True:
        screen.fill(BLUE_BG)
        draw_grid()
        draw_hud(score, high_score, score + 1)
        draw_centered_text("GAME OVER", font_big, RED, 120)
        if new_record:
            draw_centered_text("New High Score!", font_medium, YELLOW, 190)
        draw_centered_text(f"Final Score: {score}", font_medium, WHITE, 230)
        draw_centered_text("Press C to Play Again  |  Q to Quit", font_small, (170, 200, 230), 280)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    return True
                if event.key == pygame.K_q:
                    return False
        clock.tick(30)


# ---------- Main game loop (single round) ----------
def play_round(high_score):
    state = new_game_state()
    flush_events()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit", state["length"] - 1, high_score
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and state["direction"] != "RIGHT":
                    state["direction"] = "LEFT"
                    state["dx"], state["dy"] = -BLOCK, 0
                elif event.key == pygame.K_RIGHT and state["direction"] != "LEFT":
                    state["direction"] = "RIGHT"
                    state["dx"], state["dy"] = BLOCK, 0
                elif event.key == pygame.K_UP and state["direction"] != "DOWN":
                    state["direction"] = "UP"
                    state["dx"], state["dy"] = 0, -BLOCK
                elif event.key == pygame.K_DOWN and state["direction"] != "UP":
                    state["direction"] = "DOWN"
                    state["dx"], state["dy"] = 0, BLOCK
                elif event.key == pygame.K_q:
                    return "quit", state["length"] - 1, high_score

        # Move
        state["x"] += state["dx"]
        state["y"] += state["dy"]

        # Wall collision
        if (state["x"] < 0 or state["x"] >= WIDTH or
                state["y"] < GRID_TOP or state["y"] >= HEIGHT):
            return "over", state["length"] - 1, high_score

        # Draw frame
        screen.fill(BLUE_BG)
        draw_grid()

        food_x, food_y = state["food"]
        draw_food(food_x, food_y)

        head = [state["x"], state["y"]]
        state["snake"].append(head)
        if len(state["snake"]) > state["length"]:
            del state["snake"][0]

        # Self collision
        for part in state["snake"][:-1]:
            if part == head:
                return "over", state["length"] - 1, high_score

        draw_snake(state["snake"])
        draw_hud(state["length"] - 1, high_score, state["length"])
        pygame.display.update()

        # Eat food
        if state["x"] == food_x and state["y"] == food_y:
            state["length"] += 1
            state["food"] = spawn_food(state["snake"])
            if state["length"] - 1 > high_score:
                high_score = state["length"] - 1
                save_high_score(high_score)

        clock.tick(current_speed(state["length"]))


# ---------- Top-level app loop ----------
def main():
    high_score = load_high_score()

    if not menu_screen(high_score):
        pygame.quit()
        return

    while True:
        result, score, high_score = play_round(high_score)

        if result == "quit":
            pygame.quit()
            return

        new_record = score >= high_score and score > 0
        if not game_over_screen(score, high_score, new_record):
            pygame.quit()
            return
        # loop back into a fresh round with a clean event queue


if __name__ == "__main__":
    main()