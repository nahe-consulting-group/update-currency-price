from odoo import fields, models, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.model
    def update_currency_and_price(self):
        #para probar se busca un name específico 
        #products = self.env['product.product'].search([('name','=','ADAPTADOR BLUETOOTH 4.0 USB - OEM TP-7183')])
        products = self.env['product.template'].search([('currency_id','=',1)])
        for product in products:
            product.list_price = product.list_price / 90
            # el numero por el que divide es el tipo de cambio hardcodeado pero quiero que tome el valor rate de force_currency_id
            product.force_currency_id = 3
            #el id 3 es dolares USD en el caso del servidor qu eestoy probando con odoo 11
