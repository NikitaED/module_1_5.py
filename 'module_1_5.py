immutable_var=1, "apple", 1.3,
print(immutable_var)
#immutable_var[1][1]="orange" #кортеж не поддерживает обращение по элементам
mutable_list=[1,2.3,"peach", False]
mutable_list[0]=2
mutable_list[1]=5.5
mutable_list[2]="orange"
mutable_list[3]=True
print(mutable_list)