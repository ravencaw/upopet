# -*- coding: utf-8 -*-

from odoo import models, fields, api

class pruebamedica(models.Model):
    _name = 'upopet.pruebamedica'

    id = fields.Integer('ID', size=9, required= True)
    fechaHora = fields.Datetime('Fecha y Hora', required = True)
    tipo = fields.Char('Tipo', size=20, required= True)
    observaciones = fields.Text('Observaciones')

    veterinario_ids = fields.Many2one('upopet.veterinario', string='Veterinario')
    mascota_ids = fields.Many2one('upopet.mascota', string='Mascota')
    clinica_ids = fields.Many2one('upopet.clinica', string='Clinica')
