# -*- coding: utf-8 -*-

from odoo import models, fields, api


class laboratorio(models.Model):
     _name = 'upopet.laboratorio'

     cif = fields.Char('CIF', size=9, required=True)
     nombre = fields.Char('Nombre', size=70, required=True)
     direccion = fields.Char('Dirección', size=60, required=True)
     telefono = fields.Integer('Teléfono', size=9, required=True)
     logo_lab = fields.Binary('Logo')

     medicamento_ids = fields.Many2many('upopet.medicamento', string='Medicamento')
