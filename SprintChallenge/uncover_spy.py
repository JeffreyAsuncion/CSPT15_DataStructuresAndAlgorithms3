"""
In a city-state of n people, there is a rumor going around that one of the n people is a spy for the neighboring city-state.

The spy, if it exists:

Does not trust anyone else.
Is trusted by everyone else (he's good at his job).
Works alone; there are no other spies in the city-state.
You are given a list of pairs, trust. Each trust[i] = [a, b] represents the fact that person a trusts person b.

If the spy exists and can be found, return their identifier. Otherwise, return -1.

Example 1:

Input: n = 2, trust = [[1, 2]]
Output: 2
Explanation: Person 1 trusts Person 2, but Person 2 does not trust Person 1, so Person 2 is the spy.
Example 2:

Input: n = 3, trust = [[1, 3], [2, 3]]
Output: 3
Explanation: Person 1 trusts Person 3, and Person 2 trusts Person 3, but Person 3 does not trust either Person 1 or Person 2. Thus, Person 3 is the spy.
Example 3:

Input: n = 3, trust = [[1, 3], [2, 3], [3, 1]]
Output: -1
Explanation: Person 1 trusts Person 3, Person 2 trusts Person 3, and Person 3 trusts Person 1. Since everyone trusts at least one other person, there is no spy.
Example 4:

Input: n = 3, trust = [[1, 2], [2, 3]]
Output: -1
Explanation: Person 1 trusts Person 2, and Person 2 trusts Person 3. However, in this situation, we don't have any one person who is trusted by everyone else. So we can't determine who the spy is in this case.
Example 5:
"""




"""
like GraphFindJudge.py
"""

def uncover_spy(n, trust):
    # base case
    if len(trust) < n-1:
        return -1
     # indegree ---> num of directed edges into a vertex == N-1
    # outdegree ---> num of directed edges from a vertex == 0
    
    # N+1 so not to go out of bounds, accounts for 0
    # create an indegree list       
    indegree = [0] * (n+1)
     # create an outdegree list
    outdegree = [0] * (n+1)
    
    # iterate over the trust and extract a and b
    for a, b in trust:
        outdegree[a] += 1
        indegree[b] += 1
     
    # iterate check indegree and outdegree    
    for i in range(1, n+1):
        if indegree[i] == n-1 and outdegree[i] == 0:
            return i
            
    # otherwise return -1 False        
    return -1