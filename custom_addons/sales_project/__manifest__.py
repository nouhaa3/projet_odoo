{
    'name': 'Sales Project',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Custom sales management module',
    'description': """
Sales management module based on Odoo Community.
Includes customers, sales orders, sellers, and stock management.
""",
    'author': 'ISIMS',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/customer_views.xml',
        'views/sale_order_views.xml',
        'views/seller_views.xml',
        'views/order_line_views.xml',
        'views/sales_seller_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
}
