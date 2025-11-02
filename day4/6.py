#problem statement:
'''Ask user for password until correct ("secret")'''

#solution:
pwd=input("Give your password: ")
while pwd != 'secret':
    print("The password is wrong!!")
    pwd = input("Give your password:")
    
print("The password is correct ")
