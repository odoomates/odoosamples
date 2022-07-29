import xmlrpc.client

url = 'http://0.0.0.0:8015'
db = 'dev_db'
username = 'admin'
password = 'admin'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
#authentication
uid = common.authenticate(db, username, password, {})
if uid:
	print("authentication succeeded")
	models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

	#search, read method
	partners = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=', True]]], {'limit': 7})
	partners_count = models.execute_kw(db, uid, password, 'res.partner', 'search_count', [[['is_company', '=', True]]])
	partner_rec = models.execute_kw(db, uid, password, 'res.partner', 'read', [partners], {'fields': ['id', 'name']})

	#search read
	partner_rec2 = models.execute_kw(db, uid, password, 'res.partner', 'search_read', [[['is_company', '=', True]]], {'fields': ['id', 'name']})
	
	#create method
	vals = {
		'name': "Odoo Mates External API",
		'email': "odoomates@gmail.com"
	}
	created_id = models.execute_kw(db, uid, password, 'res.partner', 'create', [vals])
	print("created record ->", created_id)

	#write, update, delete method
	partners = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['email', '=', 'odoomates@gmail.com']]])
	models.execute_kw(db, uid, password, 'res.partner', 'write', [partners, {'mobile': "3333333", "phone": "88888888"}])
	models.execute_kw(db, uid, password, 'res.partner', 'unlink', [partners])

else:
	print("authentication failed")