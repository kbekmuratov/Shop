
product = input("Введите название продукта: ")
quantity = int(input("Введите количество: "))
price = float(input("Введите стоимость: "))

total_price = quantity * price

print(f"{product} | {quantity} = {total_price:.0f} тенге")