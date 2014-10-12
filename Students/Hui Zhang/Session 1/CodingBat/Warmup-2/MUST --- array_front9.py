def array_front9(nums):
    n = len(nums)
    count1 = 0
    if n >= 4:
        for i in range(4):
            if 9 - nums[i] == 0:
                count1 = count1 + 1
        if count1 >= 1:
            return(True)
        else:
            return(False)
    else:
        for i in range(n):
            if 9 - nums[i] == 0:
                count1 = count1 + 1
        if count1 >= 1:
            return(True)
        else:
            return(False)
