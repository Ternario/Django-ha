from db import create_tables
from tasks import populate_data, read_data, update_data, aggregate_data, filter_categories


def main():
    create_tables()
    populate_data()
    read_data()
    update_data()
    aggregate_data()
    filter_categories()


if __name__ == "__main__":
    main()
