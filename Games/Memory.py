import tkinter as tk
import pygame
import random
import sys
print(pygame.ver)

# Initialise pygame colours and constants
WIDTH, HEIGHT = 800, 600
GRID_COLS = 4
GRID_ROWS = 4
CELL_SIZE = 100
GRID_PADDING = 20
BG_COLOUR = (240, 240, 240)
TEXT_COLOUR = (0, 0, 0)
HIDDEN_COLOUR = (200, 200, 200)
FONT_SIZE = 36
PRESSED_COLOUR = (150, 150, 150)

# Sets up screen for game, font will be set after pygame.init() in main_game()
screen = None
font = None

class MemoryGame:
    def __init__(self):
        self.start_number = 1
        self.score = 0
        self.current_step = 0
        self.active_count = 4               # start with 4 numbers
        self.round_counter = 0              # count rounds
        self.last_active = set()            # holds grid positions used in previous round
        self.visible = False
        self.generate_grid()

    def generate_grid(self):
        self.cells = []
        # Create full grid with a grid position tuple for each cell.
        for row in range(GRID_ROWS):
            for col in range(GRID_COLS):
                cell = {
                    "grid_pos": (row, col),
                    "x": col * (CELL_SIZE + GRID_PADDING) + GRID_PADDING,
                    "y": row * (CELL_SIZE + GRID_PADDING) + GRID_PADDING,
                    "rect": pygame.Rect(col * (CELL_SIZE + GRID_PADDING) + GRID_PADDING,
                                          row * (CELL_SIZE + GRID_PADDING) + GRID_PADDING,
                                          CELL_SIZE,
                                          CELL_SIZE),
                    "clicked": False
                }
                self.cells.append(cell)
        # Prepare a list of cells whose grid_pos was not active in the previous round
        available = [cell for cell in self.cells if cell["grid_pos"] not in self.last_active]
        chosen = []
        if len(available) >= self.active_count:
            chosen = random.sample(available, self.active_count)
        else:
            # Not enough distinct new cells; choose available first then fill with previous active cells 
            chosen = available
            needed = self.active_count - len(available)
            old_cells = [cell for cell in self.cells if cell["grid_pos"] in self.last_active]
            chosen += random.sample(old_cells, needed)
        # Assign sequential numbers and update last_active positions 
        for i, cell in enumerate(chosen):
            cell["num"] = self.start_number + i
        self.last_active = {cell["grid_pos"] for cell in chosen}

    def draw(self):
        screen.fill(BG_COLOUR)
        for cell in self.cells:
            if "num" in cell:
                if self.visible:
                    pygame.draw.rect(screen, (255, 255, 255), cell["rect"])
                    text = font.render(str(cell["num"]), True, TEXT_COLOUR)
                    text_rect = text.get_rect(center=cell["rect"].center)
                    screen.blit(text, text_rect)
                else:
                    color = PRESSED_COLOUR if cell.get("clicked", False) else HIDDEN_COLOUR
                    pygame.draw.rect(screen, color, cell["rect"])
            else:
                # Inactive cells are always drawn in hidden colour
                pygame.draw.rect(screen, HIDDEN_COLOUR, cell["rect"])

        # Display score
        score_text = font.render(f"Score: {self.score}", True, TEXT_COLOUR)
        screen.blit(score_text, (WIDTH - 150, 20))

    def check_click(self, pos):
        for cell in self.cells:
            if cell["rect"].collidepoint(pos):
                # An inactive cell is an incorrect click
                if "num" not in cell:
                    self.game_over()
                    return False

                expected = self.start_number + self.current_step
                if cell["num"] == expected:
                    cell["clicked"] = True  # Mark as clicked
                    self.current_step += 1
                    self.score += 1
                    if self.current_step == self.active_count:
                        self.next_level()
                    return True
                else:
                    self.game_over()
                    return False
        return False

    def next_level(self):
        self.round_counter += 1
        # Every round add one more number (if available)
        if self.round_counter % 1 == 0:
            self.active_count += 1
            if self.active_count > len(self.cells):
                self.active_count = len(self.cells)
        self.current_step = 0
        # Reset clicked status and remove previous active numbers
        for cell in self.cells:
            cell.pop("num", None)
            cell["clicked"] = False
        self.generate_grid()
        self.show_numbers()

    def show_numbers(self):
        self.visible = True
        pygame.time.set_timer(pygame.USEREVENT, 3000)  # Display numbers for 3 seconds

    def hide_numbers(self):
        self.visible = False
        pygame.time.set_timer(pygame.USEREVENT, 0)  # Disable the timer

    def game_over(self):
        print(f"Game Over! Final Score: {self.score}")
        pygame.quit()
        sys.exit()

def main_game():
    global screen, font
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Memory Number Game")
    font = pygame.font.Font(None, FONT_SIZE)
    game = MemoryGame()
    game.show_numbers()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.USEREVENT:
                game.hide_numbers()
            elif event.type == pygame.MOUSEBUTTONDOWN and not game.visible:
                if event.button == 1:  # Left click
                    game.check_click(event.pos)

        game.draw()
        pygame.display.flip()

    pygame.quit()
    sys.exit()

# Tkinter Launcher
def launch_game():
    # launcher.destroy()
    main_game()

# launcher = tk.Tk()
# launcher.title("Memory Number Game Launcher")
# launcher.geometry("300x150")
# label = tk.Label(launcher, text="Welcome to Memory Number Game")
# label.pack(pady=20)
# start_button = tk.Button(launcher, text="Start Game", command=launch_game)
# start_button.pack(pady=10)
# launcher.mainloop()