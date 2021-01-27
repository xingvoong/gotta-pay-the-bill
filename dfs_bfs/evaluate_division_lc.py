'''
1. medium, graph, dfs, bfs.

2. problem statement

You are given an array of variable pairs equations
and an array of real numbers values,
where equations[i] = [Ai, Bi] and
values[i] represent the equation Ai / Bi = values[i].
Each Ai or Bi is a string that represents a single variable.

You are also given some queries,
where queries[j] = [Cj, Dj] represents the jth query
where you must find the answer for Cj / Dj = ?.

Return the answers to all queries.
If a single answer cannot be determined, return -1.0.

Note: The input is always valid.
You may assume that evaluating the queries will not result in division
by zero and that there is no contradiction.

Input: equations = [["a","b"],["b","c"]],
values = [2.0,3.0],
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation:
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]

3. solution in plain English or pseudocode
intuition: transfer the problem in a graph
step 1: build the graph
    where each variable is a node, an edge is an equal, the weight is the value

step 2: evaluate the query one by one:
    + use dfs:
        + we search by 2 node variables:
                base case
            + if 2 nodes does not exist:
                return -1
            + if 2 nodes exist:
                return edge weigh
            + if there is no direct edge between node 1 and node 2:
                + search through directed node from node 1 to find node 2
                    mark a node as visted
                    call dfs on node i and node 2
                    + if dfs returns - 1:
                        continue
                    else: return the chain products of edge weight

4: implementation

'''


def eval_division(equations, values, queries):

    import collections
    # step 1: build the graph
    graph = collections.defaultdict(dict)
    for (x, y), val in zip(equations, values):
        graph[x][y] = val
        graph[y][x] = 1 / val

    # step 2: dfs to explore the graph
    def dfs(x, y, visited):
        # base case
        if x not in graph or y not in graph:
            return -1
        if y in graph[x]:
            return graph[x][y]

        for i in graph[x]:
            if i not in visited:
                visited.add(i)
                temp = dfs(i, y, visited)
                if temp == -1:
                    continue
                else:
                    return graph[x][i] * temp
        return -1

    res = []
    for query in queries:
        res.append(dfs(query[0], query[1], set()))
    return res


equations1 = [["a", "b"], ["b", "c"]]
querries1 = [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
values1 = [0.5]
expected_output1 = [0.50000, 2.00000, -1.00000, -1.00000]

eq2 = [["a", "b"], ["b", "c"]]
querries2 = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
values2 = [2.0, 3.0]
expected_output2 = [6.0, 0.5, -1.0, 1.0, -1.0]

eq3 = [["a", "b"], ["b", "c"], ["bc", "cd"]]
q3 = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
value3 = [1.5, 2.5, 5.0]
expected_output3 = [3.75000, 0.40000, 5.00000, 0.20000]

assert eval_division(equations1, values1, querries1) == expected_output1
assert eval_division(eq2, values2, querries2) == expected_output2
assert eval_division(eq3, value3, q3) == expected_output3
