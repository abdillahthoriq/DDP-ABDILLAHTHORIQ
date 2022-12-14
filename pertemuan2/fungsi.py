def greeting(hour = 1):
    if hour < 12:
        return "selamat pagi"
    elif hour < 18 :
        return "selamat sore"
    else:
        return "selamat malam"
    
print(greeting(7))


