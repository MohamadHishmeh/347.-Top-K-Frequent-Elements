from collections import defaultdict
ans = {}

strs = ["eat","tea","tan","ate","nat","bat"]

for s in strs:
            count = [0] * 26
            print("hey",count)
            for c in s:
                count[ord(c) - ord("a")] += 1
                print("hey",count)
            break
        