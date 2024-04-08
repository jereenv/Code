class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        st = deque(students)
        sd = deque(reversed(sandwiches))
        
        t = len(st)
        
        n = t
        
        while n > 0:
            if st[-1] == sd[-1]:
                st.pop()
                sd.pop()
                n = len(st)
            else:
                st.appendleft(st.pop())
                n -= 1
        return len(st)
                
        