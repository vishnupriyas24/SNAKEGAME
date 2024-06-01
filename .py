import pygame
import random
pygame.init()
WIDTH, HEIGHT = 400, 400
CELL_SIZE = 20
GRID_WIDTH, GRID_HEIGHT = WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE
FPS = 10
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = (0, 0)  # Initial direction
        self.color = GREEN
    def move(self):
        head = self.positions[0]
        x, y = self.direction
        new_head = ((head[0] + x * CELL_SIZE) % WIDTH, (head[1] + y * CELL_SIZE) % HEIGHT)
        if new_head in self.positions[1:]:
            self.reset()
        else:
            self.positions.insert(0, new_head)
            if len(self.positions) > self.length:
                self.positions.pop()
    def reset(self):
        self.length = 1
        self.positions = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = (0, 0)
    def draw(self, surface):
        for pos in self.positions:
            pygame.draw.rect(surface, self.color, (pos[0], pos[1], CELL_SIZE, CELL_SIZE))
    def handle_keys(self, key):
        if key == pygame.K_UP and self.direction != (0, 1):
            self.direction = (0, -1)
        elif key == pygame.K_DOWN and self.direction != (0, -1):
            self.direction = (0, 1)
        elif key == pygame.K_LEFT and self.direction != (1, 0):
            self.direction = (-1, 0)
        elif key == pygame.K_RIGHT and self.direction != (-1, 0):
            self.direction = (1, 0)
class Apple:
    def __init__(self):
        self.position = (random.randint(0, GRID_WIDTH - 1) * CELL_SIZE, random.randint(0, GRID_HEIGHT - 1) * CELL_SIZE)
        self.color = RED
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.position[0], self.position[1], CELL_SIZE, CELL_SIZE))
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()
    snake = Snake()
    apple = Apple()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                snake.handle_keys(event.key)
        snake.move()
        if snake.positions[0] == apple.position:
            snake.length += 1
            apple.position = (random.randint(0, GRID_WIDTH - 1) * CELL_SIZE, random.randint(0, GRID_HEIGHT - 1) * CELL_SIZE)
        screen.fill((0, 0, 0))
        snake.draw(screen)
        apple.draw(screen)
        pygame.display.update()
        clock.tick(FPS)
if __name__ == "__main__":
    main()