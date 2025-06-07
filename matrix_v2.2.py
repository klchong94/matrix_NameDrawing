import pygame
from random import randint, choice
from pygame.locals import *
import string
import sys

# Define a list of names to be used
names = [
    "Carmen Marshall",
    "Kaiden Merritt",
    "Kaisley Duran",
    "Ismael Henson",
    "Kinslee Bond",
    "Roger Adams",
    "Stella Wise",
    "Frederick Friedman",
    "Aspyn Bates",
    "Ellis Jennings",
    "Palmer Pham",
    "Russell Mayo",
    "Aarya Terry",
    "Armani Mann",
    "Paislee Pacheco",
    "Erik Zimmerman",
    "Ariyah Duncan",
    "Avery Bass",
    "Zahra Fisher",
    "Gael Richmond",
    "Whitney Schmitt",
    "Murphy Ramsey",
    "Lyric Sheppard",
    "Trent Snyder",
    "Callie Stevens",
    "Zachary Holmes",
    "Bailey Bailey",
    "Axel Mejia",
    "Saylor Williams",
    "Oliver Hess",
    "Kaliyah Farley",
    "Graysen O’Neill",
    "Kenna Atkins",
    "Cason Love",
    "Avianna Miller",
    "Benjamin Shelton",
    "Makenzie Carpenter",
    "Jeremy Mack",
    "Nadia Costa",
    "Kenji Lam",
    "Karina Vance",
    "Casen Bowers",
    "Elisa Bryant",
    "Jonah Melton",
    "Kamiyah O’Neill",
    "Marcel Horne",
    "Marlowe Holt",
    "Niko Underwood",
    "Ensley Ray",
    "Arlo McKinney",
    "Gwendolyn McClure",
    "Reese McPherson",
    "Emmaline Harrington",
    "Omari Costa",
    "Robin Farley",
    "Graysen Bowen",
    "Dream Rodgers",
    "Mathias Le",
    "Myla Sierra",
    "Dayton Holmes",
    "Bailey Liu",
    "Pedro Fitzgerald",
    "Marlee Rivera",
    "Charles Friedman",
    "Aspyn Roth",
    "Roy Booker",
    "Nataly Gilbert",
    "Tobias Espinosa",
    "Braylee Stanton",
    "Zyair Patrick",
    "Lyra Coffey",
    "Kody Palacios",
    "Bria Butler",
    "Ryder Bowen",
    "Dream Roth",
    "Roy Chen",
    "Valeria Simpson",
    "Elliott Vincent",
    "Allyson Schmitt",
    "Murphy Gutierrez",
    "Savannah Chavez",
    "Ian McCann",
    "Joyce Huerta",
    "Douglas Harvey",
    "Nicole Sanders",
    "Jose Cervantes",
    "Aylin Love",
    "Jeffrey Jones",
    "Sophia Juarez",
    "Joaquin Allen",
    "Riley Tapia",
    "Samir Rodgers",
    "Selah Berg",
    "Cayson Young",
    "Zoey Torres",
    "Jayden Guerra",
    "Edith Ball",
    "Shane Whitaker",
    "Ivanna Moreno",
    "Myles Brennan",
    "Elodie Austin",
    "Omar Ware",
    "Eileen Montoya",
    "Ford McKee",
    "Kori Brennan",
    "Curtis Sampson",
    "Meilani Rivera",
    "Charles Morris",
    "Genesis Proctor",
    "Vance Jackson",
    "Avery Nelson",
    "Dylan Weiss",
    "Lennox Bates",
    "Ellis Bullock",
    "Winnie Beck",
    "Eduardo Galindo",
    "Corinne Bush",
    "Tyson Watkins",
    "Lola Ryan",
    "Timothy Weber",
    "Alayah McIntyre",
    "Eliseo Blankenship",
    "Rosalee Cook",
    "Ezekiel Pollard",
    "Marisol Webster",
    "Shawn Hale",
    "Brinley Small",
    "Rudy English",
    "Kelly Stewart",
    "Nolan Lee",
    "Scarlett Singh",
    "Louis Lara"
]

