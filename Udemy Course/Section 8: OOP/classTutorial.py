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
        print("I'm {}, and I'm gonna be King of the Pirates! I love {}!!!".format(self.name, food))

    #special/dunder method (denoted by __ which will be called whenever a built in function asks for the str representation of an object)
    def __str__(self):
        return "I'm {}, a {} year old rubber human who ate the {}!".format(self.name, self.age, self.devilFruit)
    
    #special method for len() calls on objects
    def __len__(self):
        return self.age  # Returns the length of the Luffy object as its age
    
    #special method for del() calls on objects which actually removes the object from memory
    def __del__(self):
        print("Luffy has been deleted!")