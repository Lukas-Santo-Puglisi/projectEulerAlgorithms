class CustomClass:
    def __eq__(self, other):
      
        print("hello")
        return True
    
    def __str__(self):
        return "love and peace"

myInstance = CustomClass()

print(str(CustomClass()))
