import requests

URL = "http://127.0.0.1:5000/vehicles"
VEHICLE_TEMPLATE= {
  "model": "Ford",
  "color": "Black",
  "year": 1990,
  "mileage": 50000,
  "user_id": 12
}

def create_vehicle(model, color, year, mileage, user_id):
  vehicle_data= VEHICLE_TEMPLATE
  vehicle_data["model"] = model
  vehicle_data["color"] = color
  vehicle_data["year"] = year
  vehicle_data["mileage"] = mileage
  vehicle_data["user_id"] = user_id
  response = requests.post(URL, json=vehicle_data)
  print("response.status..",response.status_code)
  if response.status_code == 204:
    print("vehicle successfully created")
  else:
    print("Something went wrong while trying to create vehicle")

if __name__ == "__main__":
  print("CREATE A VEHICLE")
  print("---------------")
  model  = input("model: ")
  color = input("color: ")
  year= input("year: ")
  mileage= input("mileage: ")
  user_id= input("user_id: ")
  create_vehicle(model, color, year, mileage, user_id)


