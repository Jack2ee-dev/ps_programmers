def solution(p):

    def recur(p):
        if len(p) < 0:
            return ""

        u, v = "", ""
        isBalanced = False
        left, right = 0, 0
        for c in p:
            if isBalanced is False:
                u += c
                if c is "(":
                    left += 1
                elif c is ")":
                    right += 1

                if left == right:
                    isBalanced = True
            else:
                v += c

        if correct(u):
            recur(v)

    def correct(p):
        p_list = list(p)
        stack = []

        for c in p:
            if c == "(":
                stack.append(c)
            else:
                stack.pop()

        if stack:
            return False
        return True

    recur(p)
