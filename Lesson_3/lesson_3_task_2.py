from smartphone import Smartphone

catalog = []
phone1 = Smartphone("Samsung", "Galaxy S23", "+79127655937")
phone2 = Smartphone("Google", "Pixel 7 pro", "+79128791803")
phone3 = Smartphone("Xiaomi", "Mi 10T Pro", "+79128777487")
phone4 = Smartphone("Apple", "IPhone 10", "+79276339397")
phone5 = Smartphone("OnePlus", "9 Pro", "+79127655936")
catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"{phone.brand} {phone.model}, {phone.phone_number}")
