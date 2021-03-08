time_in_sec = int(input("Введите время в секундах: "))
hour = time_in_sec // 3600
minute = (time_in_sec // 60) % 60
sec = time_in_sec % 60

print(" time is %02d:%02d:%02d" % (hour, minute, sec))
