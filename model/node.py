from model.kid import Kid


class Node:
    def __init__(self,kid:Kid):
        self.data=kid
        self.next = None