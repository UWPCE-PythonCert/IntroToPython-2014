def array123(nums):
    n = len(nums)
    if n < 3:
        return(False)
    elif n == 3:
        if nums[0] == 1 and nums[1] == 2 and nums[2] == 3:
            return(True)
        else:
            return(False) 
    elif n > 3:
        count1 = 0
        for i in range(0,n-2):
            if (nums[i] == 1) and (nums[i+1] == 2) and (nums[i+2] == 3):
                count1 = count1 + 1
        if count1 >= 1:
            return(True)
        else:
            return(False)
