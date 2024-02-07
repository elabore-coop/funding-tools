

from odoo import api, fields, models
from odoo.exceptions import UserError


class FundingCampaign(models.Model):
    _inherit = 'funding.campaign'

    project_id = fields.Many2one('project.project', 'Project')