def count_upper_lower(s):
    upper_count = sum(1 for c in s if c.isupper())
    lower_count = sum(1 for c in s if c.islower())
    return upper_count, lower_count


sample_string = "The quick Brown Fox"
upper, lower = count_upper_lower(sample_string)
print(f"No. of Upper case characters : {upper}")
print(f"No. of Lower case characters : {lower}")
