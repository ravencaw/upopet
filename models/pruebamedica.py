# -*- coding: utf-8 -*-

from odoo import models, fields, api

class pruebamedica(models.Model):
    _name = 'upopet.pruebamedica'

    fechaHora = fields.Datetime('Fecha y Hora', required = True)
    tipo = fields.Char('Tipo', size=20, required= True)
    observaciones = fields.Text('Observaciones')

    veterinario_id = fields.Many2one('upopet.veterinario', 'pruebamedica_id', string='Veterinario')
    mascota_id = fields.Many2one('upopet.mascota', string='Mascota')
    clinica_id = fields.Many2one('upopet.clinica', string='Clinica')
