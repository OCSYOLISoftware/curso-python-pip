import charts
import read_csv
import utils

def run():
    data = read_csv.read_csv('reporte.csv')

    departamento = input("Elige el departamento que quieras revisar: ").upper()
    data = list(filter(lambda item : item['DEPARTAMENTO'] == departamento, data)) #Filtra el departamento en la grafica de Pie

    users = list(map(lambda x: x['USER'], data)) #consigue informacion de todos los usuarios
    calls = list(map(lambda x: x['CALLS'], data)) #consigue informacion de todas las llamadas
    charts.generate_pie_chart(users, calls)

    departamento = input("Elige un departamento: ").upper()

    result = utils.calls_by_user


    result = utils.calls_by_user(data, departamento)

    if len(result) > 0:
        departamento = result[0]
        labels, values = utils.get_agents(departamento)
        charts.generate_bar_chart(departamento['DEPARTAMENTO'], labels, values)


if __name__ == '__main__':
  run()