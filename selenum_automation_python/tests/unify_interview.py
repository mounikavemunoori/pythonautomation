
list1=[1, 2, 3, 4, 5, 6, 7,8, 9, 10]
list2=[ "Even " if x%2==0 else "Odd" for x in list1]
print(list2)

str1="Hello"
new_dict={}
for i in str1:
    new_dict[i]=str1.count(i)
print(new_dict)

str2="Madam"
rev_str2=""
for x in range(len(str2)-1, -1,-1):
    rev_str2+=str2[x]
print(rev_str2)
def convert(str1):
    pass

if str2.upper()==rev_str2.upper():
    print("palindrome")
else:
    print("Not a palindrome")
#
x=5
double=lambda x: x*2
print(double(x))
sum_of_two=lambda x,y: x+y
print(sum_of_two(6, 7))

# Input: exp = "[()]{}"
# Output: Valid

# Input: exp = "[(])"
# Output: Invalid
# for i in range(len(input)-1, -1, -1):
#     rev_str1+=input[i]
# print(rev_str1)
input="[()]{}"
rev_str1=input.replace("{}", "")
rev=''
for i in range(len(rev_str1)-1, -1, -1):
    rev+=rev_str1[i]
print(rev)
print(rev_str1)










