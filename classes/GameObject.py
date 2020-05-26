import pygame

# Defining the class of the objects:


class GameObject:

    def __init__(self, image_path, x, y, width, height):
        object_image = pygame.image.load(image_path)
        # Scaling up the size of the object:
        self.image = pygame.transform.scale(object_image, (width, height))

        self.x_pos = x
        self.y_pos = y

        self.width = width
        self.height = height

    # Displaying the object:
    def draw(self, background):
        background.blit(self.image, (self.x_pos, self.y_pos))

# Defining the class fot the character:


class Hero(GameObject):

    speed = 10

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    # Defining the move direction:
    def move(self, direction, game_height):
        if direction > 0:
            self.y_pos -= self.speed
        elif direction < 0:
            self.y_pos += self.speed
        if self.y_pos >= game_height - self.height:
            self.y_pos = game_height - self.height

    # Defining the collision detection:
    def detect_collision(self, other_object):
        if self.y_pos > other_object.y_pos + other_object.height / 1.3:
            return False
        elif self.y_pos + self.height / 1.3 < other_object.y_pos:
            return False
        if self.x_pos > other_object.x_pos + other_object.width / 1.3:
            return False
        elif self.x_pos + self.width / 1.3 < other_object.x_pos:
            return False
        return True


# Defining the class fot the ennemies:
class NPC(GameObject):

    speed = 10

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    # Defining the move of the NPC:
    def move(self, game_width):
        if self.x_pos <= self.width:
            self.speed = abs(self.speed)
        elif self.x_pos >= game_width - self.width * 2:
            self.speed = -abs(self.speed)
        self.x_pos += self.speed