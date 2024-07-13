
#https://www.youtube.com/watch?v=W45GoPbgXfk

#https://www.youtube.com/watch?v=zLCJM9OZGZE

#Input_Python_OR_ABCDE

string= input("Enter a string =")
length= len(string)

for i in range(length):
    for j in range(i+1):
        print(string[j], end= " ")
    print()