reveal_names = [
        "Carmen Marshall",
        "Kaiden Merritt",
        "Kaisley Duran",
        "Ismael Henson"
]

# Initialize Pygame Mixer
pygame.mixer.init()

# Load Sound Files (replace 'sound_file.wav' with your actual file paths)
try:
    background_hum = pygame.mixer.Sound("resources/sounds/background_hum.wav")
    glitch_sound = pygame.mixer.Sound("resources/sounds/glitch.wav")
    scan_sound = pygame.mixer.Sound("resources/sounds/scan.wav")
    reveal_sound = pygame.mixer.Sound("resources/sounds/reveal.wav")
    shuffle_sound = pygame.mixer.Sound("resources/sounds/shuffle.wav") # Load the shuffle sound
except pygame.error as e:
    print(f"Error loading sound file: {e}")
    background_hum = None
    glitch_sound = None
    scan_sound = None
    reveal_sound = None
    shuffle_sound = None

class textblock():
    def __init__(self, character, font, background, fadetime, x_pos, y_pos):
        self.character = character
        self.font = font
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.cur_color = 0
        self.rect = None
        self.color_prog = [(255, 255, 255), (250, 250, 250), (150, 150, 150),
                            (125, 250, 125), (0, 250, 0), (0, 250, 0),
                            (0, 250, 0), (0, 125, 0), (0, 100, 0), (0, 0, 0)]
        self.last_update = pygame.time.get_ticks()
        self.fade_interval = (fadetime * 1000) / len(self.color_prog)
        self.update(background)
    def update(self, background):
        current_time = pygame.time.get_ticks()
        if (current_time - self.last_update) > self.fade_interval:
            self.last_update = current_time
            self.cur_color += 1
            if randint(0, 1000) == 1:
                self.character = choice(string.ascii_lowercase)
            if self.cur_color >= len(self.color_prog):
                background.fill(pygame.Color("black"), self.rect)
                return False
            text = self.font.render(self.character, 1, self.color_prog[self.cur_color])
            textpos = text.get_rect()
            textpos.x = self.x_pos
            textpos.y = self.y_pos
            background.blit(text, textpos)
            self.rect = textpos
        return True

class textline():
    def __init__(self, font, background, x_pos, speed):
        self.x_pos = x_pos
        self.font = font
        self.speed = speed
        self.chars = []
        self.fade_time = randint(1, 4)
        self.head_y_pos = 0
        self.last_update = pygame.time.get_ticks()
        self.font_height = font.get_height()
        self.current_name = ""
        self.name_index = 0
        self.new_name()
        self.update(background)
    def new_name(self):
        global names
        self.current_name = choice(names)
        self.name_index = 0
    def update(self, background):
        to_remove = []
        for i, char in enumerate(self.chars):
            if not char.update(background):
                to_remove.append(i)
        for i in sorted(to_remove, reverse=True):
            del (self.chars[i])
        current_time = pygame.time.get_ticks()
        if (current_time - self.last_update) > self.speed:
            self.last_update = current_time
            if self.head_y_pos < background.get_height():
                if self.name_index < len(self.current_name):
                    new_char = self.current_name[self.name_index]
                    self.chars.append(textblock(new_char, self.font,
                                                background, self.fade_time,
                                                self.x_pos, self.head_y_pos))
                    self.head_y_pos += self.font_height
                    self.name_index += 1
                else:
                    self.new_name()
                    self.head_y_pos += self.font_height
                    self.name_index = 0
            elif not self.chars:
                return False
        return True

def add_line(matrix_lines, font, background, num_columns, used_columns):
    screen_width = background.get_width()
    column_width = screen_width // num_columns
    available_columns = list(set(range(num_columns)) - used_columns)
    if not available_columns:
        return
    random_column = choice(available_columns)
    x_pos = random_column * column_width
    line = textline(font, background, x_pos, randint(60, 150))
    matrix_lines.append((line, random_column))
    used_columns.add(random_column)

