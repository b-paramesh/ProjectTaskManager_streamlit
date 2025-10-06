# 📝 ProjectTaskManager_Streamlit

A **Task Management System** built with Python, Supabase, and Streamlit.  
Manage users, tasks, and assignments through both **CLI** and **web interface**.

---

## 🚀 Features

### **User Management**
- 👤 Add, edit, and delete users
- 💻 Store username, email, and password hash

### **Task Management**
- 📝 Add, edit, and delete tasks  
- ⏳ Track task status (`pending`, `in-progress`, `completed`)  
- 📅 Optional deadlines for tasks  

### **Task Assignment**
- 👥 Assign tasks to specific users  
- ✅ Update task status individually  

### **Filter Tasks**
- 🔍 Filter tasks by `user_id`, `status`, or `deadline`

### **Web Interface**
- 🌐 Streamlit dashboard for easier task and user management
- 📊 Visualize task status and assignments

---

## 🛠 Tech Stack

- Python 3.x
- Supabase (PostgreSQL backend)
- Streamlit for web interface
- `python-dotenv` for environment variables

---

## ⚡ Setup Instructions

1. **Clone the repository**
```bash

python -m venv venv
# Windows
venv\Scripts\activate
# Linux / Mac
source venv/bin/activate

pip install -r requirements.txt

SUPABASE_URL="https://your-supabase-url.supabase.co"
SUPABASE_KEY="your-supabase-api-key"

python -m cli.main

streamlit run app.py

📋 Example Actions (CLI)
Action	Inputs	Predicted Output
Add User	Username: paramesh
Email: bhupathiparamesh@gmail.com

Password: paramesh	✅ User added successfully!
Edit User	User ID: 1
Field: username
New value: param	✅ User updated successfully!
Delete User	User ID: 1	✅ User deleted successfully!
Add Task	Title: study
Description: exam study
Deadline: 2025-09-24	✅ Task added successfully!
Edit Task	Task ID: 1
Field: title
New value: study harder	✅ Task updated successfully!
Delete Task	Task ID: 1	✅ Task deleted successfully!
Assign Task	Task ID: 1
User ID: 1	✅ Task assigned successfully!
Update Task Status	Task ID: 1
Status: completed	✅ Task status updated successfully!
List Tasks	Filter: status
Value: completed	{'task_id': 1, 'title': 'study', 'status': 'completed', ...}

📂 Project Structure
ProjectTaskManager_streamlit/
│
├─ cli/                 # CLI interface
│   └─ main.py
├─ service/             # Business logic
│   ├─ user_service.py
│   ├─ task_service.py
│   └─ assignment_service.py
├─ dao/                 # Data Access Objects (Supabase interactions)
│   ├─ user_dao.py
│   ├─ task_dao.py
│   └─ assignment_dao.py
├─ app.py               # Streamlit application
├─ venv/                # Python virtual environment
├─ requirements.txt
└─ README.md

🌟 Future Enhancements

🔐 Add user authentication (login/logout)

✉️ Email notifications for task deadlines

📈 Enhanced dashboards and charts in Streamlit
