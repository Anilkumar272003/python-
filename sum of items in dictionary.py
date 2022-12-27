def returnsum(mydict):
    list=[]
    for i in mydict:
        list.append(mydict[i])
    final=sum(list)
    return final
dict={'a':100,'b':200,'c':300}
print("sum:",returnsum(dict))
