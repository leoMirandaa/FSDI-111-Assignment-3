import requests

URL= "http://127.0.0.1:5000/vehicles"
VEHICLE_TEMPLATE = {
  "model": "Ford",
  "color": "Black",
  "year": 1990,
  "mileage": 50000,
  "user_id": 12
}

def get_vehicle(pk):
  url = "%s/%s" % (URL,  pk) # http://127.0.0.1:5000/vehicles/1
  response = requests.get(url)
  my_response = response.json()
  return my_response


def update_vehicle(pk, model, color, year, mileage, user_id):
  url = "%s/%s" % (URL,  pk) # http://127.0.0.1:5000/users/1
  print("update URL: ",url)
  vehicle_data = VEHICLE_TEMPLATE
  vehicle_data["model"] = model
  vehicle_data["color"] = color
  vehicle_data["year"] = year
  vehicle_data["mileage"] = mileage
  vehicle_data["user_id"] = user_id

  print('data to send: ',vehicle_data)

  response = requests.put(url, json=vehicle_data)# http://127.0.0.1:5000/users/#id
  print("response.status... ", response.status_code)
  if response.status_code == 204:
    print("Vehicle successfully updated")
  else:
    print("Something went wrong while trying to update vehicle")


if __name__ == "__main__":
  target_id = input("Type in the vehicle's ID: ")
  user = get_vehicle(target_id)
  print('user to update:',user["user"])

  print("---------------")
  print("UPDATE VEHICLE")
  print("---------------")
  model  = input("model: ")
  color = input("color: ")
  year= input("year: ")
  mileage= input("mileage: ")
  user_id= input("user_id: ")
  update_vehicle(target_id, model, color, year, mileage, user_id)

