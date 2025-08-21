import classTutorialBase
class Luffy(classTutorialBase.Human): 
    
    #Class Object Attribute
    #Same for any instance of a class
    #can be referenced later with either self.devilFruit or Luffy.devilFruit (this way is preferred)
    devilFruit = 'Gomu Gomu no Mi'

    #Init method for user defined attributes
    #methods are functions defined inside a class
    def __init__(self, name, age):
        classTutorialBase.Human.__init__(self)  # Call the parent class's init method
        print("I am a rubber human!")
        self.name = name
        self.age = age

    def gumgumpistol(self):
        print("Gum-Gum Pistol!")

    def kingofthepirates(self, food):
        print("I'm {}, and I'm gonna be King of the Pirates! I love {} btw".format(self.name, food))