def create_abbreviation(name):
    parts = name.split()
    abbreviation = '.'.join([part[0] for part in parts[:-1]]) + '.' + parts[-1]
    return abbreviation

# Example usage
name1 = "Netaji Subhas Chandra Bose"
name2 = "Niren Dutta"
print(create_abbreviation(name1))  # Output: N.S.C.Bose
print(create_abbreviation(name2))  # Output: N.Dutta
