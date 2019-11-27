# -*- coding: utf-8 -*-

from odoo import models, fields, api

class medicamento(models.Model):
     _name = 'medicamento.upopet'

     cif_lab = fields.Char()
     nombre = fields.Char()
     referencia = fields.Char()
     fechaCaducidad = fields.Datetime()
     prospecto = fields.Char()

