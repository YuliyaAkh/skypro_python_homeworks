#Месяц — сезон

month_to_season = input("Введите номер месяца:")
month = int(month_to_season)
if month in (1, 2, 12): 
 print("Зима")
if month in (3, 4, 5):
 print("Весна")
if month in (6, 7, 8):
 print("Лето")
if month in (9, 10, 11):
 print("Осень")