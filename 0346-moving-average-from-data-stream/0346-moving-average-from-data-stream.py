class MovingAverage:

    def __init__(self, size: int):
        self.arr = deque()
        self.size = size
        self.sum = 0
        
        

    def next(self, val: int) -> float:
        self.arr.append(val)
        self.sum += val - (self.arr.popleft() if len(self.arr) > self.size else 0)
        return self.sum/len(self.arr)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)