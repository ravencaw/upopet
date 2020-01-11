# -*- coding: utf-8 -*-

from odoo import models, fields, api


class laboratorio(models.Model):
     _name = 'upopet.laboratorio'

     _rec_name = 'cif'
     cif = fields.Char('CIF', size=9, required=True)
     nombre = fields.Char('Nombre', size=70, required=True)
     direccion = fields.Char('Dirección', size=60, required=True)
     telefono = fields.Integer('Teléfono', size=9, required=True)
     logo_lab = fields.Binary('Logo')

     medicamento_ids = fields.Many2many('upopet.medicamento', string='Medicamento')

     @api.one 
     @api.constrains('cif')
     def _check_cif(self):

      if len(self.cif) != 9:
        raise models.ValidationError('El CIF debe constar de 9 dígitos')

     @api.one 
     @api.constrains('telefono')
     def _check_telefono(self):

      if len(str(self.telefono)) != 9:
        raise models.ValidationError('El teléfono debe constar de 9 dígitos')
