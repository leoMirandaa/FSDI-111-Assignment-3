from flask import (
  Flask,
  request
)
from datetime import datetime
from app.database import user #user = module, it has init.py
from app.database import vehicle #user = module, it has init.py

from .helper.validate import validate_entry, validate_vehicle

app = Flask(__name__)

VERSION = "1.0.0"

@app.get('/ping')
def ping():
  out = {
    "status": "ok",
    "message": "ping"
  }
  return out

@app.get("/version")
def version():
  out = {
    "status": "ok",
    "version": VERSION,
    "server_time": datetime.now().strftime("%F %H:%M:%S")
  }
  return out

@app.get("/users")
def get_all_users():
  user_list = user.scan()
  out = {
    "status": "ok",
    "users": user_list
  }
  return out

@app.get("/users/<int:pk>")
def get_user_by_id(pk):
  record = user.select_by_id(pk)
  out = {
    "status": "ok",
  }
  if not record:
    out["status"] = "error"
    out["message"] = "not found"
    return out, 404
  else:
    out["user"] = record
  return out

@app.post("/users") #request context object
def create_user():
  user_data = request.json

  is_valid = validate_entry(user_data)

  if is_valid == True:
    user.insert(user_data)
    return "", 204
  else:
    return "", 404

  # user.insert(user_data)
  # return "", 204

@app.put("/users/<int:pk>")
def update_user(pk):
  user_data = request.json
  user.update(pk, user_data)
  return "", 204

@app.delete("/users/<int:pk>")
def delete_user(pk):
  user.deactivate_user(pk)
  return "", 204

# ----------------------------------------
# -----VEHICLE----------------------------
# ----------------------------------------
@app.get("/vehicles")
def get_all_vehicles():
  vehicle_list = vehicle.scan()
  out = {
    "status": "ok",
    "vehicle": vehicle_list
  }
  return out


@app.get("/vehicles/<int:pk>")
def get_vehicle_by_id(pk):
  record = vehicle.select_by_id(pk)
  out = {
    "status": "ok",
  }
  if not record:
    out["status"] = "error"
    out["message"] = "not found"
    return out, 404
  else:
    out["user"] = record
  return out

@app.post("/vehicles") #request context object
def create_vehicle():
  vehicle_data = request.json
  is_valid = validate_vehicle(vehicle_data)
  if is_valid == True:
    vehicle.insert(vehicle_data)
    return "", 204
  else:
    return "", 404

@app.put("/vehicles/<int:pk>")
def update_vehicle(pk):
  vehicle_data = request.json
  vehicle.update(pk, vehicle_data)
  return "", 204

@app.delete("/vehicles/<int:pk>")
def delete_vehicles(pk):
  vehicle.deactivate_vehicle(pk)
  return "", 204