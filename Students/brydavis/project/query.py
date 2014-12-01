import json

store_string = ""
store_array = []
model_dict = []



def json_to_sql (data,level=0,key=None):


	def iterate_through(elements,k=key):
		# sql_log.write("CREATE TABLE IF NOT EXISTS %s (%s);\n" % (k,elements))
		next_level = level+1

		for e in elements:
			# global store_string
			# store_string += "%skey: %s, type: %s, level: %s" % ("\t"*level,e,type(data[e]), level)


			global store_array
			if len(store_array) <= level:
				# store_array.append(["%skey: %s, type: %s, level: %s" % ("\t"*level,e,type(data[e]), level)])
				# store_array.append(set("%skey: %s, type: %s, level: %s" % ("\t"*level,e,type(data[e]), level)))
				store_array.append({e:type(data[e])})

			else:
				# store_array[level].append("%skey: %s, type: %s, level: %s" % ("\t"*level,e,type(data[e]), level))
				# store_array[level].add("%skey: %s, type: %s, level: %s" % ("\t"*level,e,type(data[e]), level))
				store_array[level][e] = type(data[e])



			e_string = e
			print "\t"*level,"key: %s, type: %s, level: %s" % (e,type(data[e]), level)
			json_to_sql(data[e],next_level,e_string)

	def create_model_dict(elements,k=key):
		# sql_log.write("CREATE TABLE IF NOT EXISTS %s (%s);\n" % (k,elements))
		next_level = level+1

		for e in elements:
			# global store_string
			# store_string += "%skey: %s, type: %s, level: %s" % ("\t"*level,e,type(data[e]), level)


			global model_dict
			if len(model_dict) <= level:
				# model_dict.append(["%skey: %s, type: %s, level: %s" % ("\t"*level,e,type(data[e]), level)])
				# model_dict.append(set("%skey: %s, type: %s, level: %s" % ("\t"*level,e,type(data[e]), level)))
				model_dict.append({e:type(data[e])})

			else:
				# model_dict[level].append("%skey: %s, type: %s, level: %s" % ("\t"*level,e,type(data[e]), level))
				# model_dict[level].add("%skey: %s, type: %s, level: %s" % ("\t"*level,e,type(data[e]), level))
				model_dict[level][e] = type(data[e])



			e_string = e
			print "\t"*level,"key: %s, type: %s, level: %s" % (e,type(data[e]), level)
			json_to_sql(data[e],next_level,e_string)

	def pass_list(elements,k=key):
		# sql_log.write("CREATE TABLE IF NOT EXISTS %s (%s);\n" % (k,elements))
		next_level = level+1

		for e in elements:
			# global store_string
			# store_string += "%skey: %s, type: %s, level: %s" % ("\t"*level,e,type(data[e]), level)


			global model_dict
			if len(model_dict) <= level:
				# model_dict.append(["%skey: %s, type: %s, level: %s" % ("\t"*level,e,type(data[e]), level)])
				# model_dict.append(set("%skey: %s, type: %s, level: %s" % ("\t"*level,e,type(data[e]), level)))
				model_dict.append({e:type(data[e])})

			else:
				# model_dict[level].append("%skey: %s, type: %s, level: %s" % ("\t"*level,e,type(data[e]), level))
				# model_dict[level].add("%skey: %s, type: %s, level: %s" % ("\t"*level,e,type(data[e]), level))
				model_dict[level][e] = type(data[e])



			e_string = e
			print "\t"*level,"key: %s, type: %s, level: %s" % (e,type(data[e]), level)
			json_to_sql(data[e],next_level,e_string)

	if isinstance(data, dict):
		keys = data.keys()
		# iterate_through(keys,key)
		create_model_dict(keys,key)		


	elif isinstance(data, list):
		indices = [index for index,value in enumerate(data)]
		# iterate_through(indices)
		pass_list(indices)		


	else:
		return type(data)

	return ""


if __name__ == '__main__':
	data = json.loads(open("one.json", "r").read())
	# data = json.loads(open("two.json", "r").read())
	# data = json.loads(open("three.json", "r").read())
	

	sql_log = open("sql.log", "a")
	
	json_to_sql(data)

	sql_log.close()
