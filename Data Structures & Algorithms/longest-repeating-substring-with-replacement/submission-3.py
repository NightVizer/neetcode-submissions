class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        if s == 1:
            return 1
        if k == 0:
            current_letter = s[0]
            count = 1
            for indx in range(1, len(s)):
                if current_letter == s[indx]:
                    count += 1
                else:
                    max_len = max(max_len, count)
                    count = 1
                    current_letter = s[indx]

            return max(max_len, count)

        left_indx = 0
        right_indx = k
        count_of_letters = 0

        letters = {}

        for indx in range(right_indx + 1):
            letters[s[indx]] = 1 + letters.get(s[indx], 0)
            count_of_letters += 1

        while right_indx < len(s):
            if right_indx + 1 > len(s) - 1:
                if self.NoramalCountOfLetters(k, letters):
                    return max(max_len, count_of_letters)

            if self.NoramalCountOfLetters(k, letters):
                # всё впорялке k нас устраивает.
                max_len = max(max_len, count_of_letters)
                right_indx += 1
                count_of_letters += 1
                letters[s[right_indx]] = 1 + letters.get(s[right_indx], 0)
            else:
                # необходимо сократить левый индекс и словарь до допустимого k
                letters[s[left_indx]] -= 1
                left_indx += 1
                count_of_letters -= 1

        return max_len

    def NoramalCountOfLetters(self, k: int, letters: dict) -> bool:
        summ = sum(letters.values())
        max_count_of_letter = max(letters.values())
        diff = summ - max_count_of_letter
        if diff <= k:
            return True
        else:
            return False