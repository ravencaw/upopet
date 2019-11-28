# -*- coding: utf-8 -*-

from odoo import models, fields, api

class tratamiento(models.Model):
    _name = 'upopet.tratamiento'

    patologia = fields.Char('Patologia', size = 20, required = True)
    inicio = fields.Datetime('Inicio', required = True, readonly = False, select = True)
    fin = fields.Datetime('Fin', required = False, readonly = False, select = True)
    observaciones = fields.Text()

    cita_id = fields.Many2one('upopet.cita', string='Cita')
    mascota_id = fields.Many2one('upopet.mascota', string='Mascota')
    veterinario_id = fields.Many2one('upopet.veterinario', string='Veterinario')
    medicamento_ids = fields.Many2many('upopet.medicamento', string='Medicamento')