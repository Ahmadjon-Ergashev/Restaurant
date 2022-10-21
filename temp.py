def func(s, n):
    inx = 1
    if len(s)>=2 and float(s[:len(s)//2])+float(s[len(s)//2:]) == n:
        print(f"{float(s[len(s)//2:])}+{float(s[:len(s)//2])}", end="")
        return True
    elif len(s)>=2 and float(s[:len(s)//2])-float(s[len(s)//2:]) == n:
        print(f"{float(s[len(s)//2:])}-{float(s[:len(s)//2])}", end="")
        return True
    elif len(s)>=2 and float(s[:len(s)//2])*float(s[len(s)//2:]) == n:
        print(f"{float(s[len(s)//2:])}*{float(s[:len(s)//2])}", end="")
        return True
    elif len(s)>=2 and float(s[:len(s)//2])/float(s[len(s)//2:]) == n:
        print(f"{float(s[len(s)//2:])}/{float(s[:len(s)//2])}", end="")
        return True
    if len(s) > 2 and func(s[inx:], n-float(s[:inx])):
        print(f"+{float(s[:inx])}", end="")
        return True
    elif len(s) > 2 and func(s[inx:], n+float(s[:inx])):
        print(f"-{float(s[:inx])}", end="")
        return True
    elif len(s) > 2 and func(s[inx:], n/float(s[:inx])):
        print(f"*{float(s[:inx])}", end="")
        return True
    elif len(s) > 2 and (s[inx:], n*float(s[:inx])):
        print(f"/{float(s[:inx])}", end="")
        return True
    else:
        return False


func("1234", 9)
