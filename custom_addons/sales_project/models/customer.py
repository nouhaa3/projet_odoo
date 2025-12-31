from odoo import models, fields


class SalesCustomer(models.Model):
    _name = 'sales.customer'
    _description = 'Sales Customer'

    name = fields.Char(string="Customer Name", required=True)
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    active = fields.Boolean(default=True)