# Glowing button effect
def draw_glowing_text(surface, text, font, position, base_color, glow_color):
    glow_sizes = [2, 4, 6]
    for size in glow_sizes:
        glow_surf = font.render(text, True, glow_color)
        glow_surf.set_alpha(30)
        surface.blit(glow_surf, glow_surf.get_rect(center=(position[0], position[1] + size)))
    final_text = font.render(text, True, base_color)
    surface.blit(final_text, final_text.get_rect(center=position))

def main():
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption('Falling Text')
    background = pygame.Surface(screen.get_size()).convert()
    background.fill((0, 0, 0))
    screen_width = screen.get_width()
    screen_height = screen.get_height()
    clock = pygame.time.Clock()
    matrix_font = pygame.font.Font("resources/fonts/matrix.ttf", 30)
    normal_font = pygame.font.Font("resources/fonts/arial.ttf", 60)
    large_font = pygame.font.Font("resources/fonts/arial.ttf", 48)
    underscore_font = pygame.font.Font("resources/fonts/arial.ttf", 60)
    num_columns = 50
    matrix_lines = []
    used_columns = set()
    for _ in range(num_columns):
        add_line(matrix_lines, matrix_font, background, num_columns, used_columns)
    screen.blit(background, (0, 0))
    pygame.display.flip()
    clock.tick(60)
    waiting_for_input = True
    selected_name = ""
    scramble_timer = pygame.time.get_ticks()
    scramble_interval = 120
    scramble_progress = 0
    name_surface = normal_font.render("", True, (0, 250, 0))
    underscore_visible = False
    underscore_timer = 0
    underscore_interval = 500
    current_reveal_index = 0
    displaying_names = False
    waiting_for_next_round_input = False
    pending_input_timer = 0
    pending_input_delay = 2000
    show_bottom_button = True
    bottom_name_text = ""
    bottom_shuffle_timer = pygame.time.get_ticks()
    bottom_shuffle_interval = 30
    delay_bottom_button = True
    bottom_button_delay_timer = 0
    bottom_button_delay_wait = 1500
    top_button_target_text = "Choose Your Player"
    top_font = pygame.font.Font("resources/fonts/arial.ttf", 48)
    top_rect = None
    reveal_overlay_active = False
    shuffling = False # Start with shuffling off
    direct_reveal = False
    top_button_scramble_timer = pygame.time.get_ticks()
    top_button_scramble_delay = 100
    top_button_scramble_index = 0
    top_button_static_text = ""
    initial_typing_done = False
    shuffle_playing = False
    waiting_to_start = False # Initialize as False, will become True after initial typing
    placeholder_visible = True # New flag for placeholder visibility
    placeholder_blink_timer = 0 # Timer for blinking
    placeholder_blink_interval = 500 # Blink every 500 milliseconds
    placeholder_rect = None # Define placeholder_rect outside the conditional
    overlay_bottom_rect = None # Define overlay_bottom_rect outside the conditional

    # Play background hum (loop indefinitely)
    if background_hum:
        background_hum.play(-1)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_RETURN:
                if waiting_to_start:
                    waiting_to_start = False # Start shuffling on ENTER
                    shuffling = True
                elif shuffling and not displaying_names:
                    selected_name = reveal_names[current_reveal_index % len(reveal_names)]
                    direct_reveal = True
                    shuffling = False
                    reveal_overlay_active = True
                    # Stop shuffle sound
                    if shuffle_sound and shuffle_playing:
                        shuffle_sound.stop()
                        shuffle_playing = False
                    # Play reveal sound
                    if reveal_sound:
                        reveal_sound.play()
                    # Play scan sound briefly before reveal (optional)
                    # if scan_sound:
                    #     scan_sound.play()
                elif waiting_for_next_round_input:
                    waiting_for_next_round_input = False
                    direct_reveal = False
                    reveal_overlay_active = False
                    background.fill((0, 0, 0))
                    matrix_lines = []
                    used_columns.clear()
                    for _ in range(num_columns):
                        add_line(matrix_lines, matrix_font, background, num_columns, used_columns)
                    current_reveal_index = (current_reveal_index + 1)
                    shuffling = False # Reset shuffling for the next round, will be turned on after delay
                    delay_bottom_button = True
                    bottom_button_delay_timer = 0
                    bottom_name_text = ""
                    shuffle_playing = False # Reset shuffle playing flag
        current_time = pygame.time.get_ticks()
        to_remove = []
        for i, (line, col_idx) in enumerate(matrix_lines):
            if not line.update(background):
                to_remove.append(i)
        for i in sorted(to_remove, reverse=True):
            _, col_idx = matrix_lines[i]
            del matrix_lines[i]
            used_columns.discard(col_idx)
        if len(matrix_lines) < 100 and randint(0, 10) > 8:
            add_line(matrix_lines, matrix_font, background, num_columns, used_columns)

        # === Top Button Typing Animation (Initial Only) ===
        if not initial_typing_done:
            if top_button_scramble_index < len(top_button_target_text):
                if current_time - top_button_scramble_timer > top_button_scramble_delay:
                    top_button_scramble_timer = current_time
                    top_button_static_text += top_button_target_text[top_button_scramble_index]
                    top_button_scramble_index += 1
                    if top_button_scramble_index >= len(top_button_target_text):
                        initial_typing_done = True
                        bottom_button_delay_timer = current_time
                        waiting_to_start = True # Set waiting_to_start to True after typing
            else:
                initial_typing_done = True
                waiting_to_start = True # Ensure it's True if typing finishes instantly

        top_text_surface = top_font.render(top_button_static_text, True, (0, 250, 0))
        top_rect = top_text_surface.get_rect(center=(screen_width // 2, screen_height // 2 - 60))
        overlay_top = pygame.Surface((top_rect.width + 200, top_rect.height + 80), pygame.SRCALPHA)
        overlay_top.fill((0, 0, 0, 200))
        background.blit(overlay_top, top_rect.inflate(100, 40))
        draw_glowing_text(background, top_button_static_text, top_font, top_rect.center, (0, 250, 0), (0, 255, 100))

        # Draw the persistent box
        if overlay_bottom_rect:
            static_glow_color = (0, 255, 100)
            pygame.draw.rect(background, static_glow_color, overlay_bottom_rect, 2)

        if not direct_reveal:
            if waiting_to_start and initial_typing_done: # Only show placeholder after typing
                placeholder_font = pygame.font.Font("resources/fonts/arial.ttf", 40)
                placeholder_text_surface = placeholder_font.render("Press ENTER to start", True, (0, 250, 0))
                placeholder_rect = placeholder_text_surface.get_rect(center=(screen_width // 2, screen_height // 2 + 60))
                overlay_bottom = pygame.Surface((int(screen_width * 0.8), placeholder_rect.height + 80), pygame.SRCALPHA)
                overlay_bottom.fill((0, 0, 0, 200))
                background.blit(overlay_bottom, (screen_width // 2 - overlay_bottom.get_width() // 2, placeholder_rect.top - 40))
                overlay_bottom_rect = (screen_width // 2 - overlay_bottom.get_width() // 2, placeholder_rect.top - 40, overlay_bottom.get_width(), overlay_bottom.get_height()) # Store the rect

                # Blinking effect for the text
                if current_time - placeholder_blink_timer > placeholder_blink_interval:
                    placeholder_blink_timer = current_time
                    placeholder_visible = not placeholder_visible # Toggle text visibility

                glow_color = (0, 255, 100) # The brighter green for the text

                if placeholder_visible:
                    draw_glowing_text(background, "Press ENTER to start", placeholder_font, placeholder_rect.center, glow_color, glow_color)
            elif shuffling and not delay_bottom_button and not waiting_to_start:
                bottom_name_text = choice(names)
                bottom_shuffle_timer = current_time
                bottom_font = pygame.font.Font("resources/fonts/arial.ttf", 60)
                bottom_text_surface = bottom_font.render(bottom_name_text, True, (0, 255, 100)) # Use the brighter green here!
                bottom_rect = bottom_text_surface.get_rect(center=(screen_width // 2, screen_height // 2 + 60))
                overlay_bottom = pygame.Surface((int(screen_width * 0.8), bottom_rect.height + 80), pygame.SRCALPHA)
                overlay_bottom.fill((0, 0, 0, 200))
                background.blit(overlay_bottom, (screen_width // 2 - overlay_bottom.get_width() // 2, bottom_rect.top - 40))
                if overlay_bottom_rect: # Redraw the persistent box on top
                    pygame.draw.rect(background, static_glow_color, overlay_bottom_rect, 2)
                draw_glowing_text(background, bottom_name_text, bottom_font, (screen_width // 2, bottom_rect.centery), (0, 250, 0), (0, 255, 100))
                # Play the shuffle sound and set the flag if it's not already playing
                if shuffle_sound and not shuffle_playing:
                    shuffle_sound.play(-1) # Loop the shuffle sound
                    shuffle_playing = True
                # Play occasional glitch sound
                if glitch_sound and randint(0, 100) == 0:
                    glitch_sound.play()
            # Stop shuffle sound if shuffling is no longer true
            elif shuffle_sound and shuffle_playing and not shuffling:
                shuffle_sound.stop()
                shuffle_playing = False
            if initial_typing_done and delay_bottom_button and not waiting_to_start:
                if current_time - bottom_button_delay_timer > bottom_button_delay_wait:
                    delay_bottom_button = False
                    shuffling = True # Start shuffling after the delay
            if not waiting_to_start and overlay_bottom_rect:
                static_glow_color = (0, 255, 100)
                pygame.draw.rect(background, static_glow_color, overlay_bottom_rect, 2)
            if not waiting_to_start and initial_typing_done:
                bottom_font = pygame.font.Font("resources/fonts/arial.ttf", 60)
                bottom_text_surface = bottom_font.render(bottom_name_text, True, (0, 250, 0)) # This is for after shuffling stops but before reveal
                bottom_rect = bottom_text_surface.get_rect(center=(screen_width // 2, screen_height // 2 + 60))
                overlay_bottom = pygame.Surface((int(screen_width * 0.8), bottom_rect.height + 80), pygame.SRCALPHA)
                overlay_bottom.fill((0, 0, 0, 200))
                background.blit(overlay_bottom, (screen_width // 2 - overlay_bottom.get_width() // 2, bottom_rect.top - 40))
                if overlay_bottom_rect: # Redraw the persistent box on top
                    pygame.draw.rect(background, static_glow_color, overlay_bottom_rect, 2)
                draw_glowing_text(background, bottom_name_text, bottom_font, (screen_width // 2, bottom_rect.centery), (0, 250, 0), (0, 255, 100))
        else:
            bottom_font = pygame.font.Font("resources/fonts/arial.ttf", 60)
            revealed_surface = bottom_font.render(selected_name, True, (0, 255, 100))
            revealed_rect = revealed_surface.get_rect(center=(screen_width // 2, screen_height // 2 + 60))

            # Create overlay_reveal with the same dimensions and position as the persistent box
            if overlay_bottom_rect:
                overlay_reveal = pygame.Surface((overlay_bottom_rect[2], overlay_bottom_rect[3]))
                overlay_reveal.fill((0, 0, 0))
                background.blit(overlay_reveal, (overlay_bottom_rect[0], overlay_bottom_rect[1]))

                # Redraw the persistent box on top of the opaque overlay
                static_glow_color = (0, 255, 100)
                pygame.draw.rect(background, static_glow_color, overlay_bottom_rect, 2)
            else:
                # Fallback if overlay_bottom_rect is not yet defined (shouldn't happen after the first "Press ENTER")
                overlay_reveal_width = revealed_rect.width + 250
                overlay_reveal_height = revealed_rect.height + 80
                overlay_reveal = pygame.Surface((overlay_reveal_width, overlay_reveal_height))
                overlay_reveal.fill((0, 0, 0))
                background.blit(overlay_reveal, (screen_width // 2 - overlay_reveal.get_width() // 2, revealed_rect.top - 40))

            background.blit(revealed_surface, revealed_rect)
            waiting_for_next_round_input = True
        screen.blit(background, (0, 0))
        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()