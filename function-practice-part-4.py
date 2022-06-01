# 1) Find the maximum of three numbers.
def max_num(num_1, num_2, num_3):
    large_num = 0
    nums = [num_1, num_2, num_3]
    for n in nums:
        if n > large_num:
            large_num = n
    return(large_num)
# print(max_num(22, 5, 226))


# 2) Multiply all the numbers in a list.
def mult_list(my_list):
    if len(my_list) == 0:
        return("The list is empty...")
    
    total = my_list[0]

    if len(my_list) == 1:
        return(total)
    
    else:
        for n in my_list[1:]:
            total = total * n
    return total
# print(mult_list([2, 10, 20]))


# 3) Reverse a string.
def rev_string(string, index=0):
    #If Empty String, return empty string.
    if len(string)==0:
        return(string)
    #Base Case (works for single character strings)
    elif index == len(string)-1:
        return string[0]
    #Recursive Case
    else:
        return string[-1-index] + rev_string(string, index+1)
# print(rev_string("Hello World!"))


# 4) Check whether a number falls in a given range.
def num_within(num, range_start, range_end):
    if num < range_start or num > range_end:
        return(False)
    else:
        return(True)
# print(num_within(11, 1, 10))


# 5) Prints out the first n rows of Pascal's triangle.
triangle = [[1],[1,1]]
def pascal(n):

    # Base Case
    if n < 1:
        print("invalid number of rows")

    elif n == 1:
        print(triangle[0])

    else:
        row_number = 2

        # Fill up correct number of rows in triangle
        while len(triangle) < n:
            row = []
            row_prev = triangle[row_number - 1]

            # Create correct row, then add to triangle 
            # (this row will be 1 longer than row before it)
            length = len(row_prev)+1
            for i in range(length):

            # 1st number is 1
                if i == 0:
                    row.append(1)

                # Intermediate nunmbers get added from previous rows
                elif i > 0 and i < length-1:
                    row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])

                # Last number is 1
                else:
                    row.append(1)
            triangle.append(row)
            row_number += 1

        # Print triangle
        for row in triangle:
            print(row)
# pascal(10)