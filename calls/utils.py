def get_agents(llamadas_dict): #get_population
  population_dict = {           #population_dict
    'Adrian Hernandez': int(llamadas_dict['CALLS']), 
    'Erika Martinez': int(llamadas_dict['CALLS']), 
    'Erika Mendoza': int(llamadas_dict['CALLS']), 
    'Grecia Garcia': int(llamadas_dict['CALLS']), 
    'Llanos': int(llamadas_dict['CALLS']), 
    'Ricardo Mejia': int(llamadas_dict['CALLS']), 
  }
  labels = population_dict.keys()
  values = population_dict.values()
  return labels, values

def calls_by_user(data, user): #population_by_country
  result = list(filter(lambda item: item['DEPARTAMENTO'] == user, data))
  return result
