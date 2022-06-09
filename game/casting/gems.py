
from game.casting.actor import Actor
from game.casting.cast import Cast

class Gem(Actor, Cast):
    """The responsibility of Artifact is to compute points.

        Attributes:
            _message (str): Message from messages.txt
    """
    def __init__(self):
        super().__init__()
        self.points = 0
        self.message = ""
       
    def get_points(self, gem, stone):
        
        point = 0
        if gem:
            point = 5
        elif stone:
            point = -5
        self.points += point
        return self.points


    def get_message(self):
        
        return f'Score: {self.points}'

    def set_message(self, message):
        self._message = message

