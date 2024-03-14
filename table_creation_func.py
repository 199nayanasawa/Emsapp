# Function to create MySQL table
def create_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS emss1 (
                Name VARCHAR(255),
                Age INT,
                Address VARCHAR(255),
                Mobile_Number VARCHAR(255),
                Gender VARCHAR(10),
                Education_Details VARCHAR(50),
                Salary INT,
                DOJ DATE,
                Department VARCHAR(255),
                Position VARCHAR(255),
                Project_Name VARCHAR(255),
                Tech_Stack VARCHAR(255),
                Manager VARCHAR(255)
            )
        """)
        print("Table created successfully.")
    except Error as e:
        print(f"Error creating table: {e}")
    finally:
        if connection.is_connected():
            cursor.close()