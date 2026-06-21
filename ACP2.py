
scores = [10, 20, 30, 40, 50]
 

#PART 1: Two-Pointer Swap")
print("Original Scores:", scores)
 
start = 0
end = len(scores) - 1
 
while start < end:
    scores[start], scores[end] = scores[end], scores[start]
    start = start + 1
    end = end - 1
 
print("Reversed Scores:", scores)
 

scores = [1, 2, 3, 4, 5, 6, 7, 8]
group_size = 3
 

#PART 2: Reverse in Groups")
print("Original Scores:", scores)
print("Group Size:", group_size)
 
i = 0
 
while i < len(scores):
    start = i
    end = min(i + group_size - 1, len(scores) - 1)
 
    while start < end:
        scores[start], scores[end] = scores[end], scores[start]
        start = start + 1
        end = end - 1
 
    i = i + group_size
 
print("Scores After Group Reverse:", scores)
 
scores = [10, 20, 30, 40, 50]
 


print("Original Scores:", scores)
 
first_score = scores[0]
 
for i in range(len(scores) - 1):
    scores[i] = scores[i + 1]
 
scores[-1] = first_score
 
print("After Left Rotate by 1:", scores)
 

scores = [10, 20, 30, 40, 50, 60]
n = 2
 

print("Original Scores:", scores)
print("Rotate By:", n)
 
n = n % len(scores)
 
for rotation in range(n):
    first_score = scores[0]
 
    for i in range(len(scores) - 1):
        scores[i] = scores[i + 1]
 
    scores[-1] = first_score
 
print("After Left Rotate by n:", scores)
 
 
scores = [16, 17, 4, 3, 5, 2]
leaders = []
 
print("PART 5: Leaders in an Array")
print("Scores:", scores)
 
max_from_right = scores[-1]
leaders.append(max_from_right)
 
i = len(scores) - 2
 
while i >= 0:
    if scores[i] > max_from_right:
        max_from_right = scores[i]
        leaders.append(scores[i])
 
    i = i - 1
 
leaders.reverse()
 
print("Leaders:", leaders)
 
 

