def mix_strings(s1, s2):
    result = []
    len1, len2 = len(s1), len(s2)
    max_len = max(len1, len2)
    for i in range(max_len):
        if i < len1:
            result.append(s1[i])
        if i < len2:
            result.append(s2[-(i+1)])
    return ''.join(result)

# Example usage
s1 = "Abc"
s2 = "Xyz"
print(mix_strings(s1, s2))  # Output: AzbycX
