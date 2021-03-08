user_str = ["Один", "Два", "Три", "Четыре"]
temp_str = ""
index = 0
f_write = open("les_4_output.txt", "a")
with open("les_4_input.txt", "r", encoding="utf-8") as f_obj:
    for line in f_obj:
        _, str2, str3 = line.split()
        temp_str = user_str[index] + " " + str2 + " " + str3 + "\n"
        index += 1
        f_write.write(temp_str)
        print(f'str1 {temp_str}')
f_write.close()

