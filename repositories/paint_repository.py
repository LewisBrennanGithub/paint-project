from db.run_sql import run_sql

from models.paint import Paint

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
        paint = Paint(row['name'], row['description'], row['value'], row['offset_value'], row['popularity'], row['id'])
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
    run_sql

def delete(id):
    sql = "DELETE FROM paints WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(paint):
    sql = "UPDATE paints SET (name, description, value, offset_value, popularity) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [paint.name, paint.description, paint.value, paint.offset_value, paint.popularity, paint.id]
    run_sql(sql, values)