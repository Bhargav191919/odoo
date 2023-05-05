from odoo import models, fields, api,_

class ContactUpdate(models.TransientModel):
    _name = 'contact.update'
    _description = "update Contact"


    ref = fields.Char(String="Reference")
    industry = fields.Many2one('res.partner.industry',String="Industry")


    def update(self):
        active_ids = self.env.context.get('active_ids')
        a = self.env['res.partner'].browse(active_ids)
        for equip_ids in a:
            equip_ids.write({'ref': self.ref, 'industry_id':self.industry})