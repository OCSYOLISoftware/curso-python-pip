import csv

#Lee CSV y transforma en diccionario

def read_csv(path): #
    with open(path,'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader) #Llama el header del documento
        data = []
        for row in reader:
            iterable = zip(header, row) #une el header y row en tuplas
            llamadas_dict = {key: value for key, value in iterable}
            data.append(llamadas_dict)
        return data

if __name__ == '__main__':
  data = read_csv('reporte.csv')
  print(data[0])