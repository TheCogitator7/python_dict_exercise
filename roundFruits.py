#roundFruits.py

#example
#cherry is small but not green.
#pea is small and green.
#watermelon is not small but green.
#pumpkin is not small and not green.


round={
    "cherry": {
        "small": True,
        "green": False},
    "pea": {
        "small": True,
        "green": True},
    "watermelon": {
        "small": False,
        "green": True},
    "pumpkin": {
        "small": False,
        "green": False}
    }

for x, y in round.items():
    print(x)
    if y["small"] == True and y["green"] == True:
        print(x, "is small and green")
        print()
    elif y["small"] == True and y["green"] == False:
        print(x, "is small but not green")
        print()
    elif y["small"] ==False and y["green"] == True:
        print(x, "is not small but green")
        print()
    else:
        print(x, "is not small and not green")
        print()
        
        
                
    
