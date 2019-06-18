import requests

apikey = "aa14885d32f060433dd547a718e132b0"
url = "http://api.openweathermap.org/data/2.5/weather?"

try:
    city = input("Enter City Name : ")
    final_url = f"{url}appid={apikey}&q={city}"
    json_data = requests.get(final_url).json()
    status = requests.get(final_url)
    if status.status_code == 404:
        raise KeyError()
    # print(json_data)
    print("**** Weather Information ****\n")
    print("Name : ", json_data['name'])
    print(f"Co-Ordinate : \tLongitude :{json_data['coord']['lon']}\n\t\tLatitude : {json_data['coord']['lat']}")
    print("Main : ", json_data['weather'][0]['main'])
    print("Description : ", json_data['weather'][0]['description'])
    print("Temperature : ", json_data['main']['temp'])
    print("Pressure : ", json_data['main']['pressure'])
    print("Humidity : ", json_data['main']['humidity'])
    print("Minimum Temperature : ", json_data['main']['temp_min'])
    print("Maximum Temperature : ", json_data['main']['temp_max'],"\n")
except KeyError as e:
    print("City Not Found : ",city)