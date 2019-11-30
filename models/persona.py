# -*- coding: utf-8 -*-

from odoo import models, fields, api


class persona(models.Model):
    _name = 'upopet.persona'

    dni = fields.Char('Dni', size=9, required=True)
    nombre = fields.Char('Nombre', size=60, required=True)
    apellidos = fields.Char('Apellidos', size=120, required=True)
    direccion = fields.Char('Direccion', size=120, required=True)
    telefono = fields.Integer('Telefono', required=True)
    fechNac = fields.Date('Fecha de nacimiento', required=True)
    email = fields.Char('Email', size=120, required=True)

    mascota_ids = fields.One2many('upopet.mascota', 'persona_id', string='Mascota')
