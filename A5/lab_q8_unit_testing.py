"""Question 8 unit tests"""

# Tommy May
# A01086435

"""
Test 1: if the two points of a line are the same point 
        eg: line_intersect([[0, 0], [0, 0]], [[1, 1], [1, 1]]) 

Test 2: if the two lines have different slopes so they meet at 1 point
        eg: line_intersect([[0, 0], [1, 1]], [[1, 2], [2, 4]])
    
Test 3: if the lines are coincident
        eg: line_intersect([[0, 0], [1, 1]], [[2, 2], [3, 3]]]
        
Test 4: if the lines are parallel and never meet up
        eg: line_intersect([[0, 0], [1, 1]], [[0, 1], [1, 2]]
"""
