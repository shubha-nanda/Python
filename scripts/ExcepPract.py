class TooYoungException(Exception):
     def __init__(self,arg):
         self.msg=arg
         

class TooOldException(Exception):
    def __init__(self,arg):
        print("Too Old to apply")


age=int(input("Enter age "))
try:
    if age < 18:
        raise TooYoungException("age")
        print("After exception")
    elif age > 60:
        raise TooOldException("age")
   

except TooYoungException:
  print("Too Young to apply")

