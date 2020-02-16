import sqlite3

# connect({filename.db}) or connect({:memory}) => Create a DB on Memory (RAM)
conn = sqlite3.connect("test.db")

# Allow the Execution of SQL Commands
c = conn.cursor()

conn.execute("DELETE FROM users WHERE user_fname = 'Absalom'")

# Commit Change
conn.commit()

# Close Object DB
conn.close()

