# -*- coding: utf-8 -*-

from odoo import models, fields, api
from tools.pycompat import string_types


class clinica(models.Model):
     _name = 'upopet.clinica'

     id = fields.Integer('ID', size=9, required=True)
     nombre = fields.Char('Nombre', size=70, required=True)
     direccion = fields.Char('Direccion', size=60, required=True)
     cp = fields.Integer('CodigoPostal', size=5, required=True)
     telefono = fields.Char('Telefono', size=9, required=True)

     pruebamedica_ids = fields.Many2many('upopet.pruebamedica', string='Prueba medica')
     cita_ids = fields.One2many('upopet.cita', string='Cita')
