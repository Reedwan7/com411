print("where should i look?")
look = input()
if look == "in the bedroom":
    print("where in the bedroom should I look?")
    bedroom_place = input()
    print("\n")
    if look == "under the bed":
        print("Found some shoes but no battery")
    else:
        print("Found some mess but no battery")
print("\n")
if look == "in the bathroom":
    print("where in the bathroom should I look?")
    bathroom_place = input()
    print("\n")
    if bathroom_place == "in the bathtub":
        print("Found a rubber duck but no battery")
    else:
        print("Found a wet surface but no battery")
