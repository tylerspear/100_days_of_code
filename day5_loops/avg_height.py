heights = input("Input a list of heights ").split()

for n in range(0, len(heights)):
    heights[n] = int(heights[n])
print(heights)

total = 0
for height in heights:
    total += height
print("Total of heights is: ", total)
avg = total/len(heights)
print("The average of the heights is: ", avg)