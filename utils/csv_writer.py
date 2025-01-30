import csv
import config

def write_products_to_csv(products):
    """Writes a list of product dictionaries to a CSV file."""
    field_names = ['name', 'price', 'rating', 'url']
    with open(config.CSV_FILE_PATH, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=field_names)
        writer.writeheader()
        for product in products:
            writer.writerow(product)
