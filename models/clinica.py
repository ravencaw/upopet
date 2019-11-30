# -*- coding: utf-8 -*-

from odoo import models, fields, api


class clinica(models.Model):
     _name = 'upopet.clinica'

     nombre = fields.Char('Nombre', size=70, required=True)
     direccion = fields.Char('Direccion', size=120, required=True)
     cp = fields.Integer('CodigoPostal', size=5, required=True)
     telefono = fields.Integer('Telefono', size=9, required=True)
     logo_clinica = fields.Binary('Logo')

     pruebamedica_ids = fields.One2many('upopet.pruebamedica', 'clinica_id', string='Prueba medica')
     cita_ids = fields.One2many('upopet.cita', 'clinica_id', string='Cita')
