#Set  creation
Days={"Monday","Tuesday","Wednesday"}
print(Days)
# Add function adds a single element in set.
Days.add("Thursday")
# Update function adds a multiple elements in set.
Days.update(["Friday","Saturday","Sunday"])
print(Days)
# Discard function remove an element but does not show any error if element not found.
Days.discard("July")
# Remove function removes an element but show error if element not found.
Days.remove("Sunday")
print(Days)
#Union combine two sets into a new one.
Day1={"Monday","Tuesday","Wednesday"}
Day2={"Friday","Saturday","Sunday"}
Day=Day1.union(Day2)
print(Day)
#Pop operation removes last element from tuple
Day.pop()
print(Day)