class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        """ res = []
            curr_line = []
            width = 0
            i = 0
            while i < len(words):
                if len(words[i]) + width <= maxWidth:
                    width += len(words[i]) + 1
                    curr_line.append(words[i])
                    i+= 1
                else:
                    spaces = maxWidth - width + len(curr_line)

                    added = 0
                    j = 0
                    while added < spaces:
                        if j >= len(curr_line) - 1:
                            j = 0
                        curr_line[j] += " "
                        added += 1
                        j += 1

                    res.append("".join(curr_line))
                    curr_line = []
                    width = 0
            for i in range(len(curr_line) - 1):
                curr_line[i] += " "

            spaces = maxWidth - width + 1
            curr_line[-1] += " " * spaces

            res.append("".join(curr_line))
            return res"""

        res, cur, num_of_letters = [], [], 0
        for w in words:
            if num_of_letters + len(w) + len(cur) > maxWidth:
                for i in range(maxWidth - num_of_letters):
                    cur[i%(len(cur)-1 or 1)] += ' '
                res.append(''.join(cur))
                cur, num_of_letters = [], 0
            cur += [w]
            num_of_letters += len(w)
        return res + [' '.join(cur).ljust(maxWidth)]

        