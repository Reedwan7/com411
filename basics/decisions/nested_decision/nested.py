# determine what type of cover.
print("what type of cover does the book have (hard/soft)?")
cover_type = input()
print("\n")
if cover_type == "soft":
    # determine if book is perfect bound.
    print("is the perfect bound(yes or no)?")
    perfect_bound = input()
    if perfect_bound == "yes":
        print("Soft covers with coils or stitches are great for short books")
    else:
        print("Soft cover, perfect bound books are very popular!")
else:
    print("Books with hard covers can be more expensive")