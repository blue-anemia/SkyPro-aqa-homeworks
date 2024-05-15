from Smartphone import Smartphone

catalog = []

catalog.append(Smartphone('Apple', 'iPhone 13', '+79111234567'))
catalog.append(Smartphone('Samsung', 'Galaxy S21', '+79111234568'))
catalog.append(Smartphone('Google', 'Pixel 6', '+79111234569'))
catalog.append(Smartphone('OnePlus', '9 Pro', '+79111234570'))
catalog.append(Smartphone('Sony', 'Xperia 1 III', '+79111234571'))

for phone in catalog:
    print(f"{phone.phone_brand} - {phone.phone_model}. {phone.phone_number}")