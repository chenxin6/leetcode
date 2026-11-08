from typing import List


class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.child: list["TreeNode"] = []


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        my_map: dict[int, list[int]] = {}
        for a, b in prerequisites:
            if a not in my_map:
                my_map[a] = []
            my_map[a].append(b)
        res = []
        loop_flag = True
        excuted_set = set()
        while loop_flag:
            loop_flag = False
            for i in range(numCourses):
                if i in excuted_set:
                    continue
                temp_list = my_map.get(i, [])
                is_ok = True
                for j in temp_list:
                    if j not in excuted_set:
                        is_ok = False
                        break
                if not is_ok:
                    continue
                res.append(i)
                excuted_set.add(i)
                loop_flag = True
            if len(res) == numCourses:
                loop_flag = False
        if len(res) != numCourses:
            res = []
        return res


s = Solution()
print(s.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
