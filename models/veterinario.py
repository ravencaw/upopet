# -*- coding: utf-8 -*-

from odoo import models, fields, api


class veterinario(models.Model):
    
    _inherit = 'upopet.persona'
    
    _name = 'upopet.veterinario'
    
    
    _rec_name = 'numColegiado'
    numColegiado = fields.Integer('Número de colegiado', required=True)
    especialidad = fields.Char('Especialidad', size=80, required=True)
    nomina = fields.Float('Nómina', digits=(4, 4))
    foto_veterinario = fields.Binary('Foto')

    tratamiento_ids = fields.One2many('upopet.tratamiento', 'veterinario_id', string='Tratamiento')
    cita_ids = fields.One2many('upopet.cita', 'veterinario_id', string='Cita')
    pruebamedica_ids = fields.One2many('upopet.pruebamedica', 'veterinario_id', string='Prueba Médica')
