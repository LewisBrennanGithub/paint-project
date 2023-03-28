from db.run_sql import run_sql
from helpers.invert import *
from models.paint import Paint
import pdb

def save(paint):
    sql = "INSERT INTO paint (name, description, value, offset_value, popularity) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [paint.name, paint.description, paint.value, paint.offset_value, paint.popularity]
    results = run_sql(sql, values)
    id = results[0]['id']
    paint.id = id
    return paint

def select_all():
    paints = []
    sql = "SELECT * FROM paints"
    results = run_sql(sql)
    for row in results:
        paint = Paint(row['name'], row['description'], row['value'], row['popularity'], row['id'])
        paints.append(paint)
    return paints

def select(id):
    paint = None
    sql = "SELECT * FROM paints WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        paint = Paint(result['name'], result['description'], result['value'], result['offset_value'], result['popularity'], result['id'])
    return paint

def delete_all():
    sql = "DELETE FROM paints"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM paints WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(paint):
    sql = "UPDATE paints SET (name, description, value, offset_value, popularity) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [paint.name, paint.description, paint.value, paint.offset_value, paint.popularity, paint.id]
    run_sql(sql, values)

def list_paints_limited():
    paints = []
    sql = "SELECT * FROM paints ORDER BY popularity DESC"
    results = run_sql(sql)
    for row in results:
        paint = Paint(row['name'], row['description'], row['value'], row['offset_value'], row['popularity'], row['id'])
        paints.append(paint)
    return paints

def save_new_paint(paint):
    offset_value = invert_colour(paint.value)
    sql = "INSERT INTO paints (name, description, value, offset_value, popularity) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [paint.name, paint.description, paint.value, offset_value, paint.popularity]
    results = run_sql(sql, values)
    id = results[0]['id']
    paint.id = id
    return paint

def update_existing_paint(paint):
    sql = "UPDATE paints SET (name, description, value, offset_value) = (%s, %s, %s, %s) WHERE id = %s"
    values = [paint.name, paint.description, paint.value, paint.offset_value, paint.id]
    pdb.set_trace()
    run_sql(sql, values)

# def update_existing_paint(paint):
#     sql = "UPDATE paints SET (name, description, value, offset_value) = (%s, %s, %s, %s) WHERE id = %s"
#     values = [paint.name, paint.description, paint.value, paint.offset_value, paint.id]
#     results = run_sql(sql, values)
#     id = results[0]['id']
#     paint.id = id
#     return paint

def decrement_paint_popularity(id):
    paint = select(id)
    paint.decrease_popularity()
    sql = "UPDATE paints SET popularity = %s WHERE id = %s"
    values = [paint.popularity, paint.id]
    run_sql(sql, values)

def increment_paint_popularity(id):
    paint = select(id)
    paint.increase_popularity()
    sql = "UPDATE paints SET popularity = %s WHERE id = %s"
    values = [paint.popularity, paint.id]
    run_sql(sql, values)

# def decrement_paint_popularity(id):
#     paint = select(id)
#     paint.decrease_popularity()
#     sql = "UPDATE paints SET popularity = %s WHERE id = %s"
#     values = [paint.popularity, paint.id]
#     run_sql(sql, values)

# def increment_paint_popularity(id):
#     paint = select(id)
#     if paint:
#         paint.increase_popularity()
#         sql = "UPDATE paints SET popularity = %s WHERE id = %s"
#         values = [paint.popularity, paint.id]
#         run_sql(sql, values)

# def decrement_paint_popularity(paint_id):
#     sql = "UPDATE paints SET popularity = (%s) WHERE id = %s"
#     values = [paint_id]
#     run_sql(sql, values)


# def increment_paint_popularity(paint_id):
#     sql = "UPDATE paints SET popularity = (%s)  WHERE id = %s"
#     values = [paint_id]
#     run_sql(sql, values)

# def decrement_paint_popularity(paint_id):
#     sql = "UPDATE paints SET popularity = popularity - 1 WHERE id = %s"
#     values = [paint_id]
#     run_sql(sql, values)

# def increment_paint_popularity(paint_id):
#     sql = "UPDATE paints SET popularity = popularity + 1 WHERE id = %s"
#     values = [paint_id]
#     run_sql(sql, values)