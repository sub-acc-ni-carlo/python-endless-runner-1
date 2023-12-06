class Sprite:
    
    """
    This class helps managing the animation of a character. 
    """

    def __init__(self, group_name=None, animation=[]):
        self.group_name = group_name
        self.animation = animation
        self.index = 0