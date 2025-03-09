{
    'name': 'Restrict Duplicate Button',
    'version': '17.0.1.0.0',
    'summary': 'Restringe el botón de duplicar en órdenes de venta a usuarios específicos.',
    'author': 'Tu Nombre o Empresa',
    'license': 'AGPL-3',
    'category': 'Sales',
    'depends': ['sale', 'sale_management'],
    'data': [
        'security/restrict_duplicate_group.xml',
        'security/ir.model.access.csv',
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'application': False,
}
