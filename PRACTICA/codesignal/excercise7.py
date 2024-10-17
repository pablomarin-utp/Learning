def increasing(sequence):
    def can_be_increasing(seq, skip_index):
        # Helper function to check if seq can be increasing by skipping one element at skip_index
        return all(seq[i] < seq[i + 1] for i in range(len(seq) - 1) if i != skip_index and i + 1 != skip_index)
    
    n = len(sequence)
    if n <= 2:
        return True

    violation_index = -1
    
    for i in range(n - 1):
        if sequence[i] >= sequence[i + 1]:
            if violation_index != -1:  # More than one violation
                return False
            violation_index = i
    
    # No violations found, or we can remove one element to fix it
    if violation_index == -1:
        return True
    return (can_be_increasing(sequence, violation_index) or
            can_be_increasing(sequence, violation_index + 1))

# Ejemplo de uso
result1 = increasing([1, 2, 3, 1, 0])  # False
result2 = increasing([1, 3, 2, 1])     # False
result3 = increasing([1, 3, 2])        # True
result4 = increasing([1, 2, 3, 4])     # True
result5 = increasing([4, 3, 2, 1])     # False
result6 = increasing([1, 2, 5, 3, 4])  # True

result1, result2, result3, result4, result5, result6
