class dog:
    tricks=[]
    def __init__(self,name):
        self.name=name
    def add_tricks(self,trick):
        self.tricks.append(trick)