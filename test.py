# 單位換算程式（無函式、無迴圈）
# 轉換公式：
# 1 km = 0.621371 mi
# F = C * 9/5 + 32
# 1 kg = 2.20462 lb

print("單位換算工具")
print("1) 公里 -> 英里")
print("2) 英里 -> 公里")
print("3) 攝氏 -> 華氏")
print("4) 華氏 -> 攝氏")
print("5) 公斤 -> 磅")
print("6) 磅 -> 公斤")

choice = input("請輸入選項 (1-6): ")

if choice == "1":
    km = float(input("輸入公里數: "))
    miles = km * 0.621371
    print(km, "公里 = ", miles, "英里")

elif choice == "2":
    miles = float(input("輸入英里數: "))
    km = miles * 1.60934
    print(miles, "英里 = ", km, "公里")

elif choice == "3":
    c = float(input("輸入攝氏溫度: "))
    f = c * 9/5 + 32
    print(c, "°C = ", f, "°F")

elif choice == "4":
    f = float(input("輸入華氏溫度: "))
    c = (f - 32) * 5/9
    print(f, "°F = ", c, "°C")

elif choice == "5":
    kg = float(input("輸入公斤數: "))
    lb = kg * 2.20462
    print(kg, "公斤 = ", lb, "磅")

elif choice == "6":
    lb = float(input("輸入磅數: "))
    kg = lb * 0.453592
    print(lb, "磅 = ", kg, "公斤")

else:
    print("輸入錯誤，請輸入 1~6。")
