import csv


def get_methods():
    with open('test_data/dogapi_methods.csv') as file:
        reader = csv.reader(file)
        next(reader)

        for method_status in reader:
            yield method_status


methods = get_methods()
