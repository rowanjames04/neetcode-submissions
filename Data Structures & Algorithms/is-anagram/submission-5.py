class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_dict = defaultdict(int)

        for c in s:
            char_dict[c] += 1

        for c in t:
            char_dict[c] -= 1
        
        for val in char_dict.values():
            if val != 0:
                return False

        return True