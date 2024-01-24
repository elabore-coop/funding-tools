

from odoo import api, fields, models
from odoo.exceptions import UserError


class FundingCampaign(models.Model):
    _name = 'funding.campaign'
    _description = 'Funding Campaign'

    def _compute_amounts(self):
        for campaign in self:
            # Wished
            campaign.total_wished_amount = sum(campaign.campaign_step_ids.mapped("step_amount"))
            # Promised
            sale_order_ids = self.order_ids.filtered(lambda x: x.state == "sale")
            campaign.promised_amount = sum(sale_order_ids.mapped("amount_total"))
            # Paid
            invoice_ids = self.invoice_ids.filtered(lambda x: x.state == "posted")
            campaign.paid_amount = sum(invoice_ids.mapped("amount_total"))
            

    name = fields.Char(string='Name')
    description = fields.Html(string='Description')
    active = fields.Boolean('Active', default=True)

    product_id = fields.Many2one('product.product', string='Product')
    state = fields.Selection(
        [("draft", "Draft"), ("opened", "Opened"), ("closed", "Closed")],
        string="Status",
        index=True,
        readonly=True,
        default="draft",
        track_visibility="onchange",
        copy=False,
    )
    opportunity_ids = fields.One2many('crm.lead', 'funding_campaign_id', string="Participants")
    order_ids = fields.One2many('sale.order', 'funding_campaign_id', string='Sale Orders')
    invoice_ids = fields.One2many('account.move', 'funding_campaign_id', string='Invoices')
    nb_participants = fields.Integer(
        string='Number of Potential Participants',
        store=False, readonly=True, compute='_compute_participants')
    promised_amount = fields.Float('Promised Amount', readonly=True, compute="_compute_amounts")
    paid_amount = fields.Float('Paid Amount', readonly=True, compute="_compute_amounts")

    campaign_step_ids = fields.One2many('campaign.step', 'funding_campaign_id', string='Campaign Steps')
    total_wished_amount = fields.Float('Total Wished Amount', readonly=True, compute="_compute_amounts")

    def action_draft_campaign(self):
        self.state = "draft"

    def action_open_campaign(self):
        self.state = "opened"

    def action_close_campaign(self):
        self.state = "closed"

    def add_registration(self):
        self.ensure_one()
        if self.state != "opened":
            raise UserError("This campaign is not opened, no registration can be added.")

    @api.depends('opportunity_ids')
    def _compute_participants(self):
        for campaign in self:
            campaign.nb_participants = len(campaign.opportunity_ids)
