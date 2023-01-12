def luhn_algorithm(n):
    sum = 0
    for index, character in enumerate(str(n) [::-1]):
        if index%2==0:
            placeholder = int(character)*2
            if len(str(placeholder)) > 1:
                sum += int(str(placeholder)[0]) + int(str(placeholder)[-1])
            else:
                sum += int(str(placeholder)[0])
        else:
            sum += int(character)
    print(f"sum: {sum}")
    print("check digit:", 10-((sum%10)%10))
    print("original number:", str(n))
    print("full account number:", str(n)+str(10-((sum%10)%10)))
luhn_algorithm(7992739871)
