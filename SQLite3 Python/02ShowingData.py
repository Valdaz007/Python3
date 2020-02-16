import sqlite3

# connect({filename.db}) or connect({:memory}) => Create a DB on Memory (RAM)
conn = sqlite3.connect("test.db")

# Allow the Execution of SQL Commands
c = conn.cursor()

# Execute SQL Command to Return Data
c.execute("SELECT * FROM users WHERE user_lname = 'Volsavai'")

# Return Next Row in Results If Exist Else it will Return 'None'
#print(c.fetchone())

# Return n Number of Rows Specified
#c.fetchmany(n)

# Return a List of the Results
print(c.fetchall())

# Close Object DB
conn.close()