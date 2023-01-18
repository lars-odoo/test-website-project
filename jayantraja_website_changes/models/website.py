import logging

from odoo import api, models, http
from odoo.http import request

class Website(models.Model):
    _inherit = 'website'

    @api.model
    def configurator_skip(self):
        super(Website, self).configurator_skip()
        website = self.get_current_website()
        website.theme_id = self.env['ir.module.module'].search([('name', '=', 'theme_default')], limit=1)
    