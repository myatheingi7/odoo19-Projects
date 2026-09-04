from odoo import fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_library_member = fields.Boolean(string='Is Library Member')
    member_code = fields.Char(string='Member Code')
    membership_date = fields.Date(string='Membership Date')