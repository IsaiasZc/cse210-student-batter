from game import constants
from game.action import Action
from game.point import Point

class MoveActorsAction(Action):
    """A code template for moving actors. The responsibility of this class of
    objects is move any actor that has a velocity more than zero.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        for group in cast.values():
            for actor in group:
                if not actor.get_velocity().is_zero():
                    self._move_actor(actor)

    def _move_actor(self, actor):
        """Moves the given actor to its next position according to its 
        velocity.
        Args:
            actor (Actor): The actor to move.
        """
        position = actor.get_position()
        velocity = actor.get_velocity()
        x1 = position.get_x() 
        y1 = position.get_y() 
        x2 = velocity.get_x() 
        y2 = velocity.get_y() 
        x = x1 + x2
        y = y1 + y2

        if actor.get_text() == "===========":
            # this is an exception for the paddle.
            if x > constants.MAX_X - 11:
                x = constants.MAX_X - 11
        else:
            if x > constants.MAX_X:
                x = constants.MAX_X

        if x < 0:
            x = 0
        
        if y > constants.MAX_Y:
            y = constants.MAX_Y
        elif y < 1:
            y = 1

        position = Point(x, y)
        actor.set_position(position)