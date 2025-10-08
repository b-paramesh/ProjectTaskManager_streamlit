import streamlit as st
import pandas as pd
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
    tab1, tab2, tab3, tab4 = st.tabs(["➕ Add User", "✏️ Edit User", "🗑️ Delete User", "📋 List Users"])

    # --- Add User ---
    with tab1:
        st.markdown("### Add New User")
        with st.form(key="add_user_form"):
            username = st.text_input("Username")
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            submit = st.form_submit_button("Add User")
            if submit:
                UserService.create_user(username, email, password)
                st.success(f"✅ User '{username}' added successfully!")

    # --- Edit User ---
    with tab2:
        st.markdown("### Edit User")
        with st.form(key="edit_user_form"):
            user_id = st.number_input("User ID", min_value=1, step=1)
            field = st.selectbox("Field to edit", ["username", "email", "password_hash"])
            value = st.text_input("New value")
            submit = st.form_submit_button("Update User")
            if submit:
                UserService.update_user(user_id, **{field: value})
                st.success("✏️ User updated successfully!")

    # --- Delete User ---
    with tab3:
        st.markdown("### Delete User")
        with st.form(key="delete_user_form"):
            user_id = st.number_input("Enter User ID to delete", min_value=1, step=1)
            submit = st.form_submit_button("Delete User")
            if submit:
                UserService.remove_user(user_id)
                st.error(f"🗑️ User {user_id} deleted successfully!")

    # --- List Users ---
    with tab4:
        st.markdown("### All Users")
        if hasattr(UserService, "list_all_users"):
            users = UserService.list_all_users()
            if users:
                st.dataframe(pd.DataFrame(users))
            else:
                st.warning("No users found.")
        else:
            st.info("ℹ️ User listing not implemented in UserService.")

# ------------------ TASKS ------------------
elif menu == "Tasks":
    st.subheader("📝 Manage Tasks")
    tab1, tab2, tab3, tab4 = st.tabs(["➕ Add Task", "✏️ Edit Task", "🗑️ Delete Task", "📋 List Tasks"])

    # --- Add Task ---
    with tab1:
        st.markdown("### Add New Task")
        with st.form(key="add_task_form"):
            title = st.text_input("Task Title")
            description = st.text_area("Task Description")
            deadline = st.text_input("Deadline (YYYY-MM-DD) or leave blank")
            submit = st.form_submit_button("Add Task")
            if submit:
                TaskService.create_task(title, description, deadline or None)
                st.success("✅ Task added successfully!")

    # --- Edit Task ---
    with tab2:
        st.markdown("### Edit Task")
        with st.form(key="edit_task_form"):
            task_id = st.number_input("Task ID", min_value=1, step=1)
            field = st.selectbox("Field to edit", ["title", "description", "status", "deadline"])
            value = st.text_input("New value")
            submit = st.form_submit_button("Update Task")
            if submit:
                TaskService.update_task(task_id, **{field: value})
                st.success("✏️ Task updated successfully!")

    # --- Delete Task ---
    with tab3:
        st.markdown("### Delete Task")
        with st.form(key="delete_task_form"):
            task_id = st.number_input("Enter Task ID to delete", min_value=1, step=1)
            submit = st.form_submit_button("Delete Task")
            if submit:
                TaskService.delete_task(task_id)
                st.error(f"🗑️ Task {task_id} deleted successfully!")

    # --- List Tasks ---
    with tab4:
        st.markdown("### All Tasks")
        filter_by = st.selectbox("Filter by", ["None", "user_id", "status", "deadline"])
        value = st.text_input("Filter value (optional)")
        tasks = TaskService.list_tasks(filter_by if filter_by != "None" else None, value if value else None)
        if tasks:
            st.dataframe(pd.DataFrame(tasks))
        else:
            st.warning("No tasks found.")

# ------------------ ASSIGNMENTS ------------------
elif menu == "Assignments":
    st.subheader("📌 Assign Tasks")

    # --- Assign Task ---
    st.markdown("### ➕ Assign Task")
    with st.form(key="assign_task_form"):
        task_id = st.number_input("Task ID", min_value=1, step=1)
        user_id = st.number_input("User ID", min_value=1, step=1)
        submit = st.form_submit_button("Assign Task")
        if submit:
            AssignmentService.assign_task(task_id, user_id)
            st.success(f"📌 Task {task_id} assigned to User {user_id} successfully!")

    # --- Update Task Status ---
    st.markdown("### 🔄 Update Task Status")
    with st.form(key="update_status_form"):
        task_id2 = st.number_input("Task ID (for status update)", min_value=1, step=1)
        status = st.selectbox("New Status", ["pending", "in-progress", "completed"])
        submit = st.form_submit_button("Update Status")
        if submit:
            TaskService.change_status(task_id2, status)
            st.info(f"✅ Task {task_id2} updated to '{status}'.")
