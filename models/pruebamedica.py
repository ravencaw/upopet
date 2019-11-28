# -*- coding: utf-8 -*-

from odoo import models, fields, api

class pruebamedica(models.Model):
     _name = 'upopet.pruebamedica'

     cif = fields.Char('CIF', size = 9, required = True)
     nombre = fields.Char('Nombre', size = 70, required = True)
     direccion = fields.Char('Direccion', size = 60, required = True)
     telefono = fields.Char('Telefono', size = 9, required = True)

     medicamento_ids = fields.Many2many('medicamento.upopet', string='Medicamento')
