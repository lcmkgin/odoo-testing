import socket
import json
import xmlrpc.client

url = 'http://10.0.1.100:8069/'
db = 'odoo_219'
username = 'changxizheng@gmail.com'
password = 'Wiznet.219'

ops= ["giaq", "gpm", "gwm","gonf","gair","gplc"]
data = []

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
    info = message.decode("utf-8").split("}{")
    for count in info:
        if count.find("{") == -1:
            temp = "{" + count
        if count.find("}") == -1:
            temp = count + "}"
        result = json.loads(temp)
        data.append(result)
    for y in range(len(data))
        for x in ops:
            if data[y]["op"] == x or data[y]["op"].find(x) != -1:
                print ("Operation mode = ",x)
                if x == "gpm" or x == "gwm":
                    print ("ID = ", data["id"])
    # try:
    #     message, address = server_socket.recvfrom(1024)
    #     print(message)
    #     message.decode("utf-8")
    #     info = message.split("}{")
    #     for count in info:
    #         if count.find("{") == -1:
    #             temp = "{" + count
    #         if count.find("}") == -1:
    #             temp = count + "}"
    #         result = json.loads(temp)
    #         data.append(result)
    #         print (data)
        # for x in ops:
        #     if data["op"] == x or data["op"].find(x) != -1:
        #         print ("Operation mode = ",x)
        #         if x == "gpm" or x == "gwm":
        #             print ("ID = ", data["id"])
        #server_socket.sendto(message, address)
        #models.execute_kw(db, uid, password, 'hr.employee', 'write', [[21], {'work_email': data["op"], 'work_phone': data["type"]}])
        #partner = models.execute_kw(db, uid, password, 'hr.employee', 'read', [21], {'fields': ['name', 'work_phone', 'work_email']})
        #print ("Partner:",partner)  
    # except Exception as e:
    #     print ("Error = ",e)
    #     json_error = "Wrong json format, please resend"
    #     server_socket.sendto(json_error.encode(), address)
    # else:
    #     pass
    # finally:
    #     pass

             








#partner = models.execute_kw(db, uid, password, 'hr.employee', 'read', [9], {'fields': ['name', 'country_id', 'comment']})      
#partner = models.execute_kw(db, uid, password, 'hr.employee', 'check_access_rights', ['read'], {'raise_exception': False})
#partner = models.execute_kw(db, uid, password, 'hr.employee', 'search', [[['company_id', '=', True]]])
#partner = models.execute_kw(db, uid, password, 'hr.employee', 'read', [6], {'fields': ['name', 'work_phone']})

#id = models.execute_kw(db, uid, password, 'hr.employee', 'create', [{'name': "Testing", 'work_phone': "1234"}])

#print ("ID:", id)
