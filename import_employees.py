import boto3
import csv
import json


csvFilePath = 'C:/Users/bcornwell/Documents/at_chars.csv'
jsonFilePath = 'C:/Users/bcornwell/Documents/jsons/'
client = boto3.client('dynamodb',
    aws_access_key_id="AAAAAAAAAAAAAAAAAAAAA",
    aws_secret_access_key="zzzzzzzzzzzzzzzzzzzz..",
					  )
#data = pd.read_csv(csvFilePath)
#data.columns = ["chars"]
#rawlist = list(data.chars)
print("got to 1")

with open(csvFilePath, newline = '', encoding='utf-8-sig') as csvFile:
	csvReader = csv.reader(csvFile)
	id = 1004
	print("id = " + str(id))
	names = list(csvReader)
	print("names = " + str(names).strip('[]'))

	for name in names:
		print("name =" + str(name).strip('[]'))
		#name = names[name]
		print(name)
		id = id+1
		q = {
			"Employee Name": {
				"S": str(name).strip('[\']')
			}, "EmployeeID": {
				"N": str(id)
			}
		}
		print(json.dumps(q, indent=4))
		with open('char_' + str(id) + '.json', 'w') as outfile:
			json.dump(q, outfile)
		f = open('char_'+str(id)+'.json')
		request_items = json.loads(f.read())
		response = client.put_item(TableName='external-data', Item=request_items)
		print(request_items)





#{
#  "EmployeeID": 01005,
#  "Employee Name": "Flame Princess"
#}
		
