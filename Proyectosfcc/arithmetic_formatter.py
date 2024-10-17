def solution(sequence):
    

    while sequence:
        for i in sequence:
            n = i
        
            if i <= n:  
                sequence = sequence.remove(i)
                break
        return 'holas'    
        
        
    for x in sequence:
        n = x
        if x <= n:
            return False        
                
        return True


sequence = [1, 3, 2, 1]
print(solution(sequence))
