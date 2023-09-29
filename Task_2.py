import psycopg2

# connect to the Postgres DB
db_connection = psycopg2.connect(
    host="localhost",
    database="task-manager",
    user="postgres",
    password="123456"
)


cursor = db_connection.cursor() # cursor for interact with DB

# query for creating table
# create_table_query = """
# CREATE TABLE IF NOT EXISTS tasks (
#     id SERIAL PRIMARY KEY,
#     task TEXT NOT NULL,
#     completed BOOLEAN
# );
# """


cursor.execute(create_table_query)  # execute the query


db_connection.commit() # commit to DB



# db_connection.close() # close connection if needed


# to see the data for DB
# query = """select * from tasks"""
# cursor.execute(query)
# result = cursor.fetchall()
# print(result)

# Functions for CRUD operation
def add_task(task):  # add new task
    query = "INSERT INTO tasks (task, completed) VALUES (%s, %s)"
    values = (task, False)
    cursor.execute(query, values)
    db_connection.commit()
    print("Task added successfully!")


def get_tasks():  # get the added task 
    query = "SELECT * FROM tasks"
    cursor.execute(query)
    tasks = cursor.fetchall()
    return tasks


def update_task(task_id, task, completed):  # update the task
    query = "UPDATE tasks SET task = %s, completed = %s WHERE id = %s"
    values = (task, completed, task_id)
    cursor.execute(query, values)
    db_connection.commit()
    print("Task updated successfully!")


def delete_task(task_id):  # delete the completed task
    query = "DELETE FROM tasks WHERE id = %s"
    values = (task_id,)
    cursor.execute(query, values)
    db_connection.commit()
    print("Task deleted successfully!")

# execute the code
if __name__ == "__main__":
    while True:
        print("\nOptions:")
        print("1. Add a new task")
        print("2. Get all tasks")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "2":
            tasks = get_tasks()
            for task in tasks:
                print(task)
        elif choice == "3":
            task_id = input("Enter the task ID to update: ")
            task = input("Enter the new task: ")
            completed = input("Enter 'True' if the task is completed, 'False' otherwise: ").lower() == 'true'
            update_task(task_id, task, completed)
        elif choice == "4":
            task_id = input("Enter the task ID to delete: ")
            delete_task(task_id)
        elif choice == "5":
            break

# close the DB connection
db_connection.close()


"""
Implements a basic task manager application that allows users to execute CRUD (Create, Read, Update, and Delete) 
activities on database-stored tasks. 

1. Database Connection: Establishing a connection to a PostgreSQL database. The connection parameters 
(host, database name, username, and password)

2. Creating a Cursor: Following the database connection, a cursor created in order to interact 
   with the database by running SQL queries.

3. Table Creation: The tables have the following fields: task (ask description), completed (boolean), and id (auto-incremented).

5. CRUD Functions: CRUD operations on tasks within the "tasks" table:
     add_task(task): Inserts a new task and sets its completion state to False.
     get_tasks(): Retrieves all tasks from table and returns them.
     update_task(task_id, task, completed): Updates a task and completion state based on the task's id.
     delete_task(task_id): Deletes a task using the task_id as a basis.


"""