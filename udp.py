import socket
import json
import xmlrpc.client

url = 'http://10.0.1.100:8069/'
db = 'odoo_219'
username = 'changxizheng@gmail.com'
password = 'Wiznet.219'

ops= ["giaq", "gpm", "gwm","gonf","gair","gplc"]

#print version (confirmed logged in)
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
version = common.version()
print ("Version details:", version)

#print uid -> inputted information is correct
uid = common.authenticate(db, username, password, {})
print ("UID: ", uid)

#combine the url to make the correct xml format for odoo
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', 1460))

while True:
    message, address = server_socket.recvfrom(1024)
    print(message)
    message.decode("utf-8")
    data = json.loads(message)
    for x in ops:
        if data["op"] is x:
            print ("Operation mode = ",x)
        elif data["op"].find(ops[1]) != -1:
            print ("Operaton mode =", ops[1]+data["id"])
        elif data["op"].find(ops[2]) != -1:
            print ("Operation mode =", ops[2]+data["id"])
    #print (data["op"])
    server_socket.sendto(message, address)
    #models.execute_kw(db, uid, password, 'hr.employee', 'write', [[21], {'work_email': data["op"], 'work_phone': data["type"]}])
    #partner = models.execute_kw(db, uid, password, 'hr.employee', 'read', [21], {'fields': ['name', 'work_phone', 'work_email']})
    #print ("Partner:",partner)               








#partner = models.execute_kw(db, uid, password, 'hr.employee', 'read', [9], {'fields': ['name', 'country_id', 'comment']})      
#partner = models.execute_kw(db, uid, password, 'hr.employee', 'check_access_rights', ['read'], {'raise_exception': False})
#partner = models.execute_kw(db, uid, password, 'hr.employee', 'search', [[['company_id', '=', True]]])
#partner = models.execute_kw(db, uid, password, 'hr.employee', 'read', [6], {'fields': ['name', 'work_phone']})

#id = models.execute_kw(db, uid, password, 'hr.employee', 'create', [{'name': "Testing", 'work_phone': "1234"}])

#print ("ID:", id)
