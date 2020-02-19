class Solution:
    def longestCommonPrefix(self, strs):
        prefix = ""
        # Unzip strs to get char matrix
        for char_tuple in zip(*strs):
            if len(set(char_tuple)) == 1:
                # All same
                prefix += char_tuple[0]
            else:
                break
        
        return prefix
