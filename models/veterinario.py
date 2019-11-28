# -*- coding: utf-8 -*-

from odoo import models, fields, api

class veterinario(models.Model):
    _name = 'upopet.veterinario'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    tratamiento_ids = fields.One2many('upopet.tratamiento', string='Tratamiento')
    cita_ids = fields.One2many('upopet.cita', string='Cita')
    pruebamedica_ids = fields.One2many('upopet.preubamedica', string='Prueba medica')