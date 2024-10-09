class Solution:
    def badSensor(self, sensor1: List[int], sensor2: List[int]) -> int:

        found = False
        for i in range(len(sensor1)):
            if found:
                if sensor1[i:] == sensor2[i-1:-1] and sensor2[i:] == sensor1[i-1:-1]:
                    return -1
                elif sensor1[i:] == sensor2[i-1:-1]:
                    return 2
                else:
                    return 1
            
            if sensor1[i] != sensor2[i]:
                found = True
        
        return -1