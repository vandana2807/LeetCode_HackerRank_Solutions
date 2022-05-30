import itertools
def pair_sum_or_less(nums, target):
  
    closest = []
    for i in itertools.combinations(nums, 2):
        if sum(i) == target:
            
            return list(i)
        else:
            if sum(i) < target:
                closest.append((target - sum(i), i))
    

    if closest == []:
        return [-1,-1]
    else:
       
        return list(min(closest)[1])
