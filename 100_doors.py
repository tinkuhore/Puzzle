'''
There are 100 doors in a row, all doors are initially closed. A person walks through all doors multiple times and toggle (if open then close, if close then open) them in the following way: 

In the first walk, the person toggles every door 

In the second walk, the person toggles every second door, i.e., 2nd, 4th, 6th, 8th, … 

In the third walk, the person toggles every third door, i.e. 3rd, 6th, 9th, … 

Likewise,

In the 100th walk, the person toggles the 100th door. 

Which doors are open in the end? 
'''


doors = ['C']*100
visit_count = [0]*100

for i in range(1, 101):
    # print("PASS = ", i)
    p = 1
    idx = i*p

    while idx <= 100:
        # print(idx, end=" ")
        visit_count[idx-1] += 1 #index of the door visited
        p += 1
        idx = i*p
    print()

print("No of visits in each door:")
print(visit_count)

for i in range(100):
    count = visit_count[i]

    if count % 2 == 1:
        doors[i] = 'O'

print("Final state of the doors:")
print(doors)

print(f"No of Closed doors = {doors.count('C')}")
print(f"No of Opened doors = {doors.count('O')}")

