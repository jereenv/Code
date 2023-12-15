class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        s = set()
        e = set()
        for path in paths:
            s.add(path[0])
            e.add(path[1])
        
        return e.difference(s).pop()
        