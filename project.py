import csv
with open('/Users/mac/Documents/work/python/project/csv/costs.csv', newline='') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=';')
     f = 0
     for row in spamreader:
        if not f:
            f = 1
            continue
        print(len(row))
        for i in range(len(row)):
            if i>0:
                print(row[i])
        # for i in range(len(row)):
        #     if i>0:
        #         if int(row[i])>0:
        #             print(row[i])
