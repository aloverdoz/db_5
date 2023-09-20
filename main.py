import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import create_tables, Publisher, Book, Shop, Sale, Stock

DSN = "postgresql://postgres:postgres@localhost:5432/test"
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

def insert_publisher(name):
    publisher = Publisher(name=name)
    session.add(publisher)
    session.commit()
    print(publisher)

def insert_book(title, id_publisher):
    book = Book(title=title, id_publisher=id_publisher)
    session.add(book)
    session.commit()
    print(book)

def insert_shop(name):
    shop = Shop(name=name)
    session.add(shop)
    session.commit()
    print(shop)

def insert_stok(id_book, id_shop, count):
    stok = Stock(id_book=id_book, id_shop=id_shop, count=count)
    session.add(stok)
    session.commit()
    print(stok)

def insert_sale(prise, date_sale, id_stock, count):
    sale = Sale(prise=prise, date_sale=date_sale, id_stock=id_stock, count=count)
    session.add(sale)
    session.commit()
    print(sale)





name_publisher = ('Вальтер Скотт', 'Стюард Чейз', "Дж. К. Роулинг", "Дж. Р. Р. Толкин")
for i in name_publisher:
    insert_publisher(i)

name_book = (('Айвенго', 1), ('Гарри Поттер и тайная комната', 3), ('Тирания слов', 2), ('Хоббит', 4), ('Гарри Поттер и филосовский камень', 3))
for i in name_book:
    insert_book(i[0], i[1])

name_shop = ('Книжный мир', 'Буквоед', "Азбука букв", "Теремок")
for i in name_shop:
    insert_shop(i)

name_stok = ((1, 1, 10), (2, 2, 10), (3, 3, 200), (4, 4, 10), (5, 4, 11))
for i in name_stok:
    insert_stok(i[0], i[1], i[2])

name_sale = ((750, '2023-09-05', 1, 1), (1250, '2023-09-05', 2, 1),
             (1000, '2023-09-05', 3, 1),   (1500, '2023-09-05', 4, 1),   (1250, '2023-09-05', 5, 1))
for i in name_sale:
    insert_sale(i[0], i[1], i[2], i[3])

print()
print('Авторы: Вальтер Скотт,     Стюард Чейз,     Дж. К. Роулинг,     Дж. Р. Р. Толкин')
name_autor = input('Введите имя автора: ')

for pub, bo, sh, st, sa in session.query(Publisher, Book, Shop, Stock, Sale)\
        .filter(Book.id_publisher == Publisher.id)\
        .filter(Stock.id_shop == Shop.id)\
        .filter(Stock.id_book == Book.id)\
        .filter(Sale.id_stock == Stock.id)\
        .all():
    try:
        if pub.name.upper() == name_autor.upper():
            print(f'{bo.title} | {sh.name} | {sa.prise} | {sa.date_sale}')
        if pub.id == int(name_autor):
            print(f'{bo.title} | {sh.name} | {sa.prise} | {sa.date_sale}')
    except:
        pass

session.close()
