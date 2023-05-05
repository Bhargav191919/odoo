from odoo import models, fields, api,_

class ResPartner(models.Model):
	_inherit = 'res.partner'

	def add(self):
		pass

	def action_update(self):
		return{
		'name': _('Update Contact'),
        'view_mode': 'form',
        'res_model': 'contact.update',
        'view_id': self.env.ref('test2.contact_update_wizard_view').id,
        'type': 'ir.actions.act_window',
        'target': 'new'
		}
		return self.action_update()