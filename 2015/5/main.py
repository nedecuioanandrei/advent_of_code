def is_nice(s: str) -> bool:
    v_count = sum([s.lower().count(x) for x in "aeiou"])  
    if v_count < 3:
        return False

    ok = False
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            ok = True
    if not ok:
        return False

    return (s.lower().count("ab") == 0 
            and s.lower().count("cd") == 0 
            and s.lower().count("pq") == 0 
            and s.lower().count("xy") == 0)

# print(is_nice("ugknbfddgicrmopn"))
# print(is_nice("chzalrnumimnmhp"))
# print(is_nice("haegwjzuvuyypxyu"))
# print(is_nice("dvszwmarrgswjxmb"))

ans = 0
with open("in", "r") as f:
    lines = f.readlines()
    for line in lines:
        if is_nice(line):
            ans += 1
    print(ans)
