url = 'http://10.0.1.100:8069/'
db = 'odoo_219'
username = 'changxizheng@gmail.com'
password = 'Wiznet.219'

import xmlrpc.client

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
version = common.version()

print ("Version details:", version)

uid = common.authenticate(db, username, password, {})
print ("UID: ", uid)

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
#partner = models.execute_kw(db, uid, password, 'hr.employee', 'read', [9], {'fields': ['name', 'country_id', 'comment']})      
#partner = models.execute_kw(db, uid, password, 'hr.employee', 'check_access_rights', ['read'], {'raise_exception': False})
#partner = models.execute_kw(db, uid, password, 'hr.employee', 'search', [[['company_id', '=', True]]])
#partner = models.execute_kw(db, uid, password, 'hr.employee', 'read', [6], {'fields': ['name', 'work_phone']})

#id = models.execute_kw(db, uid, password, 'hr.employee', 'create', [{'name': "Testing", 'work_phone': "1234"}])
models.execute_kw(db, uid, password, 'hr.employee', 'write', [[21], {'work_email': "test@hi.com", 'work_phone': "10000"}])
#print ("ID:", id)
partner = models.execute_kw(db, uid, password, 'hr.employee', 'read', [21], {'fields': ['name', 'work_phone', 'work_email']})
print ("Partner:",partner)               
