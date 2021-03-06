__author__="Ravi Teja"
def get_hcf(first,second):
    result=[]
    for tup1 in first:
        for tup2 in second:
            if tup1[0]==tup2[0]:
                if (tup1[1])>tup2[1]:
                    result.append(tup2)
                else:
                    result.append(tup1)
    return result



def get_lcm(first,second):
    result = []
    first_dict=dict(first)
    second_dict=dict(second)
    for key in (set(first_dict.keys()) | set(second_dict.keys())):
        if (key in first_dict.keys()) and (key in second_dict.keys()):
            result.append((key,max(first_dict[key],second_dict[key])))
        elif key in first_dict.keys():
            result.append((key,first_dict[key]))
        elif key in second_dict.keys():
            result.append((key,second_dict[key]))

    return sorted(result)

def multiply(first,second):
    result = []
    first_dict = dict(first)
    second_dict = dict(second)
    for key in (set(first_dict.keys()) | set(second_dict.keys())):
        if (key in first_dict.keys()) and (key in second_dict.keys()):
            result.append((key, first_dict[key]+ second_dict[key]))
        elif key in first_dict.keys():
            result.append((key, first_dict[key]))
        elif key in second_dict.keys():
            result.append((key, second_dict[key]))

    return sorted(result)



