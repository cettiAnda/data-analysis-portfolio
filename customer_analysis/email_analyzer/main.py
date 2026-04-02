fhandle=open("mbox.txt")
mail_count=0
dict_mail={}
dict_hour={}
for line in fhandle:
   if line.startswith("From "):
        array=line.split()
        mail=array[1]
        hour=array[5][:2]
        if mail not in dict_mail:
            dict_mail[mail]=1
        else:
            dict_mail[mail]+=1
        if hour not in dict_hour:
            dict_hour[hour]=1
        else:
            dict_hour[hour]+=1
mail_list=list(dict_mail.items())
mail_list.sort(key= lambda x: x[1], reverse=True)
print(f"{'Email':<30} {'Email Sent':<10}")
print("-"*43)
for tupla in mail_list:
    el1 = tupla[0]
    el2 = tupla[1]
   
    print(f"{el1:<30} {el2:<10}")
print("\nThe user who sent the most emails is:", mail_list[0][0])
hour_list=list(dict_hour.items())
hour_list.sort(key= lambda x: x[1], reverse=True)
print(f"{'Hour':<10} {'Email Sent':<10}")
print("-"*22)
for tupla in hour_list:
    el1 = tupla[0]
    el2 = tupla[1]
   
    print(f"{el1:<10} {el2:<10}")
print("\nThe hour with the highest number of emails is:", hour_list[0][0])
