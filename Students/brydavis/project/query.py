import json

data = json.loads(open("new.json", "r").read())

def json_to_sql (data,level=0,key=None):

	def iterate_through(elements,k=key):
		sql_log = open("sql.log", "a")
		sql_log.write("CREATE TABLE IF NOT EXISTS %s (%s);\n" % (k,elements))
		next_level = level+1
		print "\t"*level,"key: %s, type: %s, len: %s, level: %s" % (key,type(data),len(data), level)

		for e in elements:
			kind = json_to_sql(data[e],next_level)
			if kind:
				print "\t"*next_level,"key: %s" % e,json_to_sql(data[e],next_level,e)


	if isinstance(data, dict):
		keys = data.keys()
		iterate_through(keys,key)		

	elif isinstance(data, list):
		indices = [index for index,value in enumerate(data)]
		iterate_through(indices)

	else:
		return type(data)

	return None





# class Query:
# 	query = ''
# 	# always end with ';' somehow


# 	def create_table(self, name, **columns):
# 		fields = ''
# 		for k in columns.keys():
# 			fields += "%s %s, " % (k,columns[k])

# 		self.query += "CREATE TABLE %s ( %s ) " % (name,fields) 
# 		return self   


# 	def select(self, *columns):
# 		columns = "%s" % (columns,)
# 		columns = columns.strip("()").replace("'","")

# 		self.query += "SELECT %s " % columns 
# 		return self   

# 	def from_table(self, *tables):
# 		tables = "%s" % (tables,)
# 		tables = tables.strip("()").replace("'","")
		
# 		self.query += "FROM %s " % tables 
		
# 		return self


# 	def where(self, conds):
# 		conds = "%s" % (conds,)
# 		conds = conds.strip("()").replace("'","")
		
# 		self.query += "WHERE %s " % conds 
		
# 		return self


# 	def limit(self, num):
# 		self.query += "LIMIT %d" % num

# 		return self



# 	def group_by(self, num):
# 		# self.query += "LIMIT %d" % num

# 		return self

# 	def update(self, num):
# 		# self.query += "LIMIT %d" % num

# 		return self

# 	def insert_into(self, num):
# 		# self.query += "LIMIT %d" % num

# 		return self

# 	def delete_from(self, num):
# 		# self.query += "LIMIT %d" % num

# 		return self




# 	def run(self): pass # requires db connection
# 	def test(self): pass
# 	def clear(self):
# 		self.query = '' 
# 		return self 



# if __name__ == '__main__':
	
# 	q = Query()
# 	under_thirty = q.select("first_name","last_name","age") \
# 					.frm("persons") \
# 					.where("age < 30") \
# 					.limit(10)

# 	print under_thirty.query



# 	example = open('example.sql','w')







# """
# I think I need to build a "blueprint" dictionary for tables and fields,
# then convert to SQL "create table" and "insert into" statements.

# : project scope
# 	input = JSON
# 	output = SQL
# 	platform = sqlite3

# - create "blueprint" dictionary object

# - open and or pass JSON to framework



# - iterate over each line
# 	- identify type and create field
# 	- if list or dict
# 		- create new "logging" table 
# 		- iterate over each field


# """



if __name__ == '__main__':
	json_to_sql(data)
