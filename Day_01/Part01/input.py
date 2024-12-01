
with open("D:/AdventOFCode/Day_01/Part01/input.txt") as f:
    i = f.read().strip().split("\n")
left = []
right = []

for line in i:
    l, r = map(int, line.split()) 
    left.append(l)                
    right.append(r)              

left.sort()
right.sort()

total_distance = sum(abs(l - r) for l, r in zip(left, right))

print("Total Distance:", total_distance)
