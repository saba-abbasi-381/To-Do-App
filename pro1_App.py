from pro1 import ToDo
import streamlit as st

todo = ToDo()

st.title("To-Do App")
st.header("Manage your daily task")

st.sidebar.title("Menu")
choice = st.sidebar.selectbox("Choose option", options=["Add", "View", "Update", "Search", "Delete", "Clear"])

if choice == "Add":
    task = st.text_input("enter task : ").lower()
    if st.button("Add Task"):
        if task:
            todo.add_task(task)
            st.success("Task added successfully!")
        else:
            st.warning("Please enter a task")

elif choice == "View":
    if st.button("View task"):
        st.text(todo.view_task())
        
elif choice == "Update":
    st.write("Current Tasks:")
    if not todo.task_lst:
        st.warning("No task available")
    else:
        st.text(todo.view_task())
    index = st.number_input("select task number for updating: ",min_value = 1, step=1)
    new_task = st.text_input("enter new task: ").lower()
    if st.button("Update task"):
        try:
            todo.update_task(index, new_task)
            st.success("Task updated!")
        except:
            st.error("Invalid task number")

elif choice == "Delete":
    st.write("Current Tasks:")
    if not todo.task_lst:
        st.warning("No task available")
    else:
        st.text(todo.view_task())
    index = st.number_input("Select task number: ", min_value=1, step=1)
    if st.button("Delete Task"):
        try:
            todo.delete_task(index)
            st.success("Task deleted successfully")
        except:
            st.warning("Invalid task number")

elif choice == "Search":
    keyword = st.text_input("Enter Task name for searching: ").lower()
    if st.button("Search Task"):
        if keyword:
            result = todo.search_task(keyword)
            st.write(result)
        else:
            st.warning("Please enter a keyword")

elif choice == "Clear":
    if st.button("Clear task"):
        todo.clear_all()
        st.success("All tasks removed successfully")

