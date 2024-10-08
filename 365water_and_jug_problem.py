class Solution:
    temp_dict = {}
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        self.temp_dict = {}
        return self.my_method(jug1Capacity, jug2Capacity, 0, 0, targetCapacity)

    def my_method(self, jug1Capacity: int, jug2Capacity: int, jug1_status: int, jug2_status: int, targetCapacity: int) -> bool:
        key = str(jug1_status) + "-" + str(jug2_status)
        if self.temp_dict.get(key) is not None:
            return False
        if jug1_status == targetCapacity or jug2_status == targetCapacity or jug1_status + jug2_status == targetCapacity:
            return True
        
        self.temp_dict[key] = 1
        temp_result = self.my_method(jug1Capacity, jug2Capacity, 0, jug2_status, targetCapacity)
        if temp_result:
            return True
        temp_result = self.my_method(jug1Capacity, jug2Capacity, jug1Capacity, jug2_status, targetCapacity)
        if temp_result:
            return True
        temp_result = self.my_method(jug1Capacity, jug2Capacity, jug1_status, 0, targetCapacity)
        if temp_result:
            return True
        temp_result = self.my_method(jug1Capacity, jug2Capacity, jug1_status, jug2Capacity, targetCapacity)
        if temp_result:
            return True
        temp_jug1_status = jug1_status
        temp_jug2_status = jug2_status
        diff = jug2Capacity - jug2_status
        if diff >= jug1_status:
            temp_jug1_status = 0
            temp_jug2_status = jug1_status + jug2_status
        else:
            temp_jug1_status = jug1_status - diff
            temp_jug2_status = jug2Capacity
        temp_result = self.my_method(jug1Capacity, jug2Capacity, temp_jug1_status, temp_jug2_status, targetCapacity)
        if temp_result:
            return True
        diff = jug1Capacity - jug1_status
        if diff >= jug2_status:
            temp_jug1_status = jug1_status + jug2_status
            temp_jug2_status = 0
        else:
            temp_jug1_status = jug1Capacity
            temp_jug2_status = jug2_status - diff
        temp_result = self.my_method(jug1Capacity, jug2Capacity, temp_jug1_status, temp_jug2_status, targetCapacity)
        if temp_result:
            return True
        return False