class Luffy(): 
    
    #Class Object Attribute
    #Same for any instance of a class
    devilFruit = 'Gomu Gomu no Mi'

    #Init method for user defined attributes
    #methods are functions defined inside a class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def gumgumpistol(self):
        print("Gum-Gum Pistol!")

    def kingofthepirates(self, food):
        print("I'm {}, and I'm gonna be King of the Pirates! I love {} btw".format(self.name, food))