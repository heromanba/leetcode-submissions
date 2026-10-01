class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        base = 29
        modulus = pow(10, 9)+7
        hash_b = 0
        for i in range(len(b)):
            hash_b = (hash_b*base + (ord(b[i])-ord('a'))) % modulus
        hash_a = 0
        found = False
        pow1 = pow(base, len(b)-1)
        i = 0
        limit = max(len(b)*2,len(a)*2)
        while not found and i <= limit:
            if i==0:
                for j in range(len(b)):
                    hash_a = (hash_a*base + (ord(a[j%len(a)])-ord('a'))) % modulus
            else:
                hash_a = (hash_a - (ord(a[(i-1)%len(a)])-ord('a')) * pow1) % modulus
                hash_a = (hash_a * base + ord(a[(i+len(b)-1)%len(a)])-ord('a')) % modulus
            # print(i, i+len(b)-1, a[i%len(a)], a[(i+len(b)-1)%len(a)], hash_a, hash_b)
            if hash_a == hash_b:
                found = True
                break
            i+=1
        return math.ceil((i+len(b))/len(a)) if found else -1
