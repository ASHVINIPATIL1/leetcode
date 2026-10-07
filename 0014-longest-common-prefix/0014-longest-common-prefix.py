class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        prefix = strs[0]  # keep the entire word as prefix -- gradually delete the last letter so we can find longest prefix

        for s in strs[1: ]:  # run from 1 --> n cause we already have 0 in prefix

            while not s.startswith(prefix):  # while the word dosnt start with prefix

                prefix = prefix[ :-1]  # delete the last letter of prefix

                if prefix == '':  # if the prefix becoms empty while deleting last letter
                    return ''  # return empty

        return prefix
