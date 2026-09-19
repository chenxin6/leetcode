from typing import List


class Solution:

    def compute(self, num_str1: str | int, num_str2: str | int, flag: str):
        if flag == "+":
            return int(num_str1) + int(num_str2)
        elif flag == "-":
            return int(num_str1) - int(num_str2)
        else:
            return int(num_str1) * int(num_str2)

    def diffWaysToCompute(self, expression: str) -> List[int]:
        if not expression:
            return []
        temp_res = self.my_method(expression)
        if temp_res is not None:
            return [temp_res]

        flag_index_list = []
        for i in range(len(expression)):
            if expression[i] not in "0123456789":
                flag_index_list.append(i)
        res = []
        for flag_index in flag_index_list:
            temp_res1 = self.diffWaysToCompute(expression[:flag_index])
            temp_res2 = self.diffWaysToCompute(expression[flag_index + 1 :])
            for i in temp_res1:
                for j in temp_res2:
                    res.append(self.compute(i, j, expression[flag_index]))
        return res

    def my_method(self, expression: str) -> int | None:
        flag = ""
        for i in expression:
            if i not in "0123456789":
                if not flag:
                    flag = i
                else:
                    return None
        if flag:
            temp_list = expression.split(flag)
            return self.compute(temp_list[0], temp_list[1], flag)
        else:
            return int(expression)


print(Solution().diffWaysToCompute("2*3-4*5"))
