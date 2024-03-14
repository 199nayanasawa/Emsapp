# Function to insert data from CSV file into MySQL table
def insert_data_from_csv(connection, file_path):
    try:
        cursor = connection.cursor()
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header row
            for row in csv_reader:
                cursor.execute("""
                    INSERT INTO emss1(Name, Age, Address, Mobile_Number, Gender,
                                           Education_Details, Salary, DOJ, Department,
                                           Position, Project_Name, Tech_Stack, Annual_Salary,Manager)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)
                """, row)
            connection.commit()
        print("Data inserted successfully")
    except Error as e:
        print(f"Error inserting data into MySQL table: {e}")