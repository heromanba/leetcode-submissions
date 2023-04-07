class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        uam = dict()
        for u_id, t_min in logs:
            if u_id not in uam:
                uam[u_id] =  { t_min }
            else:
                uam[u_id].add( t_min )
        for u_id, t_min in uam.items():
            uam[u_id] = len(t_min)
        t_to_uid = dict()
        for u_id, t_min in uam.items():
            if t_min not in t_to_uid:
                t_to_uid[t_min] = [ u_id ]
            else:
                t_to_uid[t_min].append(u_id)
        ret = [0] * k
        for t_min, u_id in t_to_uid.items():
            ret[t_min-1] = len(u_id)
        return ret
