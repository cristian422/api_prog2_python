class Kid:
    """
    def __init__(self,identification:str,name:str, age:int, gender:str):
        self.identification = identification
        self.name = name
        self.age = age
        self.gender = gender
    """

    def __init__(self, my_dict):
        for key in my_dict:
            setattr(self, key, my_dict[key])


