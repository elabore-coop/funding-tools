from odoo import api, fields, models
from odoo.exceptions import UserError

class CampaignStep(models.Model):
    _name = 'campaign.step'
    _description = 'Campaign Step'

    name = fields.Char(string='Name')
    description = fields.Html(string='Description')
    active = fields.Boolean('Active', default=True)
    sequence = fields.Integer()
    funding_campaign_id = fields.Many2one('funding.campaign', string='Funding Campaign')
    step_amount = fields.Float('Step Amount')
    state = fields.Selection(
        [("locked", "Locked"), ("unlocked", "Unlocked"), ("reached", "Reached")],
        string="Status",
        index=True,
        readonly=True,
        default="locked",
        track_visibility="onchange",
        copy=False,
    )