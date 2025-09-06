input = str(input())
"""
Input: "You are very stupid"

2 first character: "Yo" -> [0], [1]
2 last character: "id" ) -> [-1]. [-2]

Output: "Yoid"
"""

print(input[0:2] + input[-1:-3])

"""
a = str("Hello")

print(a[0:3])

Output: 

a[0:5] = 0 -> 4 ":" 
"""