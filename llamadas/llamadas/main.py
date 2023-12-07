import charts
import read_csv
import utils

def run():
    data = read_csv.read_csv('reporte.csv')
    data = list(filter(lambda item : item['OPERACION'] == 'RIOS', data))

    users = list(map(lambda x: x['USER'], data))
    calls = list(map(lambda x: x['CALLS'], data))
    charts.generate_pie_chart(users, calls)

    departamento = input("Elige un departamento: ").upper()

    result = utils.calls_by_user


    result = utils.calls_by_user(data, departamento)

    if len(result) > 0:
        departamento = result[0]
        labels, values = utils.get_agents(departamento)
        charts.generate_bar_chart(departamento['USER'], values)


if __name__ == '__main__':
  run()