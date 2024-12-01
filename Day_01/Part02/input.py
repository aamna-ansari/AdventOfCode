
with open("D:/AdventOFCode/Day_01/Part02/input.txt") as f:
    i = f.read().strip().split("\n")

left = []
right = []

for j in i:
    l, r = map(int, j.split())  
    left.append(l)                
    right.append(r)               

score = 0

for num in left:
    count_in_right = right.count(num)  
    score += num * count_in_right  

# Print the result
print("SimilarityScore:", score)
