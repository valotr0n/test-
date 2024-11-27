from itertools import combinations

def count_unique_elements(sets):
    total = 0
    n = len(sets)
    
    # Loop over all non-empty subsets of sets
    for mask in range(1, 1 << n):
        current_intersection = None
        first_set = True
        
        # Apply mask to select sets
        for j in range(n):
            if (mask >> j) & 1:
                if first_set:
                    current_intersection = sets[j].copy()
                    first_set = False
                else:
                    current_intersection &= sets[j]
        
        # Count number of bits in mask to determine inclusion/exclusion
        bits = bin(mask).count('1')
        
        if bits % 2 == 1:
            total += len(current_intersection)
        else:
            total -= len(current_intersection)
    
    return total

# Test the function
A = {1, 1, 1}
B = {1, 1, 1}
C = {1, 1, 1}
sets = [A, B, C]

result = count_unique_elements(sets)
print("Total:", result)
