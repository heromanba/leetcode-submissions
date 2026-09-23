class Solution:
    def passwordStrength(self, password: str) -> int:
        pts_map = {
            c: 1 for c in 'abcdefghijklmnopqrstuvwxyz'
        }
        pts_map.update({
            c: 2 for c in 'abcdefghijklmnopqrstuvwxyz'.upper()
        })
        pts_map.update({
            c: 3 for c in '0123456789'
        })
        pts_map.update({
            c: 5 for c in '!@#$'
        })
        ret = 0
        for c in set(password):
            ret += pts_map[c]
        return ret
