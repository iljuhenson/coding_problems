class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) > len(text2):
            dictText = text1
            sweepText = text2
        else:
            dictText = text2
            sweepText = text1

        # Build a dictionary containing a list of offsets for each character.
        # so,  for the string "aaa", dictOffset['a'] = [0, 1, 2]
        dictOffsets = {}
        for i, c in enumerate(dictText):
            entry = dictOffsets.get(c, [])
            entry.append(i)
            dictOffsets[c] = entry

        #array to hold the lowest offset so far for a given length.
        # The index of the array represents the size of the subsequence.
        #[0] = -1 to indicate we need to find the next character with lowest offset
        #[1] = lowest offset in dictText of 1 character match.
        #[2] = lowest offset in dictText of 2 character match.
        offsetAtLen = [-1]
        for c in sweepText:
            if c not in dictOffsets: # character is not found in the other string, skip it
                continue
            count_offsetAtLen = len(offsetAtLen)
            for subseq_len in reversed(range(count_offsetAtLen)): #Update the subseq_len from the end
                offset_list = dictOffsets[c]
                # See if this character can be appended fo the current offset
                index = bisect(offset_list, offsetAtLen[subseq_len])
                if index >= len(offset_list): 
                    continue  #Reaching this line means the character can't be used to grow the subsequence.
                # If we reach here the character can be appended, we need to increase the offset of the next subseq_len
                match_offset = offset_list[index]
                if offsetAtLen[subseq_len] <= match_offset:
                    if subseq_len == count_offsetAtLen - 1:
                        offsetAtLen.append(match_offset) # This entry grows the subseq_len
                    elif offsetAtLen[subseq_len+1] > match_offset:
                        offsetAtLen[subseq_len+1] = match_offset # This entry moves the offset for this substr_length "back" to a better spot
                
        return len(offsetAtLen)-1

if __name__ == "__main__":
    print(Solution().isMatch())