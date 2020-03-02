from collections import Counter


class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []
        len_word = len(words[0])    # The length of one word
        num = len(words)
        length = len(s)

        # The dictionary of words
        words_counter = Counter(words)

        ans = []

        for i in range(len_word):
            # define slide window
            left = i
            right = i

            cnt = 0     # The number of words in the slide window
            cur_words_counter = Counter()   # The dictionary of words in the slide window

            while right + len_word <= length:
                # Get the right word
                word = s[right: right + len_word]
                right += len_word

                cur_words_counter[word] += 1
                cnt += 1

                while cur_words_counter[word] > words_counter[word]:
                    left_word = s[left: left + len_word]
                    left += len_word
                    cur_words_counter[left_word] -= 1
                    cnt -= 1
                if cnt == num:
                    ans.append(left)

        return ans
