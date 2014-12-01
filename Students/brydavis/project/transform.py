import json

# sample_dict = {
# 	'name': 'Bryan',
# 	'age': 32,
# 	'male': True,
# 	'skills': ['abc','def','ghi']
# }
sample_dict = json.loads(open("one.json", "r").read())

model_dict = {}


def reduce_dict(obj,lev=0):
	
	def process_dict(obj,lev=lev):
		global model_dict	
		keys = obj.keys() 

		for k in keys:

			if lev in model_dict:
				if k not in model_dict:
					model_dict[lev][k] = type(obj[k])
			else:
				model_dict[lev] = {k:type(obj[k])}

			if isinstance(obj[k], list): process_list(obj[k],lev)

	def process_list(obj,lev=lev):
		global model_dict	
		keys = len(obj) 

		for k in range(keys):
			# model_dict.append(type(obj[k]))
			if isinstance(obj[k], dict): process_dict(obj[k],lev+1)		

	def finalize_sql():
		global model_dict
		model_sql = []
		table_name = "table_one"
		


		for table in model_dict:
			columns = []
			# print model_dict[table]
			for k in model_dict[table]:
				# print k, model_dict[table][k] 
				columns.append("%s %s" % (k, model_dict[table][k]))
			model_sql.append("CREATE TABLE %s (%s)" % (table_name,",".join(columns))) 

		return model_sql


	if isinstance(obj, dict): 
		process_dict(obj)
	elif isinstance(obj, list): 
		process_list(obj)
	else:
		type(obj)

	return finalize_sql()




if __name__ == '__main__':
	m = reduce_dict(sample_dict)

	# print model_dict