# # grep stringtesttesttest
str1="testing is the procedure to test an application and to test the performance"
new_list=str1.split(' ')
for i in range(len(new_list)):
    if new_list[i]=='test':
        start_index=i
        break
if len(new_list)>start_index:
    new_string=new_list[start_index+1:]
    end_index=new_string.index('test')
    final_string=' '.join(new_string[:end_index])
    print(final_string)
