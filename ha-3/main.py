from db import engine, session
from models import Base, Product, Category


def add_example_data():
    electronics = Category(name='Electronics', description='Devices')
    food = Category(name='Food', description='Food')

    session.add_all([electronics, food])
    session.commit()

    smartphone = Product(name='Smartphone', price=600, in_stock=True, category_id=electronics.id)
    laptop = Product(name='Laptop', price=1299.99, in_stock=False, category_id=electronics.id)
    milk = Product(name='Butter', price=3.99, in_stock=True, category_id=food.id)
    bread = Product(name='Bread', price=1.29, in_stock=True, category_id=food.id)
    apples = Product(name='Apricots', price=3.60, in_stock=True, category_id=food.id)

    session.add_all([smartphone, laptop, milk, bread, apples])
    session.commit()


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    add_example_data()
    products = session.query(Product).all()

    for product in products:
        print(f"Product: {product.name}, Price: {product.price}")
