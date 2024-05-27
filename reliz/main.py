import pygame  # Імпортуємо модуль pygame
import random  # Імпортуємо модуль random для випадкових чисел
import sys  # Імпортуємо модуль sys для завершення програми

# Ініціалізуємо Pygame
pygame.init()

# Встановлюємо розміри вікна гри
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Встановлюємо заголовок вікна
pygame.display.set_caption("Avoid the Falling Blocks")

# Визначаємо кольори
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Визначаємо параметри гравця
player_size = 50
player_x = screen_width // 2
player_y = screen_height - 2 * player_size
player_speed = 10

# Визначаємо параметри перешкод
obstacle_width = 50
obstacle_height = 50
obstacle_speed = 5
obstacle_list = []

# Встановлюємо початковий рахунок
score = 0

# Визначаємо шрифт для відображення рахунку
font = pygame.font.SysFont("monospace", 35)

# Функція для створення нових перешкод
def create_obstacle():
    x_pos = random.randint(0, screen_width - obstacle_width)
    y_pos = 0 - obstacle_height
    obstacle_list.append([x_pos, y_pos])

# Функція для оновлення позиції перешкод
def update_obstacles():
    global score
    for obstacle in obstacle_list:
        obstacle[1] += obstacle_speed  # Переміщуємо перешкоди вниз
        if obstacle[1] > screen_height:  # Якщо перешкода вийшла за межі екрану
            obstacle_list.remove(obstacle)
            score += 1  # Додаємо очки

# Функція для перевірки зіткнень
def check_collisions():
    for obstacle in obstacle_list:
        if (player_x < obstacle[0] < player_x + player_size or player_x < obstacle[0] + obstacle_width < player_x + player_size) and (player_y < obstacle[1] < player_y + player_size or player_y < obstacle[1] + obstacle_height < player_y + player_size):
            return True
    return False

# Основний цикл гри
running = True
while running:
    # Перевіряємо події
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Якщо гравець закриває вікно
            running = False  # Виходимо з основного циклу

    # Отримуємо стан всіх клавіш
    keys = pygame.key.get_pressed()

    # Рухаємо гравця залежно від натиснутих клавіш
    if keys[pygame.K_LEFT] and player_x - player_speed >= 0:
        player_x -= player_speed  # Рух вліво
    if keys[pygame.K_RIGHT] and player_x + player_speed <= screen_width - player_size:
        player_x += player_speed  # Рух вправо

    # Створюємо нові перешкоди
    if random.randint(1, 20) == 1:  # 1 з 20 шансів на кожній ітерації
        create_obstacle()

    # Оновлюємо позиції перешкод
    update_obstacles()

    # Перевіряємо зіткнення
    if check_collisions():
        running = False  # Завершуємо гру, якщо є зіткнення

    # Заповнюємо екран білим кольором
    screen.fill(WHITE)

    # Малюємо гравця
    pygame.draw.circle(screen, BLUE, (player_x + player_size // 2, player_y + player_size // 2), player_size // 2)

    # Малюємо перешкоди
    for obstacle in obstacle_list:
        pygame.draw.rect(screen, RED, (obstacle[0], obstacle[1], obstacle_width, obstacle_height))

    # Відображаємо рахунок
    score_text = font.render("Score: {}".format(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Оновлюємо екран
    pygame.display.flip()

    # Встановлюємо частоту оновлення екрану
    pygame.time.Clock().tick(30)

# Виходимо з Pygame
pygame.quit()
sys.exit()