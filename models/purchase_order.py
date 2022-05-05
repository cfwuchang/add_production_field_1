from odoo import api, fields, models, tools, _

class PurchasePurchase(models.Model):
    _inherit = 'stock.move'

    x_createUid = fields.Char(string=u'bom列表行创建人',readonly='True',compute='_get_createUid')


    def _get_createUid(self):
        for obj in self:	
            obj.x_createUid=obj.bom_line_id.create_uid.name

    
    
