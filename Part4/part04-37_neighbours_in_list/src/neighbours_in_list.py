def longest_series_of_neighbours(my_list: list) -> int:
    if not my_list:
        return 0
    
    max_len = 1
    current_len = 1
    
    for i in range(len(my_list) - 1):
        # Check if the absolute difference between neighbors is exactly 1
        if abs(my_list[i] - my_list[i+1]) == 1:
            current_len += 1
        else:
            # Sequence broken, reset current length
            current_len = 1
        
        # Update max_len if the current streak is the longest we've seen
        if current_len > max_len:
            max_len = current_len
            
    return max_len
my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
print(longest_series_of_neighbours(my_list))
    