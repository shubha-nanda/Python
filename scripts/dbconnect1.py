import cx_Oracle
con=cx_Oracle.connect('scott/tiger@localhost')
print(con.version)
con.close()