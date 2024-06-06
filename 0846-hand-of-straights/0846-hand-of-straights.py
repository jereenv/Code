class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        
        if n % groupSize != 0:
            return False
        
        card_dic = Counter(hand)
        
        keys = list(card_dic.keys())
        
        keys.sort()
                
        for key in keys:
            curr = card_dic[key]
            
            if curr > 0:
                for i in range(groupSize):
                    if key + i not in card_dic or card_dic[key + i] < curr:
                        return False
                    card_dic[key + i] -= curr
        
        return True