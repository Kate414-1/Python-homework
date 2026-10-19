def longest_run(seq):
    if not seq:
        return 0, None
    best_len = 0
    best_val = None
    cur_len = 1
    cur_val = seq[0]
    for i in range(1, len(seq)):
        if seq[i] == cur_val:
            cur_len += 1
        else:
            if cur_len > best_len:
                best_len = cur_len
                best_val = cur_val
            cur_val = seq[i]
            cur_len = 1
    if cur_len > best_len:
        best_len = cur_len
        best_val = cur_val
    return best_len, best_val

print(longest_run([1,1,1,2,2,3,3,3,3]))