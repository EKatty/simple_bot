
catalog_item = {"type": "phone",
                "vendor": "Apple",
                "model": "Iphone 12",
                'price': 30
}

catalog_item['price'] = 70  #заменили прайс в каталоге
catalog_item['audio_jack'] = False #добавили в каталог
print(catalog_item)

item_name = 'Var1: ' + catalog_item['vendor'] + ' ' + catalog_item['model']     #складывание + пробел ' '
print(item_name)


# МЕТОД .Get()

item_name = 'Var2: ' + catalog_item.get('vendor') + " " + catalog_item.get('model')     #складывание + пробел ' ' c .get()
print(item_name)

print(catalog_item.get('discount', 'Скидок нет!'))

print('model' in catalog_item) #показывает есть ли ключ в словаре
print('discount' in catalog_item)
print('discount' not in catalog_item)

# del удаляет из каталога

del catalog_item['price']
print(catalog_item)
