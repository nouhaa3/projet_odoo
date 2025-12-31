from odoo import models, fields, api


class SalesOrderLine(models.Model):
    _name = 'sales.order.line'
    _description = 'Sales Order Line'

    name = fields.Char(string="Product / Service", required=True)
    quantity = fields.Integer(string="Quantity", default=1)
    price_unit = fields.Float(string="Unit Price")

    is_discounted = fields.Boolean(string="Discount Applied")

    order_id = fields.Many2one(
        'sales.order',
        string="Sales Order",
        required=True,
        ondelete='cascade'
    )

    subtotal = fields.Float(
        string="Subtotal",
        compute="_compute_subtotal",
        store=True
    )

    @api.depends('quantity', 'price_unit')
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = line.quantity * line.price_unit
