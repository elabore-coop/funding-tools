# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import fields, models

class SaleOrder(models.Model):  
    _inherit = "sale.order"

    def _compute_is_funding_campaign_order(self):
        for lead in self:
            lead.is_funding_campaign_order = True if lead.funding_campaign_id else False

    
    funding_campaign_id = fields.Many2one('funding.campaign', string='Funding Campaign')
    is_funding_campaign_order = fields.Boolean('Is Funding Campaign Order', compute="_compute_is_funding_campaign_order")

    