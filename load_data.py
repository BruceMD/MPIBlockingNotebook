import csv


def full(file_directory):

    names_list = []

    with open(file_directory) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            names_list.append(row)

    return names_list
