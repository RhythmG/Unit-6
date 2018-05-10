#Stephen Wang
#5/10/18
#how many words there are for each numbers of letters in the dictionary file

file = open('engmix.txt')
nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for line in file:
    for i in range(1, 23):
        if len(line) == i:
            nums[i-1] += 1
            
print(nums)
        
            
