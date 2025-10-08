
import streamlit as st
from service.user_service import UserService
from service.task_service import TaskService
from service.assignment_service import AssignmentService

# Page config
st.set_page_config(page_title="Task Manager", page_icon="✅", layout="wide")

# Title
st.markdown("<h1 style='text-align:center; color:#4CAF50;'>📋 Task Management System</h1>", unsafe_allow_html=True)

# Sidebar navigation
menu = st.sidebar.radio(
    "📌 Navigate",
    ["Home", "Users", "Tasks", "Assignments"]
)

# ------------------ HOME ------------------
if menu == "Home":
    st.success("Welcome to your Task Management System 🚀")
    st.info("Use the sidebar to navigate between **Users**, **Tasks**, and **Assignments**.")

# ------------------ USERS ------------------
elif menu == "Users":
    st.subheader("👤 Manage Users")
    tab1, tab2, tab3 = st.tabs(["➕ Add User", "✏️ Edit User", "🗑️ Delete User"])

    with tab1:
        st.markdown("### Add New User")
        username = st.text_input("Username")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        if st.button("Add User", type="primary"):
            UserService.create_user(username, email, password)
            st.success(f"✅ User '{username}' added successfully!")

    with tab2:
        st.markdown("### Edit User")
        user_id = st.number_input("User ID", min_value=1, step=1)
        field = st.selectbox("Field to edit", ["username", "email", "password_hash"])
        value = st.text_input("New value")
        if st.button("Update User"):
            UserService.update_user(user_id, **{field: value})
            st.success("✏️ User updated successfully!")

    with tab3:
        st.markdown("### Delete User")
        user_id = st.number_input("Enter User ID to delete", min_value=1, step=1, key="del_user")
        if st.button("Delete User", type="secondary"):
            UserService.remove_user(user_id)
            st.error(f"🗑️ User {user_id} deleted successfully!")

# ------------------ TASKS ------------------
elif menu == "Tasks":
    st.subheader("📝 Manage Tasks")
    tab1, tab2, tab3, tab4 = st.tabs(["➕ Add Task", "✏️ Edit Task", "🗑️ Delete Task", "📋 List Tasks"])

    with tab1:
        st.markdown("### Add New Task")
        title = st.text_input("Task Title")
        description = st.text_area("Task Description")
        deadline = st.date_input("Deadline (optional)")
        if st.button("Add Task", type="primary"):
            TaskService.create_task(title, description, deadline=str(deadline))
            st.success("✅ Task added successfully!")

    with tab2:
        st.markdown("### Edit Task")
        task_id = st.number_input("Task ID", min_value=1, step=1)
        field = st.selectbox("Field to edit", ["title", "description", "status", "deadline"])
        value = st.text_input("New value")
        if st.button("Update Task"):
            TaskService.update_task(task_id, **{field: value})
            st.success("✏️ Task updated successfully!")

    with tab3:
        st.markdown("### Delete Task")
        task_id = st.number_input("Enter Task ID to delete", min_value=1, step=1, key="del_task")
        if st.button("Delete Task", type="secondary"):
            TaskService.delete_task(task_id)
            st.error(f"🗑️ Task {task_id} deleted successfully!")

    with tab4:
        st.markdown("### All Tasks")
        filter_by = st.selectbox("Filter by", ["None", "user_id", "status", "deadline"])
        value = st.text_input("Filter value (optional)")
        tasks = TaskService.list_tasks(filter_by if filter_by != "None" else None, value if value else None)

        if tasks:
            st.table(tasks)
        else:
            st.warning("No tasks found.")

# ------------------ ASSIGNMENTS ------------------
elif menu == "Assignments":
    st.subheader("📌 Assign Tasks")
    task_id = st.number_input("Task ID", min_value=1, step=1)
    user_id = st.number_input("User ID", min_value=1, step=1)
    if st.button("Assign Task", type="primary"):
        AssignmentService.assign_task(task_id, user_id)
        st.success(f"📌 Task {task_id} assigned to User {user_id} successfully!")

    st.markdown("### Update Task Status")
    task_id2 = st.number_input("Task ID (for status update)", min_value=1, step=1)
    status = st.selectbox("New Status", ["pending", "in-progress", "completed"])
    if st.button("Update Status"):
        TaskService.change_status(task_id2, status)
        st.info(f"✅ Task {task_id2} updated to '{status}'.")
