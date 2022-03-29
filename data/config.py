import json


token = ""
url = ""
FileNameDataBase = "db.db3"
admins_id = [
    XXXXXXXXX
]
headers = {'authtoken':''}
dateformater = "%b %d, %Y %H:%M %p"

json_params = json.dumps({"list_info": {"start_index": 1, "row_count": 1000, "get_total_count": "true"}}) 
json_data = {"input_data": json_params}