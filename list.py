# grocery = ['deo','chicken','milk','eggs','sprouts','mug dal' , 199]
# print(grocery[6])
# numbers = [2,5,1,67,9,1]
# list_1 =['f','srinath']
# my_list = numbers[:] # this will ensure that my_list gets only the copy of the numbers

# a = numbers.sort() # its unnecessry to write a function for sorting insted of using the inbuit one
# b = numbers.reverse()
# print(numbers[1::2]) # but doing these actions wil not effect aur original iist
# print(numbers) # a & b has changed the original list
# print(numbers[0::-2])# we should not use  no.s less then -1 on 3rd either in str or in list
# print(max(numbers))
# print(min(numbers))
# print(len(numbers))
# numbers.append(91)
# numbers.insert(2,16) # 2 is the index where the number 16 is going to be insorted.
# numbers.remove(9) # 9 will get removed from the list
# numbers.pop() # this wi remove the end iteam from the list.
# numbers[1]=32
# print(numbers[2:]) #print elements starting from 3rd elements in the list
# print(numbers[1:3]) # print elements 2nd and 3rd
# print(numbers*2) # prints the list numbers twice
# print((numbers+list_1)) # provides such a list where there is elements of both numbers and list_1 ( respectivly)

# TUPPLES
# '''mutable - can change
# immutable- can't change'''
# tupple = (3,2,5,1,5)
# print(tupple)
# tp=(1,) # wee need to put a , after the charecter if u have one iteam in ur tupple
# print(tp)

# SWAPPING
# a = 1
# b =3
# a,b = b,a
# temp = a
# a=b
# b = temp
# print(a,b)
#-------------------------------------------------question----------------------------------------
# question to input 10 nums in a list and then display all the elements by multiplying 2
# print('Enter the elements of these list : ')
# lis =[]
# for i in range(0,5):
#     a = int(input())
#     lis.append(a*2)
# print(lis)