import datetime 
from decimal import Decimal

DATE_FORMAT = '%Y-%m-%d'
goods = {'Яйца Фабрики №1': [{'amount': Decimal('1'),
                      'expiration_date': datetime.date(2025, 3, 5)}],
 'Фабрика №2: яйца': [{'amount': Decimal('2'),
                       'expiration_date': datetime.date(2025, 3, 1)},
                      {'amount': Decimal('3'),
                       'expiration_date': datetime.date(2025, 3, 3)}],
 'макароны': [{'amount': Decimal('100'), 'expiration_date': None}]}

def add(items, title, amount, expiration_date=None):
    if title not in items:
        items[title] = []
    expiration_date = datetime.datetime.strptime(
    expiration_date, DATE_FORMAT
    ).date() if expiration_date else expiration_date
    list.append(
    items[title],
        {'amount': amount, 'expiration_date': expiration_date}
        )
    
def add_by_note(items, note):
    elements = str.split(note, ' ')
    if len(str.split(elements[-1], '-')) == 3:
        expiration_date = elements[-1]
        amount = Decimal(elements[-2])
        title = str.join(' ', elements[0:-2])
        add(items, title, amount, expiration_date)
    else:
        amount = Decimal(elements[-1])
        title = str.join(' ', elements[0:-1])
        expiration_date = None
        add(items, title, amount, expiration_date) 


def find(items, needle):
    list_of_needle = []
    for key in items:
        if needle.lower() in key.lower():
            list_of_needle.append(key)
    return list_of_needle
          


def get_amount(items, needle):
    needs_goods = find(items, needle)
    sum_of_amount = 0
    for point in needs_goods: 
        value = items[point]
        for position in value:
            sum_of_amount += position['amount']
    return Decimal(sum_of_amount)
    
              
        


def get_expired(items, in_advance_days=None):
    product_for_recycling = []  # Список просроченныз продуктов  состоящий из катеджей
    is_today = datetime.date.today() #значение сегодня
    if in_advance_days is None:
        in_advance_days=1
    time_delta = datetime.timedelta(days = in_advance_days+1) #Дельта
    date_of_get_expired = is_today + time_delta  #дата истечения срока годности
    list_of_goods = list(items.keys())  #Список продуктов в массиве ['Яйца Фабрики №1', 'Фабрика №2: яйца', 'макароны']
    list_of_overdue_double = []  # Простроченные товары ['Яйца Фабрики №1', 'Фабрика №2: яйца', 'Фабрика №2: яйца']
    list_of_sum_dup = []  # в этом списке дупликаты собираем в один
    for good in list_of_goods:
        # Яйца Фабрики №1
        # Фабрика №2: яйца
        # макароны
        parties_of_goods = items[good]  #Партии для каждого отдельного продукта 
        # [{'amount': Decimal('1'), 'expiration_date': datetime.date(2025, 2, 25)}]
        # [{'amount': Decimal('2'), 'expiration_date': datetime.date(2025, 2, 21)}, {'amount': Decimal('3'), 'expiration_date': datetime.date(2025, 2, 20)}]
        # [{'amount': Decimal('100'), 'expiration_date': None}]
        
        for party in parties_of_goods:  #Разбираем каждую отдельную партию
            # {'amount': Decimal('1'), 'expiration_date': datetime.date(2025, 2, 25)}
            # {'amount': Decimal('2'), 'expiration_date': datetime.date(2025, 2, 21)}
            # {'amount': Decimal('3'), 'expiration_date': datetime.date(2025, 2, 20)}
            # {'amount': Decimal('100'), 'expiration_date': None}
            if party['expiration_date'] == None:
                
                continue
            elif party['expiration_date'] < date_of_get_expired:
                first_tuple_with_bad_goods = (good, party['amount'])
                product_for_recycling.append(first_tuple_with_bad_goods)

    for product in product_for_recycling:
        list_of_overdue_double.append(product[0])

    duplicates = list(set([item for item in list_of_overdue_double if list_of_overdue_double.count(item) > 1]))
    print(duplicates)

    for duplicate in duplicates:
        counter = Decimal('0')
        for product in product_for_recycling:
            if duplicate in product:
                counter += product[1]
            
            
        list_of_sum_dup.append((duplicate,counter))  

    for duplicate in duplicates:

        for product in product_for_recycling:
            if duplicate not in product:
                list_of_sum_dup.append(product)
    
        
    print(product_for_recycling)
    print(list_of_sum_dup)
    return list_of_sum_dup
