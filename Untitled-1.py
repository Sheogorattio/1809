def main():
    task1()
    task2()
    task3()
    task4()

def task1():
    length,width,height = int(input("Enter room lenght: ")), int(input("Enter room width: ")),int(input("Enter room height: "))
    if(length > 0 and width > 0 and height > 0):
        volume = length * width * height
        if(volume <=5):
            print("Size: small")
        elif(volume <= 10):
            print("Size: medium")
        else:
            print("Size: large")
    else:
        print("Invalid data")

def task2():
    length = int(input("Enter sequence length: "))
    f_num ,s_num, buf=0,1,0
    for i in range(length):
        print(f_num, end=", ")
        buf = f_num
        f_num += s_num
        s_num = buf
    print("\b\b.")

def task3():
    lst = []
    length = int(input("Enter sequence length: "))
    f_num ,s_num, buf=0,1,0
    for i in range(length):
        lst.insert(i,f_num)
        buf = f_num
        f_num += s_num
        s_num = buf
    for i in lst:
        print(i, end=", ")

    print("\b\b.")
        
def task4():
    lst = []
    length = int(input("Enter sequence length: "))
    f_num ,s_num, buf,even_conuter,odd_counter=0,1,0,0,0
    for i in range(length):
        if f_num%2 == 0 or f_num == 0:
            even_conuter+=1
        else:
            odd_counter+=1
        lst.insert(i,f_num)
        buf = f_num
        f_num += s_num
        s_num = buf
    for i in lst:
        print(i, end=", ")
    print("\b\b.")
    try:
        print(f"Even: {even_conuter/(odd_counter+even_conuter)*100}%\nOdd: {odd_counter/(odd_counter+even_conuter)*100}%")
    except:
        print("Something went wrong")

if __name__ == "__main__":
    main()
