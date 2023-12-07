def get_agents(llamadas_dict):
  population_dict = {
    'Hernandez': llamadas_dict['CALLS'], 
    'MARTINEZ': llamadas_dict['CALLS'], 
    'Mendoza': llamadas_dict['CALLS'], 
    'Garcia': llamadas_dict['CALLS'], 
    'Llanos': llamadas_dict['CALLS'], 
    'Ricardo': llamadas_dict['CALLS'], 
  }
  labels = llamadas_dict.keys()
  values = llamadas_dict.values()
  return labels, values

def calls_by_user(data, user):
  result = list(filter(lambda item: item['DEPARTAMENTO'] == user, data))
  return result
