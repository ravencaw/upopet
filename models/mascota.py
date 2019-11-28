#-*- coding: utf-8 -*-

from odoo import models, fields, api

class mascota(models.Model):
    _name = 'upopet.mascota'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
#
    cita_ids = fields.One2many('upopet.cita', string='Cita')
    tratamiento_ids = fields.One2many('upopet.tratamiento', string='Tratamiento')
    pruebamedica_ids = fields.One2many('upopet.pruebamedica', string='Prueba medica')
    persona_ids = fields.Many2one('upopet.persona', string='Persona')