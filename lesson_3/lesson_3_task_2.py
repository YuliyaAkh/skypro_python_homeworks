from smartphone import Smartphone

catalog = []

phone1=Smartphone("Apple", "iPhone15", "+79998889999")
phone2=Smartphone("Sumsung", "Galaxy A10", "+79873332211")
phone3=Smartphone("Nokia", "G21", "+79175553232")
phone4=Smartphone("Xiaomi", "Redmi A3", "+79140005543")
phone5=Smartphone("Huawey", "HUAWEI P60 Pro", "+79654443121")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f'{phone.brand} - {phone.model}. {phone.phone_number}')