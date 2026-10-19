def find_most_similar(strings):
    best_s1 = None
    best_s2 = None
    min_diff = float('inf')
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            s1 = strings[i]
            s2 = strings[j]
            if len(s1) != len(s2):
                continue
            diff_count = 0
            for k in range(len(s1)):
                if s1[k] != s2[k]:
                    diff_count += 1
            if diff_count < min_diff:
                min_diff = diff_count
                best_s1 = s1
                best_s2 = s2
    if best_s1 is None:
        return None, None, None

    return best_s1, best_s2, min_diff

print(find_most_similar(["abcdef", "abcxef", "zzzzzz"]))
