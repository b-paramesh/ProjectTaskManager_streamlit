def validate_email(email):
    import re
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def format_task(task):
    return f"ID: {task['task_id']}, Title: {task['title']}, Status: {task['status']}, Deadline: {task['deadline']}"
