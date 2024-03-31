def majority_element(nums):
    candidate = None
    count = 0
    
    for num in nums:
        if count == 0:
            candidate = num
        elif num == candidate:
            count += 1
        else:
            count -= 1
        
        verificationCount = nums.count(candidate)