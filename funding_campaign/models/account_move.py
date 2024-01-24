# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import fields, models

class AccountMove(models.Model):  
    _inherit = "account.move"

    funding_campaign_id = fields.Many2one('funding.campaign', string='Funding Campaign')

    