# app.py
import streamlit as st
from service.user_service import UserService
from service.task_service import TaskService
from service.assignment_service import AssignmentService

st.title("Task Management Dashboard")

menu = ["Add User", "List Users", "Add Task", "List Tasks", "Assign Task"]
choice = st.sidebar.selectbox("Menu", menu)

# ----------------- Add User -----------------
if choice == "Add User":
    st.subheader("Add a New User")
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Add User"):
        UserService.create_user(username, email, password)
        st.success(f"User '{username}' added successfully!")

# ----------------- List Users -----------------
elif choice == "List Users":
    st.subheader("All Users")
    users = UserService.list_all_users()
    if users:
        for u in users:
            st.write(u)
    else:
        st.info("No users found.")

# ----------------- Add Task -----------------
elif choice == "Add Task":
    st.subheader("Add a Task")
    title = st.text_input("Task Title")
    description = st.text_area("Task Description")
    deadline = st.date_input("Deadline")
    if st.button("Add Task"):
        TaskService.create_task(title, description, deadline=str(deadline))
        st.success(f"Task '{title}' added successfully!")

# ----------------- List Tasks -----------------
elif choice == "List Tasks":
    st.subheader("All Tasks")
    tasks = TaskService.list_tasks()
    if tasks:
        for t in tasks:
            st.write(t)
    else:
        st.info("No tasks found.")

# ----------------- Assign Task -----------------
elif choice == "Assign Task":
    st.subheader("Assign Task to User")
    task_id = st.number_input("Task ID", min_value=1)
    user_id = st.number_input("User ID", min_value=1)
    if st.button("Assign Task"):
        AssignmentService.assign_task(task_id, user_id)
        st.success(f"Task {task_id} assigned to User {user_id}")
