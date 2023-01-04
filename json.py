import json
 
data = '{"firstName":"serkan","lastName":"gntn"}'

y=json.loads(data)
type(y)

print(y["firstName"])
print(y["lastName"])

customer={
    "firstName":"serkan",
    "lastName":"gntn",
    "email":"srkangntn@xgmail.com"
      }
customerJson=json.dumps(customer)
print(customer)
