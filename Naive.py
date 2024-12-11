def naive_string_matching(text, pattern):
    n = len(text)
    m = len(pattern)
    for i in range(n - m + 1):
        if text[i:i + m] == pattern:
            print(f"Pattern found at index {i}")
text = "15975364532156"
pattern = "321"
naive_string_matching(text, pattern)
