class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        dic = Counter(students)
        
        for idx, val in enumerate(sandwiches):
            if dic[val] > 0:
                dic[val] -= 1
            else:
                return len(sandwiches) - idx
        return 0
            
                
        