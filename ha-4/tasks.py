from sqlalchemy import func
from models import Category, Product
from db import session

SESSION = session


def populate_data():
    categories = [
        Category(name="Electronics", description="Gadgets and devices."),
        Category(name="Books", description="Printed books and e-books."),
        Category(name="Cloth", description="Clothes for men and women.")
    ]
    SESSION.add_all(categories)
    SESSION.commit()

    electronics = SESSION.query(Category).filter_by(name="Electronics").first()
    books = SESSION.query(Category).filter_by(name="Books").first()
    clothing = SESSION.query(Category).filter_by(name="Cloth").first()

    products = [
        Product(name="Smartphone", price=299.99, in_stock=True, category=electronics),
        Product(name="Laptop", price=499.99, in_stock=True, category=electronics),
        Product(name="Science fiction novel", price=15.99, in_stock=True, category=books),
        Product(name="Jeans", price=40.50, in_stock=True, category=clothing),
        Product(name="T-shirt", price=20.00, in_stock=True, category=clothing)
    ]
    SESSION.add_all(products)
    SESSION.commit()


def read_data():
    categories = SESSION.query(Category).all()
    for category in categories:
        print(f"Category: {category.name}, Description: {category.description}")
        for product in category.products:
            print(f"Product: {product.name}, Price: {product.price}")


def update_data():
    product = SESSION.query(Product).filter_by(name="Smartphone").first()
    if product:
        product.price = 349.99
        SESSION.commit()


def aggregate_data():
    results = SESSION.query(Category.name, func.count(Product.id)).join(Product).group_by(Category.id).all()
    for category_name, product_count in results:
        print(f"Category: {category_name}, Products count: {product_count}")


def filter_categories():
    results = SESSION.query(Category).join(Product).group_by(Category.id).having(func.count(Product.id) > 1).all()
    for category in results:
        print(f"Category: {category.name}, Description: {category.description}")
