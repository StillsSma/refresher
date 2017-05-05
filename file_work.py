import csv


with open('authors.csv') as csvfile:
    books = csv.reader(csvfile, delimiter=',', quotechar= '|')
    for book in books:
        print(book[2])
