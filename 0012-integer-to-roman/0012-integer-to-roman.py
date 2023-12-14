class Solution:
    def intToRoman(self, num: int) -> str:
        roman = []
        value_to_roman = [["M",1000],["CM",900],["D",500],["CD",400],["C",100],["XC",90],["L",50],["XL",40],["X",10],["IX",9],["V",5],["IV",4],["I",1]]
        
        for i in value_to_roman:
            while num >= i[1]:
                roman.append(i[0])
                num -= i[1]
        return "".join(roman)
        