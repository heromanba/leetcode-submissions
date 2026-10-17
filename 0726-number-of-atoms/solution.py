class Solution:
    def countOfAtoms(self, formula: str) -> str:
        s = formula
        stack = []
        i = 0
        while i < len(s):
            if s[i] == '(':
                stack.append(s[i])
                i += 1
            elif s[i] == ')':
                multiple = 1
                i += 1
                if i<len(s) and s[i].isdigit():
                    # extract element count
                    multiple_str = ''
                    while i<len(s) and s[i].isdigit():
                        multiple_str+=s[i]
                        i+=1
                    multiple = int(multiple_str)
                top = stack.pop()
                tmp_stack = []
                while top != '(':
                    top[1] = top[1]*multiple
                    tmp_stack.append(top)
                    top = stack.pop()
                while tmp_stack:
                    stack.append(tmp_stack.pop())
            else:
                ele = s[i]
                assert ele.isupper()
                i += 1
                while i < len(s) and s[i].isalpha() and s[i].islower():
                    # extract element name
                    ele += s[i]
                    i += 1
                cnt = 1
                if i<len(s) and s[i].isdigit():
                    cnt_str = ''
                    while i<len(s) and s[i].isdigit():
                        # extract element count
                        cnt_str += s[i]
                        i+=1
                    cnt = int(cnt_str)
                stack.append([ele, cnt])
        ele_map = dict()
        for ele, cnt in stack:
            # aggregate count for same element
            if ele in ele_map:
                ele_map[ele] += cnt
            else:
                ele_map[ele] = cnt
        result = sorted(ele_map.items())
        return ''.join([item[0]+str(item[1] if item[1]>1 else '') for item in result])


