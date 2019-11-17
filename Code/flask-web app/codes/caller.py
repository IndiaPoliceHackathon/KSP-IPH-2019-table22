import os
import pysqlite3
data_path = os.path.expanduser('~')+r"\AppData\Local\Google\Chrome\User Data\Default"
files = os.listdir(data_path)
history_db = os.path.join(data_path, 'history')

c = pysqlite3.connect(history_db)
cursor = c.cursor()
select_statement = "SELECT urls.url, urls.visit_count FROM urls, visits WHERE urls.id = visits.url;"
cursor.execute(select_statement)

results = cursor.fetchall()


