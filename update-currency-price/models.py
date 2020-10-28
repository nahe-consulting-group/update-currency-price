from odoo import fields, models, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    @api.model
    def update_currency_and_price(self):
        #para probar se busca un name específico 
        #products = self.env['product.product'].search([('name','=','ADAPTADOR BLUETOOTH 4.0 USB - OEM TP-7183')])
        products = self.env['product.product'].search([('force_currency_id','=',20)])
        currency_usd = self.env['res.currency'].search([('name','=','USD')])
        for product in products:
            product.list_price = product.list_price * currency_usd.rate
            # el tipo de cambio es el de la moneda USD se puede cambiar el name en el search para otra moneda
            product.force_currency_id = 3
            #el id 3 es dolares USD en el caso del servidor que estoy probando con odoo 11
