import json

def json_to_sql (data,level=0,key=None):

	def iterate_through(elements,k=key):
		sql_log.write("CREATE TABLE IF NOT EXISTS %s (%s);\n" % (k,elements))

		next_level = level+1
		# print "\t"*level,"key: %s, type: %s, len: %s, level: %s" % (key,type(data),len(data), level)

		for e in elements:
			e_string = e


			# print "\t"*level,"key: %s, type: %s, len: %s, level: %s" % (e,type(data[e]),len(data[e]), level)
			print "\t"*level,"key: %s, type: %s, level: %s" % (e,type(data[e]), level)

			json_to_sql(data[e],next_level,e_string)

			# # Use to prevent None
			# kind = json_to_sql(data[e],next_level,e_string)
			# if kind:
			# 	print "\t"*next_level,"key: %s" % e,json_to_sql(data[e],next_level,e_string)
			#	print "\t"*next_level,"key: %s, type: %s, len: %s, level: %s" % (e,type(data),len(data), level)




	if isinstance(data, dict):
		keys = data.keys()
		# print key, keys,
		iterate_through(keys,key)		

	elif isinstance(data, list):
		indices = [index for index,value in enumerate(data)]
		iterate_through(indices)

	else:

		return type(data)

	return ""






if __name__ == '__main__':
	# data = json.loads(open("one.json", "r").read())
	# data = json.loads(open("two.json", "r").read())
	data = json.loads(open("three.json", "r").read())
	
	sql_log = open("sql.log", "a")
	
	json_to_sql(data)

	sql_log.close()
