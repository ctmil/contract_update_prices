from odoo import fields,models, api, _
from odoo.exceptions import UserError, ValidationError
import logging
from datetime import date

_logger = logging.getLogger(__name__)

class UpdateContractsWizard(models.TransientModel):
    _name = 'update.contracts.wizard'
    _description = 'update.contracts.wizard'

    new_price = fields.Float('Nuevo precio')

    def btn_confirm(self):
        active_ids = self.env.context.get('active_ids',[])
        for line in self.env['contract.line'].browse(active_ids).filtered(lambda l: l.state == 'in-progress'):
            line.price_unit = self.new_price
