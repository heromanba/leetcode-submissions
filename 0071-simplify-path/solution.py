class Solution:
    def simplifyPath(self, path: str) -> str:
        path_splitted = path.split('/')
        result = []
        for path in path_splitted:
            if not path or path == '.':
                continue
            if path == '..':
                if result:
                    result.pop()
            else:
                result.append(path)
        return '/' + '/'.join(result)
