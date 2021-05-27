import csv

def int_list(lst):
    new_list = []
    for elem in lst:
        if elem=='':
            new_list.append(0)
        else:
            new_list.append(int(elem))
    return new_list

def lst2dict(lst):
    print(sum(lst))
    d = {'min':min(lst),'max':max(lst),'len':len(lst),'s':sum(lst),'avg':sum(lst)/len(lst)}
    return d

def listsdicts(lsts_name, lsts_data):
    dcts = []
    for i in range(len(lsts_name)):
        dct = {'name':lsts_name[i],'min':min(lsts_data[i]),'max':max(lsts_data[i]),'avg':sum(lsts_data[i])/len(lsts_data[i])}
        dcts.append(dct)
    return dcts


with open('c:/work/python/python-course-project/csv/costs.csv', newline='') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=';')
     f = 0
     name_list=[]
     list_data_list=[]
     for row in spamreader:
        if not f:
            f = 1
            continue
        name_list.append(row[0])
        row.pop(0)
        print(lst2dict(int_list(row)))
        data_list=[]
        for i in range(len(row)):
            if i>0:
                if row[i]!='':
                  print(row[i])
                  data_list.append(int(row[i]))
                else:
                  data_list.append(0)
        list_data_list.append(data_list)
print(list_data_list)

print(listsdicts(name_list,list_data_list))




