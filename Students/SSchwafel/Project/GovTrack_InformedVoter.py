
#List Current Members of Congress with GovTrack
#congresspeople_url = 'https://www.govtrack.us/api/v2/role?current=true&limit=600'

#One Particular Congressman
#url = 'https://www.govtrack.us/api/v2/person/400054'
# this takes a python object and dumps it to a string which is a JSON
# representation of that object
data = json.load(urllib2.urlopen(congresspeople_url))

objects = data['objects']
#for representative in objects:
#    print representative['person']['name'].encode('utf-8')
#pprint(objects[0][person]['sortname'])

representatives = []

for i in objects:
    representatives.append(i['person']['sortname'].encode('utf-8'))

#representatives = sorted(representatives)
#pprint(representatives)

