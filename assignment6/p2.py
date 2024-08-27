def store_toppers_details(toppers):
    for i in range(len(toppers)):
        toppers[i][1] += 5  # Example modification: Adding 5 marks to each topper
    return toppers

toppers = [['Alice', 95], ['Bob', 90], ['Charlie', 85]]
toppers = store_toppers_details(toppers)
for topper in toppers:
    print(f"{topper[0]}: {topper[1]}")
