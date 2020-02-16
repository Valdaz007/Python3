import sqlite3

# connect({filename.db}) or connect({:memory}) => Create a DB on Memory (RAM)
conn = sqlite3.connect("test.db")

# Allow the Execution of SQL Commands
c = conn.cursor()

# Create a Table
c.execute("""CREATE TABLE users (
            user_fname text,
            user_lname text,
            user_id interger
)""")

# Commit Change
conn.commit()

# Close Object DB
conn.close()