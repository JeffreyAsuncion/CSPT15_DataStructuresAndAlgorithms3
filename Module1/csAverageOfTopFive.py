"""
Given a list of different students' scores, 
write a function that returns the average of each student's top five scores. 
You should return the averages in ascending order of the students' id numbers.

Each entry (scores[i]) has the 
student's id number (scores[i][0]) and 
the student's score (scores[i][1]). 

The averages should be calculated using integer division.

Example 1:

Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
Explanation:
The average student `1` is `87`.
The average of student `2` is `88.6`, but with integer division is `88`.
Notes:

The score of the students is between 1 and 100.
"""

"""
Leetcode 1086
https://www.youtube.com/watch?v=3iqC5J4l0Cc"""

def csAverageOfTopFive(scores):
    result = []
    _lista = []
    _listb = []
    for i in range(len(scores)):
        for j in range(0, 2):
            #print(scores[i][j])
            if i == 0:
                _lista.append(scores[i][j])
            if i == 1:
                _listb.append(scores[i][j])
    _lista.sort(reverse=True)
    averageA = sum(_lista[:6])/5
    result.append([1, averageA])
    _listb.sort(reverse=True)
    averageB = sum(_listb[:6])/5
    result.append([2, averageB])


    return result


scores = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
print(csAverageOfTopFive(scores))#Output: [[1,87],[2,88]]
