import requests
from pprint import pprint

URL= "http://127.0.0.1:5000/vehicles"

def get_vehicle(pk):
  url = "%s/%s" % (URL,  pk) # http://127.0.0.1:5000/vehicles/1
  response = requests.get(url)
  if response.status_code == 200:
    pprint(response.json())
  else:
    print("something went wrong retrieving the target vehicle.")


def delete_vehicle(pk):
    url = "%s/%s" % (URL,  pk) # http://127.0.0.1:5000/vehicles/1
    response = requests.delete(url)
    if response.status_code == 204:
      print("Vehicle successfully deleted.")
    else:
      print("Something went wrong while trying to delete the target vehicle.")

if __name__ == "__main__":
  print("DELETE VEHICLE")
  print("-" * 50)
  vehicle_id = input("Type in the target vehicle's ID: ")
  print("Delete the vehicle shown belows?")
  get_vehicle(vehicle_id)
  # print ("result.. ",get_user(user_id))

  option = input("[Y/n]: ")
  if option == "Y" or option == "y":
    delete_vehicle(vehicle_id)
  else:
    print("Vehicle not deleted")