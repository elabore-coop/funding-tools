# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import fields, models

class Lead(models.Model):
    _inherit = 'crm.lead'

    def _compute_is_funding_campaign_lead(self):
        for lead in self:
            lead.is_funding_campaign_lead = True if lead.funding_campaign_id else False

    
    funding_campaign_id = fields.Many2one('funding.campaign', string='Funding Campaign')
    is_funding_campaign_lead = fields.Boolean('Is Funding Campaign Lead', compute="_compute_is_funding_campaign_lead")

    def _prepare_opportunity_quotation_context(self):
        context = super(Lead,self)._prepare_opportunity_quotation_context()
        if self.funding_campaign_id:
            context["funding_campaign_id"] = self.funding_campaign_id.id
        return context