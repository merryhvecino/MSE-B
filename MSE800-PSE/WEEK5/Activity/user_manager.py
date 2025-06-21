from database import get_connection

def add_user(name, email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    conn.close()

def view_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return users

def search_user(name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE name LIKE ?", ('%' + name + '%',))
    results = cursor.fetchall()
    conn.close()
    return results

def delete_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()

def advanced_search_user(user_id, name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ? AND name LIKE ?", (user_id, '%' + name + '%'))
    results = cursor.fetchall()
    conn.close()
    return results

def insert_course(course_id, name, unit):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO course (id, name, unit) VALUES (?, ?, ?)", (course_id, name, unit))
    conn.commit()
    conn.close()

def assign_course_to_user(user_id, course_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO user_courses (user_id, course_id) VALUES (?, ?)", (user_id, course_id))
    conn.commit()
    conn.close()

def search_course_by_user(course_id, user_name):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        SELECT course.* FROM course
        JOIN user_courses ON course.id = user_courses.course_id
        JOIN users ON users.id = user_courses.user_id
        WHERE course.id = ? AND users.name LIKE ?
    """
    cursor.execute(query, (course_id, '%' + user_name + '%'))
    results = cursor.fetchall()
    conn.close()
    return results
