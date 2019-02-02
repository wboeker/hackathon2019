import requests
import json

# constants, making it easier for you to modify/reuse
TOKEN = "EAAhCG2XgvzMBAPMDKIiMvhAn6e7TpRtMYSVZCsGPrl5jsHfrLBRlBtWWKhNgBDfKTAZB8QsbPxf0RGoVc4yFBHqoLElNZCZBZA86OZBYZC2gO9AnZAe4upgkcRZBSclOgykDNzhSvWqSgdTs0FrbSYHE4RnOGL8EVAly41ZBbxfZCiQnvbTtmCQOyoqlVGeM3iXxI3qGtmi60Ch8AZDZD"
FIELDS = "id,name,events" #if you need additional fields, add a comma(,) followed by the name; NO SPACE IN BETWEEN!!

# if you need additional parameters, add an and sign(&) to the end of the string,
# followed by the key, and then the equal sign(=), and finally the value
URL = "https://graph.facebook.com/1789798511275151?debug=all&fields="+FIELDS+"&access_token=" + TOKEN

response = requests.get(URL)
data_string = response.text # response from the API call, in string
data_json = json.loads(data_string) # converts to JSON
events_Array = data_json["events"]["data"] # an array/list of JSON/dictionary objects

print(events_Array[0])


