import os
import random

from game.casting.actor import Actor
from game.casting.gems import Gem
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "The Greed Game"
WHITE = Color(255, 255, 255)
DEFAULT_GEMS_AND_STONES = 40


def main():
    
    # create the cast
    cast = Cast()
    
    # create the banner
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # create the robot
    x = int(MAX_X / 2)
    y = int(MAX_Y / 2)
    # y = 550 Uncomment this after the animation is working
    robot_position = Point(x, y)

    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(robot_position)
    cast.add_actor("robots", robot)

    # create the gems and stones
    for n in range(DEFAULT_GEMS_AND_STONES):
        gem_char = chr(42)
        stone_char = chr(48)

        # For gems
        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        gem_position = Point(x, y)
        position = gem_position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        gem = Gem()
        gem.set_text(gem_char)
        gem.set_font_size(FONT_SIZE)
        gem.set_color(color)
        gem.set_position(position)
        cast.add_actor("gems", gem)
        
        # For stones
        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        stone_position = Point(x, y)
        position = stone_position.scale(CELL_SIZE)
       
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)

        stone = Gem()
        stone.set_text(stone_char)
        stone.set_font_size(FONT_SIZE)
        stone.set_color(color)
        stone.set_position(position)
        cast.add_actor("stones", stone)

        score = Gem()
        score.get_points(gem_char, stone_char)
        score.get_message()
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()