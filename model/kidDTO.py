from model.kid import Kid


class KidByPositionDTO:
    def __init__(self,position:int,kid:Kid):
        self.position=position
        self.kid = kid