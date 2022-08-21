'''
Given a string s, find the first non-repeating characters
in it and return its index.  If it does not exist, return -1

{
    l: (1, 0)
    e: (3, 1)
    t: (1, 3)
    c: (1, 4)
    o: (1, 5)
    d: (1, 6)
}
'''
# dictionary in python3.7 and above is in ordered
def firstUniqChar(s):
    hash_map = {}
    for c in s:
        if c not in hash_map:
            hash_map[c] = 1
        else:
            hash_map[c] += 1

    for k, v in hash_map.items():
        if v == 1:
            return s.index(k)

    return -1




s1 = "leetcode"
s2 = "loveleetcode"
s3 = ""
s4 = "aabb"

print(firstUniqChar(s1))
print(firstUniqChar(s2))
print(firstUniqChar(s3))
print(firstUniqChar(s4))

'''
E: no result => return -1
empty string? => return -1

'''