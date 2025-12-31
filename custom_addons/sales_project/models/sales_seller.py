from odoo import models, fields, api


class SalesSeller(models.Model):
    _name = 'sales.seller'
    _description = 'Sales Seller'

    name = fields.Char(required=True)
    email = fields.Char()

    is_available = fields.Boolean(
        string="Available",
        compute="_compute_is_available",
        store=True
    )

    order_ids = fields.One2many(
        'sales.order',
        'seller_id',
        string="Sales Orders"
    )

@api.depends('order_ids.state')
def _compute_is_available(self):
    for seller in self:
        active_orders = seller.order_ids.filtered(
            lambda o: o.state == 'confirmed'
        )
        seller.is_available = not bool(active_orders)
