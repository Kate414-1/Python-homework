def top_3_chars(text):
    cleaned = []
    for ch in text:
        if ch != ' ':
            cleaned.append(ch.lower())

    freq = {}
    for ch in cleaned:
         if ch in freq:
             freq[ch] += 1
         else:
             freq[ch] = 1
    result = []
    used = set()
    for _ in range(3):
        best_ch = None
        best_count = -1
        for ch in cleaned:
            if ch in used:
                continue
            if freq[ch] > best_count:
                best_count = freq[ch]
                best_ch = ch
        if best_ch is None:
            break
        result.append((best_ch, best_count))
        used.add(best_ch)

    return result
print(top_3_chars("Hello World"))