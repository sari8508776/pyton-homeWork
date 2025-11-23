# #region str s
# from fontTools.misc.cython import returns
# # ex1
# str='sari$6 HSLA89n'
# def clean(str):
#     for i in str:
#         if not i.isalpha() or not i.isalnum():
#           str = str.replace(i, '')
#     return str
# print(clean(str)
# )
# # ex2
# def popular(str):
#     count=0
#     word=""
#     str=str.splite()
#     for i in str:
#         # if(str)
# #endregion




#region homeWork_ex1
def analyze_list(list):
    dec={}
    x=set(list)
    dec[0]={"not again":x}
    sum=0
    list.sort()
    for i in list:
        sum +=i
    dec[1]={"avg":sum/len(list)}
    dec[2]={"max":list[0]}
    dec[3]={"min":list[len(list)-1]}




    return dec,
list=[1,2,2,3]
print(analyze_list(list))
#endregion

def filter_dict(d,theshold):
    list=[]
    for i in d:
        if d[i]>theshold:
            list.append(i)
    return list;


d={"ruti":388,"sari":8894390}
print(filter_dict(d,10000))
