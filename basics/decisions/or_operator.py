print("what type of adventure should I have?")
adventure = input()
# identify adventure type
if (adventure == 'scary') or (adventure == 'short'):
    print("Entering the dark forest!")
elif (adventure == 'safe') or (adventure == 'long'):
    print("Taking the safe route!")
else:
    print("Not sure which route to take.")

