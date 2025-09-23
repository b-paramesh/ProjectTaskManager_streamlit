# 📝 Task Management CLI

A **Command-Line Interface (CLI) Task Management System** built with Python and Supabase.  
Manage users, tasks, and assignments from your terminal.

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

---

## 🛠 Tech Stack

- Python 3.x
- Supabase (PostgreSQL backend)
- `python-dotenv` for environment variables

---

## ⚡ Setup Instructions

1. **Clone the repository**
```bash
git clone <your_repo_url>
cd projectTaskManager

2. Create and activate a virtual environment

python -m venv venv
# Windows
venv\Scripts\activate
# Linux / Mac
source venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

4. Setup environment variables

Create a .env file in the root:

SUPABASE_URL="https://your-supabase-url.supabase.co"
SUPABASE_KEY="your-supabase-api-key"

5. Run the CLI

python -m cli.main


| Action                 | Inputs                                                                                                             | Predicted Output                                               |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------- |
| **Add User**           | Username: paramesh<br>Email: [bhupathiparamesh@gmail.com](mailto:bhupathiparamesh@gmail.com)<br>Password: paramesh | ✅ User added successfully!                                     |
| **Edit User**          | User ID: 1<br>Field: username<br>New value: param                                                                  | ✅ User updated successfully!                                   |
| **Delete User**        | User ID: 1                                                                                                         | ✅ User deleted successfully!                                   |
| **Add Task**           | Title: study<br>Description: exam study<br>Deadline: 2025-09-24                                                    | ✅ Task added successfully!                                     |
| **Edit Task**          | Task ID: 1<br>Field: title<br>New value: study harder                                                              | ✅ Task updated successfully!                                   |
| **Delete Task**        | Task ID: 1                                                                                                         | ✅ Task deleted successfully!                                   |
| **Assign Task**        | Task ID: 1<br>User ID: 1                                                                                           | ✅ Task assigned successfully!                                  |
| **Update Task Status** | Task ID: 1<br>Status: completed                                                                                    | ✅ Task status updated successfully!                            |
| **List Tasks**         | Filter: status<br>Value: completed                                                                                 | `{'task_id': 1, 'title': 'study', 'status': 'completed', ...}` |


projectTaskManager/
│
├─ cli/                 # Main CLI entry point
│   └─ main.py
├─ service/             # Business logic
│   ├─ user_service.py
│   ├─ task_service.py
│   └─ assignment_service.py
├─ dao/                 # Data Access Objects (Supabase interactions)
│   ├─ user_dao.py
│   ├─ task_dao.py
│   └─ assignment_dao.py
├─ venv/                # Python virtual environment
├─ requirements.txt
└─ README.md

🌟 Future Enhancements

🔐 Add user authentication (login/logout)

🌐 Integrate Streamlit UI for a web-based interface

✉️ Email notifications for task deadlines
