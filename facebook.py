import requests
import json

# constants, making it easier for you to modify/reuse
TOKEN = "EAAhCG2XgvzMBACbYLRb3N9yBxj89ZB1xwVPkcyp5vQnsPB6JBmXVoWby3QlN2WlwhEZCdZCZCefzwrVH2zhtMSh1pZBZBSYo0ZBn28DKRgQDtfq4zpZCY8OhkZA1clBjc90G05bXoEYurwyUnLWSdOdj9JdVWGkc4xXEulzmWdJKBJJpa6db73NODXrquOY7hQFpx5fZCSRTArHQZDZD"
FIELDS = "id,name,events" #if you need additional fields, add a comma(,) followed by the name; NO SPACE IN BETWEEN!!

# if you need additional parameters, add an and sign(&) to the end of the string,
# followed by the key, and then the equal sign(=), and finally the value
URL = "https://graph.facebook.com/1789798511275151?debug=all&fields="+FIELDS+"&access_token=" + TOKEN

response = requests.get(URL)
data_string = response.text # response from the API call, in string
data_json = json.loads(data_string) # converts to JSON
events_Array = data_json["events"]["data"] # an array/list of JSON/dictionary objects

#print(events_Array[0].keys())

#index = 0
#for index in range(len(events_Array)):
	#print("Event Name:", end =" ")
	#print(events_Array[index]['name'])
	#print("Place:", end =" ")
	#print(events_Array[index]['place']['name'])
	#print("Start Time:", end =" ")
	#print(events_Array[index]['start_time'])
	#print("End Name:", end =" ")
	#print(events_Array[index]['end_time'])
	#print("Description:", end =" ")
	#print(events_Array[index]['description'])
	#print("")
