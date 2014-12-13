"""
Final project for UW's Intro to Python, Autumn 2014.  
The project's name is "json2sql", because this script 
will take a json object and create an sqlite3 database 
and matching schemas.  
"""

import json, re, time, os, sqlite3

sample_dict = json.loads(open("test.json", "r").read())

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
		table_name = "table_"
		table_exp = 1
		table_num = 64
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
			for k in model_dict[table]:
				columns.append("%s %s" % (k, model_dict[table][k]))

			table_vars = ",".join(columns)
			for p in patterns:
				table_vars = re.sub(p[0],p[1],table_vars)

			model_sql.append("CREATE TABLE %s%s (%s)" % (table_name,chr(table_num)*table_exp,table_vars)) 

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
	print m

	t = str(int(time.time()))[-4:]
	folder = "./output"
	sql_file = "%s/test%s.sql"%(folder,t) 
	
	if not os.path.isdir(folder): os.mkdir(folder)

	with open(sql_file,"a+") as f:
		for i in m:
			f.writelines("%s;\n"%i)


	db_file = './output/main.db'

	db_is_new = not os.path.exists(db_file)

	if db_is_new:
	    print 'Creating database...'
	else:
	    print 'Database exists...'

	with sqlite3.connect(db_file) as conn:
		
		with open(sql_file, 'rt') as f:
			schema = f.read()
		
		conn.executescript(schema)


	# Project TODO
	# =======================================
	# Once database / schemas are created,
	# insert sample data from original json
	# into the new database (12/11)







