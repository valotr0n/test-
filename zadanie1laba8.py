def IncTime(h,m,s,t):
    hInSeconds = h * 3600
    mInSeconds = m * 60
    totalSeconds = hInSeconds + mInSeconds + s + t
    Hours = totalSeconds // 3600
    Minutes = totalSeconds // 60
    Secundes = totalSeconds // 60
    return Hours,Minutes,Secundes

h = int(input("Введите значение в часах: "))
m = int(input("Введите значение в минутах: "))
s = int(input("Введите значение в секундах: "))
t = int(input("Введите значение в секундах: "))
Hours,Minutes,Secundes = IncTime(h,m,s,t)

print(f'Новое время: {Hours}часов, {Minutes}минут, {Secundes}секунд')