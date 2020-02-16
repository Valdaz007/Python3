import sqlite3

# connect({filename.db}) or connect({:memory}) => Create a DB on Memory (RAM)
conn = sqlite3.connect("test.db")

# Allow the Execution of SQL Commands
c = conn.cursor()

# Execute SQL Command to Insert Values into Table
c.execute("INSERT INTO users VALUES ('Absalom', 'Volsavai', 20241004)")

# Commit Change
conn.commit()

# Close Object DB
conn.close()