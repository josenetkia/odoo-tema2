{
 'name':'Library Management',
 'description': 'Libreria Tema 2 Curso Odoo',
 'author': 'Jose',
 'depends': ['base'],
 'application': True,
 'data':[
     'security/library_security.xml',
     'security/ir.model.access.csv',
     'views/library_menu.xml',
     'views/book_view.xml',
     'views/book_list_template.xml'

 ]
 }


