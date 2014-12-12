import json, re, time, os

# sample_dict = {
# 	'name': 'Bryan',
# 	'age': 32,
# 	'male': True,
# 	'skills': ['abc','def','ghi']
# }




# import __builtin__
# builtin_types= [t for t in __builtin__.__dict__.itervalues() if isinstance(t, type)]

# import pprint
# pprint.pprint(sorted(builtin_types, key=repr))


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
		model_sql_orig = []
		model_sql = []
		table_name = "table_"
		table_exp = 1
		table_num = 64
		
		# patterns = {
		# 	"tags": "(<type \'?\"?)|(\'?\"?>)",
		# 	"lists": ",?[A-z|0-9]+ (list|dict),?[^A-z|0-9|\W]?",
		# 	"strings": ",?[A-z|0-9]+ (string|str|unicode),?[^A-z|0-9|\W]?",
		# 	"integers": ",?[A-z|0-9]+ (int|long),?[^A-z|0-9|\W]?",
		# 	"floats": ",?[A-z|0-9]+ (float|long),?[^A-z|0-9|\W]?",
		# 	"tuples": ",?[A-z|0-9]+ (tuple|set|frozenset),?[^A-z|0-9|\W]?",
		# 	"bools": ",?[A-z|0-9]+ (bool),?[^A-z|0-9|\W]?"
		# }

		patterns = [
			["(<type \'?\"?)|(\'?\"?>)", ""],
			[",?[A-z|0-9]+ (list|dict),?[^A-z|0-9|\W]?", ","], 
			["[\S]?(string|str|unicode)(?![A-z])(?=[,|)|\s])", "TEXT"],
			["[\S]?(int|long)(?![A-z])(?=[,|)|\s])", "INTEGER"],
			["[\S]?(float)(?![A-z])(?=[,|)|\s])", "FLOAT"],
			["[\S]?(tuple|set|frozenset)(?![A-z])(?=[,|)|\s])", "BLOB"],
			["[\S]?(bool)(?![A-z])(?=[,|)|\s])", "BOOLEAN"]
		]

		for table in model_dict:
			table_exp = table_exp + 1 if table_num == 90 else table_exp
			table_num = table_num + 1 if table >= 64 or table < 91 else 65

			columns = []
			# print model_dict[table]
			for k in model_dict[table]:
				# print k, model_dict[table][k] 
				columns.append("%s %s" % (k, model_dict[table][k]))



			table_vars_orig = ",".join(columns)
			table_vars = ",".join(columns)

			for p in patterns:
				table_vars = re.sub(p[0],p[1],table_vars)


			model_sql.append("CREATE TABLE %s%s (%s)" % (table_name,chr(table_num)*table_exp,table_vars)) 
			model_sql_orig.append("CREATE TABLE %s (%s)" % (table_name,table_vars_orig)) 


		return model_sql, model_sql_orig


	if isinstance(obj, dict): 
		process_dict(obj)
	elif isinstance(obj, list): 
		process_list(obj)
	else:
		type(obj)

	return finalize_sql()




if __name__ == '__main__':
	m,n = reduce_dict(sample_dict)
	# print n
	# print ""
	print m

	t = str(int(time.time()))[-4:]
	folder = "./really" 
	
	if not os.path.isdir(folder): os.mkdir(folder)

	with open("%s/test%s.sql"%(folder,t),"a+") as f:
		for i in m:
			f.writelines("%s;\n"%i)









