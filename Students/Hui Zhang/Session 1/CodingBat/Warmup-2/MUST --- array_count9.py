def array_count9(nums):
    count1 = 0
    for i in range(len(nums)):
        if 9 - nums[i] == 0:
            count1 = count1 + 1
    return(count1)

