# -*- coding: utf-8 -*-

from odoo import models, fields, api

class veterinario(models.Model):
    
    _inherit = 'upopet.persona'
    
    _name = 'upopet.veterinario'

    numColegiado = fields.Integer('Numero de colegiado', required = True)
    especialidad = fields.Char('Especialidad', size = 80, required = True)
    nomina = fields.Float('Nomina', digits=(4,4))
    foto_veterinario = fields.Binary('Foto')

    tratamiento_ids = fields.One2many('upopet.tratamiento', string='Tratamiento')
    cita_ids = fields.One2many('upopet.cita', string='Cita')
    pruebamedica_ids = fields.One2many('upopet.preubamedica', string='Prueba medica')