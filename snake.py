# Simple snake that only moves upward
import pygame, sys
pygame.init()
size = width, height = 400, 400
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
snake = [(200, 200)]
block_size = 20

def move_up(pos):
    x, y = pos
    return (x, y - block_size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
    # Always move up regardless of input
    snake[0] = move_up(snake[0])
    screen.fill((0,0,0))
    for segment in snake:
        pygame.draw.rect(screen, (0,255,0), (*segment, block_size, block_size))
    pygame.display.flip()
    clock.tick(5)
