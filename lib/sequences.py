def print_fibonacci(length):
    # Start with an empty list
    fibonacci_list = []
    
    # Loop to generate the sequence
    for i in range(length):
        if i == 0:
            fibonacci_list.append(0)
        elif i == 1:
            fibonacci_list.append(1)
        else:
            # Sum of the previous two numbers
            fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])
    
    print(fibonacci_list)
