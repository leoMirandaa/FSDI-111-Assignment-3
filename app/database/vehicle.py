#data is returned in tuples in sqlite3
from app.database import get_db

def output_formatter(results):
  out = []
  for result in results:
    result_dict = {
      "id": result[0],
      "model": result[1],
      "color": result[2],
      "year": result[3],
      "mileage": result[4],
      "active": result[5],
      "user_id": result[6],
    }
    out.append(result_dict)
  return out


  # this function creates a user in our user table
def insert(vehicle_dict):
  value_tuple = (
    vehicle_dict.get("model"),
    vehicle_dict.get("color"),
    vehicle_dict.get("year"),
    vehicle_dict.get("mileage"),
    vehicle_dict.get("user_id"),
  )

#""" its to create multiple lines
  statement = """
  INSERT INTO vehicle (
    model,
    color,
    year,
    mileage,
    user_id
  ) VALUES(?,?,?,?,?)
  """

  cursor = get_db()
  # cursor.execute("PRAGMA foreign_keys = ON")
  cursor.execute(statement, value_tuple)
  cursor.commit()
  cursor.close()

def scan():
  cursor = get_db().execute(
    "SELECT * FROM  vehicle WHERE active = 1",
    () #empty tuples, there is nothing to map
  )
  results = cursor.fetchall()
  cursor.close()
  return output_formatter(results)

def select_by_id(pk):
  cursor = get_db().execute("SELECT * FROM vehicle WHERE id=? AND active = 1", (pk, )) #the comma after pk MUST be there!
  results = cursor.fetchall()
  cursor.close()
  return output_formatter(results)

def update(pk, vehicle_data):
  value_tuple = (
    vehicle_data.get("model"),
    vehicle_data.get("color"),
    vehicle_data.get("year"),
    vehicle_data.get("mileage"),
    vehicle_data.get("user_id"),
    pk
  )
  statement = """
    UPDATE vehicle
    SET model=?,
    color=?,
    year=?,
    mileage=?,
    user_id=?
    WHERE id=?
  """

  cursor = get_db()
  cursor.execute(statement, value_tuple)
  cursor.commit()
  cursor.close()

def deactivate_vehicle(pk):
  cursor = get_db()
  cursor.execute("UPDATE vehicle SET active=0 WHERE id=?", (pk, ))
  cursor.commit()
  cursor.close()