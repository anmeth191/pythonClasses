"""class Bird():
    
    def __init__(self , bird_color , bird_country):
        self.color = bird_color
        self.country = bird_country
    
    
    def fly(self):
        print(f"This bird can fly high and is {self.color} color")
        
    def eat(self , food_type):
        print(f"This bird likes {food_type} and lives in {self.country}")
        

my_bird = Bird("Light Blue" , "Nicaragua")
my_bird.eat("Apples")
my_bird.fly()
#print(my_bird.country)
"""


class Coding():
    #creating my constructor or instances Variables
    
    def __init__(self , language , hours_practicing, is_easy):
        self.lang = language
        self.time = hours_practicing
        self.level = is_easy
        
    #create a instance Object that says if practicing is true says keep learning 
    def verify_learning(self):
        if self.level == True:
            print(f"Do not give up in learning {self.lang}")
        else:
            print(f"{self.lang} is an Important coding language ,  give it a try :)!!")
        
        
create_object = Coding("Python" , 1.5 , False)
create_object.verify_learning()