# 📝 Task Master - A Flask To-Do Web App

**Task Master** is a simple yet powerful web-based To-Do list application built using **Flask** and **SQLite**. It lets users:

- Add tasks  
- Mark tasks as completed  
- Update existing tasks  
- Delete tasks

---

## 🚀 Features

- ✅ Add tasks with a description
- ✏️ Update tasks
- ❌ Delete tasks with confirmation
- ✔️ Mark tasks as completed/incomplete via checkbox
- 📅 View creation date of each task
- 💾 Persistent storage using SQLite
- 🧼 Simple and clean UI using HTML & CSS

---

## 🛠️ Technologies Used

| Component     | Tech Stack                 |
|---------------|-----------------------------|
| Backend       | Python 3, Flask             |
| Frontend      | HTML, Jinja2, CSS           |
| Database      | SQLite (via SQLAlchemy ORM) |
| Templating    | Jinja2 (Flask)              |
| Styling       | Custom CSS (`/static/css/main.css`) |

---

## 📁 Project Structure

```
task-master/
├── app.py                   # Main Flask application
├── templates/
│   ├── base.html            # Base layout
│   ├── index.html           # Homepage with task list
│   └── update.html          # Task update form
├── static/
│   └── css/
│       └── main.css         # Custom styles
├── instance/
│   └── test.db              # SQLite database (auto-created)                
├── README.md                # Project documentation
```

---

## ⚙️ How to Run the Project

### 1. Clone the repository:
```bash
git clone https://github.com/your-username/task-master.git
cd task-master
```

### 2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install required packages:
```bash
pip install -r requirements.txt
```

### 4. Run the Flask app:
```bash
python app.py
```

The app will be running on: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## ✨ Example Usage

- Type a task into the input field and click **"Add Task"**.
- Click the checkbox to mark a task as done.
- Click **"Update"** to edit a task.
- Click **"Delete"** to remove it (confirmation required).

---

## 🛡️ Future Improvements (Optional)

- User authentication (login/signup)
- Categorization of tasks
- Due date & reminders
- Responsive UI with Bootstrap or Tailwind CSS
- Dark mode support

---

## 📄 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
