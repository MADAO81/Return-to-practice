def check_number(num):
    while True:
        try:
            num = int(input("Enter the grade 1-100: "))
        except ValueError:
            print("Please enter a valid grade 1-100")
            continue
        if num >= 1 and num <= 100:
            return num
            break
        else:
            print('The grade must be in the range 1-100')
            
grade = check_number(input)
print(grade)