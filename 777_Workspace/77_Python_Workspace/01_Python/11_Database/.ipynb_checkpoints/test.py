import cx_Oracle

dsn_tns = cx_Oracle.makedsn('10.217.231.114', '1524', service_name='TE2SMF2')
conn = cx_Oracle.connect(user='SMF_ODR_MGMT', password= 'admin2_Smf', dsn=dsn_tns)
c = conn.cursor()

c.execute('select * from OM_ORDER_HEADER')
print(c)