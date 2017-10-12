import os
import json


hab_db_path = "device.db"
hob_db_path = os.path.expanduser("~/.homebridge/config.json")
state_prefix = os.path.expanduser("~/.homebridge/")

with open(hab_db_path) as jsonfile:
	hab_db = json.load(jsonfile)

with open(hob_db_path) as jsonfile:
	hob_db = json.load(jsonfile)

accessories = hob_db['accessories']
for device in hab_db:
	if device['deviceType'] == "exec":
		print ("Convert " + device['name'] + "...")
		entry = {}
		entry['accessory'] = 'Script'
		entry['name'] = device['name']
		entry['on'] = device['onUrl']
		entry['off'] = device['offUrl']
		entry['state'] = state_prefix + "state_" + device['name'].replace(' ', '_') + ".flag"
		entry['fileState'] = state_prefix + device['name'].replace(' ', '_') + ".flag"
		entry['on_value'] = 'true'
		entry['exact_match'] = 'true'
		accessories.append(entry)


with open(hob_db_path, 'wt') as out:
	res = json.dump(hob_db, out, indent=4, separators=(',',': '))



