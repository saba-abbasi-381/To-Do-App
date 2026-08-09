# ✅ To-Do App

A simple task management web application built with **Python and Streamlit**. The application allows users to create, view, update, search, and delete daily tasks while storing tasks in a local text file.

## 📌 Overview

The **To-Do App** is a Python-based task management application designed to practice fundamental programming concepts and build an interactive user interface with Streamlit.

The project uses a class-based backend to manage tasks and a Streamlit frontend for user interaction.

Tasks are stored in a local `task.txt` file, allowing the application to load previously saved tasks when it starts.

## ✨ Features

* ➕ Add new tasks
* 👀 View all saved tasks
* ✏️ Update an existing task
* 🔍 Search tasks by keyword
* 🗑️ Delete individual tasks
* 🧹 Clear all tasks
* 💾 Save tasks to a local text file
* 🔄 Load previously saved tasks when the application starts
* 🖥️ Interactive Streamlit interface

## 🛠️ Technologies Used

* **Python**
* **Streamlit**
* **Object-Oriented Programming (OOP)**
* **File Handling**
* **Text File Storage**

## 🧩 Project Structure

```text
To-Do-App/
│
├── app.py
├── pro1.py
├── task.txt
└── README.md
```

### `app.py`

Contains the Streamlit frontend and handles:

* User input
* Menu navigation
* Button interactions
* Displaying tasks
* Showing success, warning, and error messages

### `pro1.py`

Contains the `ToDo` class and the main task-management logic.

The class includes methods for:

* Loading tasks
* Saving tasks
* Adding tasks
* Viewing tasks
* Updating tasks
* Searching tasks
* Deleting tasks
* Clearing all tasks

### `task.txt`

A local text file used to store tasks.

Each task is saved on a separate line.

## 🔄 How It Works

The application follows a simple workflow:

```text
User
  ↓
Streamlit Interface
  ↓
ToDo Class
  ↓
Task Operations
  ↓
task.txt
```

### Adding a Task

1. Select **Add** from the sidebar.
2. Enter a task.
3. Click **Add Task**.
4. The task is added to the task list.
5. The updated list is saved to `task.txt`.

### Viewing Tasks

The **View** option displays all currently stored tasks with their corresponding numbers.

### Updating a Task

1. Select **Update**.
2. View the current tasks.
3. Enter the task number.
4. Enter the new task.
5. Click **Update Task**.

### Searching Tasks

Users can enter a keyword to search through existing tasks.

### Deleting a Task

Users can select a task number and remove that task from the list.

### Clearing Tasks

The **Clear** option removes all tasks from the current task list and updates the saved file.

## ⚙️ Installation & Usage

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Open the project directory

```bash
cd To-Do-App
```

### 3. Install Streamlit

```bash
pip install streamlit
```

### 4. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## 🧠 Python Concepts Practiced

This project helped me practice several important Python concepts:

* Classes and objects
* Constructors
* Instance attributes
* Methods
* Lists
* Loops
* Conditional statements
* String handling
* Exception handling
* File reading and writing
* Persistent local data storage
* Streamlit application development

## 📚 What I Learned

Building this project helped me understand how a simple Python program can be transformed into an interactive application.

I practiced separating the **task-management logic** from the **user interface**, using file handling to preserve data, and designing different operations for managing a collection of tasks.

The project also strengthened my understanding of Object-Oriented Programming and basic application structure.

## 🔮 Future Improvements

Possible improvements for future versions include:

* Add task completion status
* Add task priorities
* Add due dates
* Add task categories
* Add confirmation before clearing all tasks
* Improve task search functionality
* Add a database instead of text-file storage
* Add better validation for task numbers
* Add task sorting and filtering

## 👩‍💻 Author

**Saba Abbasi**

Aspiring AI Engineer | Python Developer
