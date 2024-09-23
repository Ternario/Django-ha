from sqlalchemy import func
from models import Category, Product
from db import get_session


def populate_data():
    session = get_session()

    categories = [
        Category(name="Electronics", description="Gadgets and devices."),
        Category(name="Books", description="Printed books and e-books."),
        Category(name="Cloth", description="Clothes for men and women.")
    ]
    session.add_all(categories)
    session.commit()

    electronics = session.query(Category).filter_by(name="Electronics").first()
    books = session.query(Category).filter_by(name="Books").first()
    clothing = session.query(Category).filter_by(name="Cloth").first()

    products = [
        Product(name="Smartphone", price=299.99, in_stock=True, category=electronics),
        Product(name="Laptop", price=499.99, in_stock=True, category=electronics),
        Product(name="Science fiction novel", price=15.99, in_stock=True, category=books),
        Product(name="Jeans", price=40.50, in_stock=True, category=clothing),
        Product(name="T-shirt", price=20.00, in_stock=True, category=clothing)
    ]
    session.add_all(products)
    session.commit()


def read_data():
    session = get_session()
    categories = session.query(Category).all()
    for category in categories:
        print(f"Category: {category.name}, Description: {category.description}")
        for product in category.products:
            print(f"Product: {product.name}, Price: {product.price}")


def update_data():
    session = get_session()
    product = session.query(Product).filter_by(name="Smartphone").first()
    if product:
        product.price = 349.99
        session.commit()


def aggregate_data():
    session = get_session()
    results = session.query(Category.name, func.count(Product.id)).join(Product).group_by(Category.id).all()
    for category_name, product_count in results:
        print(f"Category: {category_name}, Products count: {product_count}")


def filter_categories():
    session = get_session()
    results = session.query(Category).join(Product).group_by(Category.id).having(func.count(Product.id) > 1).all()
    for category in results:
        print(f"Category: {category.name}, Description: {category.description}")