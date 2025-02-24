"""
There is an undirected tree with n nodes labeled from 0 to n - 1, rooted at node 0. You are given a 2D integer array edges of length n - 1 
where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

At every node i, there is a gate. You are also given an array of even integers amount, where amount[i] represents:

    the price needed to open the gate at node i, if amount[i] is negative, or,
    the cash reward obtained on opening the gate at node i, otherwise.

The game goes on as follows:

    Initially, Alice is at node 0 and Bob is at node bob.
    At every second, Alice and Bob each move to an adjacent node. Alice moves towards some leaf node, while Bob moves towards node 0.
    For every node along their path, Alice and Bob either spend money to open the gate at that node, or accept the reward. Note that:
        If the gate is already open, no price will be required, nor will there be any cash reward.
        If Alice and Bob reach the node simultaneously, they share the price/reward for opening the gate there. In other words, if the price to open the gate 
        is c, then both Alice and Bob pay c / 2 each. Similarly, if the reward at the gate is c, both of them receive c / 2 each.
    If Alice reaches a leaf node, she stops moving. Similarly, if Bob reaches node 0, he stops moving. Note that these events are independent of each other.

Return the maximum net income Alice can have if she travels towards the optimal leaf node.
"""


class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        # find bob's shortest path to 0
        dq, seen, min_path = deque([(bob, [])]), set(), []
        while dq:
            node, path = dq.pop()
            if node in seen:
                continue

            seen.add(node)
            path = path + [node]
            if node == 0:
                min_path = path
                break

            for n in adj[node]:
                dq.appendleft((n, path))
        seen_gates = {n: i for i, n in enumerate(min_path)}

        # find alice's max income
        seen = set()
        def dfs(node, level):
            if node in seen:
                return float("-inf")

            seen.add(node)
            max_path_income = float("-inf")
            for n in adj[node]:
                max_path_income = max(max_path_income, dfs(n, level + 1))

            gate_income = 0
            if seen_gates.get(node, float("inf")) > level:
                gate_income = amount[node]
            if seen_gates.get(node, float("inf")) == level:
                gate_income = amount[node] / 2

            return gate_income + max_path_income if max_path_income != float("-inf") else gate_income

        return int(dfs(0, 0))
