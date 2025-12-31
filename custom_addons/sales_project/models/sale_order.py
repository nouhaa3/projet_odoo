from odoo import models, fields, api
from odoo.exceptions import ValidationError
from ..blockchain import Blockchain

blockchain = Blockchain()

class SalesOrder(models.Model):
    _name = 'sales.order'
    _description = 'Sales Order'

    name = fields.Char(
        string="Order Reference",
        required=True,
        default="SO"
    )

    customer_id = fields.Many2one(
        'sales.customer',
        string="Customer",
        required=True
    )

    order_date = fields.Date(default=fields.Date.today)

    order_line_ids = fields.One2many(
        'sales.order.line',
        'order_id',
        string="Order Lines"
    )

    amount_total = fields.Float(
        string="Total Amount",
        compute="_compute_amount_total",
        store=True
    )

    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('confirmed', 'Confirmed'),
            ('done', 'Done'),
            ('cancel', 'Cancelled')
        ],
        default='draft'
    )

    seller_id = fields.Many2one(
        'sales.seller',
        string="Seller"
    )

    blockchain_hash = fields.Char(
        string="Blockchain Hash",
        readonly=True,
        copy=False
    )

    @api.depends('order_line_ids.subtotal')
    def _compute_amount_total(self):
        for order in self:
            order.amount_total = sum(
                line.subtotal for line in order.order_line_ids
            )

    # BUTTONS
    def action_confirm(self):
        for order in self:
            data = {
                "order_reference": order.name,
                "customer": order.customer_id.name,
                "amount": order.amount_total,
                "date": str(order.order_date)
            }

            block = blockchain.add_block(data)
            order.blockchain_hash = block.hash

        self.state = 'confirmed'

    def action_done(self):
        for order in self:
            if order.state != 'confirmed':
                raise ValidationError(
                    "You can only mark a confirmed order as Done."
                )
            order.state = 'done'

    def action_cancel(self):
        self.state = 'cancel'
