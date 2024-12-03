with open("./day_02/day_02.txt") as fin:
    lines = fin.readlines()

def isSafe(report):
    inc = None
    for i in range(0, len(report) - 1):
        a, b = report[i], report[i + 1]
        diff = a - b
        if diff == 0 or abs(diff) > 3:
            return False
        elif diff > 0 and inc == None:
            inc = True
        elif diff < 0 and inc == None:
            inc = False
        elif (diff > 0 and not(inc)) or (diff < 0 and inc):
            return False
    return True    

cnt1 = 0
cnt2 = 0
for line in lines:
    report = line.strip().split(' ')
    report = [int(item) for item in report]
    # print(reports[0], reports[1])
    if isSafe(report):
        cnt1 += 1
        cnt2 += 1
        continue
    
    for i in range(0, len(report)):
        new_report = list(report)
        del new_report[i]
        if isSafe(new_report):
            cnt2 += 1
            break

print(cnt1, cnt2)