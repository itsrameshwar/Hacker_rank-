def minimumNumber(n, password):
    c=0
    # if n<6:
    #     return 6-n
    if any(i.isdigit() for i in password)==False:
        c+=1
    if any(i.isupper() for i in password)==False:
        c+=1
    if any(i.islower() for i in password)==False:
        c+=1
    if any(i in "!@#$%^&*()-+" for i in password)==False:
        c+=1
    return max(c,6-n)
