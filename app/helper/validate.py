def validate_entry(data):
  if(data["first_name"].isdigit() or not data["first_name"]):
    print("**first name should not be digit")
    return False

  if(data["last_name"].isdigit() or data["last_name"] == ''):
    print("**last name should not be digit")
    return False

  if(data["hobbies"].isdigit() or not data["hobbies"]):
    print("**hobbies should not be digit")
    return False

  return True

# ----------------------------------------
# -----VEHICLE----------------------------
# ----------------------------------------
def validate_vehicle(data):
  if(data["model"].isdigit() or not data["model"]):
    print("**model should not be digit")
    return False

  if(data["color"].isdigit() or data["color"] == ''):
    print("**color should not be digit")
    return False

  if(not data["year"]):
    print("**year is required")
    return False

  if(not data["mileage"]):
    print("**mileage is required")
    return False

  if(not data["user_id"]):
    print("**mileage is required")
    return False

  return True