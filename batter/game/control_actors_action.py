from game import constants
from game.action import Action
from game.point import Point

class ControlActorsAction(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def __init__(self, input_service):
        """The class constructor.
        
        Args:
            input_service (InputService): An instance of InputService.
        """
        self._input_service = input_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        direction = self._input_service.get_direction()
        paddle = cast["paddle"][0] # there's only one in the cast
        if self._can_move(paddle, direction):
            paddle.set_velocity(direction)
    
    def _can_move(self, cast, direction):
        move = True
        x = cast.get_position().get_x()
        left = Point(-1, 0)
        right = Point(1, 0)
        limit = constants.MAX_X - 11
        if x == limit and (direction.equals(right)):
            move = False
        elif x == 1 and direction.equals(left): # x == 1 and 
            move = False
        return move


        

