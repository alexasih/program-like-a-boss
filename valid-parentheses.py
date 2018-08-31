class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_new = s
        check = ""
        if len(s) == 1:
            return False
        for elem in s:
            if elem in "[{(":
                if elem == "[":
                    check += "]"
                elif elem == "{":
                    check += "}"
                elif elem == "(":
                    check += ")"
                s_new = s[1:]
        for index in range(len(check)-1):
            if check[index] != s_new[index]:
                return False
        return True
