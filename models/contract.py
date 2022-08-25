from odoo import fields, models, api
from odoo.exceptions import ValidationError
import logging

_logger = logging.getLogger(__name__)


class ContractLine(models.Model):
    _inherit = "contract.line"

    @api.depends('contract_id')
    def _compute_partner_id(self):
        for rec in self:
            if rec.contract_id and rec.contract_id.partner_id:
                rec.partner_id = rec.contract_id.partner_id.id
            else:
                rec.partner_id = None

    partner_id = fields.Many2one('res.partner','Cliente',compute=_compute_partner_id,store=True)

