while True:
    try:
        a = int(input("Enter 1st number: "))
        b = int(input("Enter 2nd number: "))
        print(a+b)
    except(ValueError):
        print("Opps; Worng keyword")
    else:
        break

# data = [i for i in range(1,21)]
# print(data)
# data = [i for i in range(1,21) if i != 2 == 0]
# print(data)