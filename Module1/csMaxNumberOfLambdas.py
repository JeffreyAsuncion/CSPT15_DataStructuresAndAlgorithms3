"""
Given a string text, you need to use the characters of text to form as many instances of the word "lambda" as possible.

You can use each character in text at most once.

Write a function that returns the maximum number of instances of "lambda" that can be formed.

Example 1:
Input: text = "mbxcdatlas"
Output: 1

Example 2:
Input: text = "lalaaxcmbdtsumbdav"
Output: 2

Example 3:
Input: text = "sctlamb"
Output: 0
"""

def csMaxNumberOfLambdas(text):
    lamb = list("lambda")
    counter = 0
    for i in range(len(lamb)):
        letter = lamb.pop()
        counter += text.count(letter)
            
    return counter // 6

# Example 1:
text1 = "mbxcdatlas"
print(csMaxNumberOfLambdas(text1))# Output: 1

# Example 2:
text2 = "lalaaxcmbdtsumbdav"
print(csMaxNumberOfLambdas(text2))# Output: 2

# Example 3:
text3 = "sctlamb"
print(csMaxNumberOfLambdas(text3))# Output: 0