# -*- coding: utf-8 -*-

from odoo import models, fields, api


class mascota(models.Model):
    _name = 'upopet.mascota'

    numChip = fields.Integer('Numero de chip', required=True)
    nombre = fields.Char('Nombre', size=15, required=True)
    especie = fields.Char('Especie', size=20, required=True)
    raza = fields.Char('Raza', size=20, required=True)
    edad = fields.Integer('Edad')
    color = fields.Char('Color', size=20)
    peso = fields.Float('Peso', required=True, digits=(4, 4))
    tam = fields.Float('Tamaño', required=True, digits=(1, 2))
    sexo = fields.Selection([('m', 'Macho'),
                                     ('h', 'Hembra'), ],
                                     'Sexo')
    foto_mascota = fields.Binary('Foto')

    cita_ids = fields.One2many('upopet.cita', 'mascota_id', string='Cita')
    tratamiento_ids = fields.One2many('upopet.tratamiento', 'mascota_id', string='Tratamiento')
    pruebamedica_ids = fields.One2many('upopet.pruebamedica', 'mascota_id', string='Prueba medica')
    persona_id = fields.Many2one('upopet.persona', string='Persona')
