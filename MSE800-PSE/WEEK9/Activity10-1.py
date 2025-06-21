import datetime

def get_timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def create_log(event_type, user_id, message):
    return f"[{get_timestamp()}] [{event_type}] User: {user_id} - {message}\n"

def log_event(event_type, user_id, message):
    log = create_log(event_type, user_id, message)
    with open("rental_log.txt", "a") as file:
        file.write(log)
