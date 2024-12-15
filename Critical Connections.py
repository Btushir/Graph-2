"""
Approach1: create an adjacency list. Traverse the list and remove neighbor for each node one at a time.
 And see if the disconnected neighbor can be reached via BFS/DFS. TC: O(E * (v+E)).
 Another view is if a connection is part of a cycle, then it is not a critical connection.

 Approach2: Torjan method:
 it uses discovery array: it tells the natural order of DFS and the lowest array: earliest time node that is discovered in
 the DFS and that can be reached.
TC: O(V+E)
"""


class Solution:
    def dfs(self, current, parent, discovery_time, lowest_time):

        # BC
        # if the node is not discovered
        if discovery_time[current] != -1:
            return

            # what is the discovery time?
        discovery_time[current] = self.time
        lowest_time[current] = self.time
        self.time += 1

        # go to neighbors
        for ne in self.hmap[current]:
            if ne == parent:
                continue

            self.dfs(ne, current, discovery_time, lowest_time)
            # parent is check if the lowest value its baby is greater than its discovery time
            # this means parent is the only node using which the current node
            # can be reached.
            if lowest_time[ne] > discovery_time[current]:
                # critical connection
                self.ans.append([ne, current])

            # if the above condition not met it means the node can be reached by other nodes as well
            # updating the lowest path of parent means: there is some other path
            # using that I could be reached
            # current is the parent of ne
            # update the lowest time of parent (current)
            lowest_time[current] = min(lowest_time[current], lowest_time[ne])

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        discovery_time = [-1 for _ in range(n)]
        lowest_time = [-1 for _ in range(n)]
        self.ans = []
        self.time = 0

        # build the adjacency list
        self.hmap = {}
        for edge in connections:
            if edge[0] not in self.hmap:
                self.hmap[edge[0]] = []

            if edge[1] not in self.hmap:
                self.hmap[edge[1]] = []

            self.hmap[edge[0]].append(edge[1])
            self.hmap[edge[1]].append(edge[0])

        self.dfs(0, -1, discovery_time, lowest_time)

        return self.ans
