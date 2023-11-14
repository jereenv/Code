class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        
        
        def get_manhattan_distance(loc1, loc2):
            return abs(loc1[0] - loc2[0]) + abs(loc1[1] - loc2[1])
        
        combinations = []
        for worker, worker_loc in enumerate(workers):
            for bike, bike_loc in enumerate(bikes):
                distance = get_manhattan_distance(worker_loc, bike_loc)
                combinations.append((distance, worker, bike))
                
        combinations.sort()
        
        bike_stat = [False] * len(bikes)
        worker_stat = [-1] * len(workers)
        
        pair_count = 0
        for distance, worker, bike in combinations:
            if worker_stat[worker] == -1 and not bike_stat[bike]:
                bike_stat[bike] = True
                worker_stat[worker] = bike
                pair_count += 1
                
                if pair_count == len(workers):
                    break
        return worker_stat
                
                
        