# -*- coding: utf-8 -*-

from odoo import models, fields, api


class veterinario(models.Model):
    
    _inherit = 'upopet.persona'
    
    _name = 'upopet.veterinario'
    
    _rec_name = 'numColegiado'
    numColegiado = fields.Char('Número de colegiado', size=9, required=True)
    especialidad = fields.Char('Especialidad', size=80, required=True)
    nomina = fields.Float('Nómina', digits=(4, 4))
    foto_veterinario = fields.Binary('Foto')

    tratamiento_ids = fields.One2many('upopet.tratamiento', 'veterinario_id', string='Tratamiento')
    cita_ids = fields.One2many('upopet.cita', 'veterinario_id', string='Cita')
    pruebamedica_ids = fields.One2many('upopet.pruebamedica', 'veterinario_id', string='Prueba Médica')
    
    _sql_constraints = [('veterinario_numColegiado_unique','UNIQUE (numColegiado)','El numero de colegiado debe ser único')]

    #Validación número de colegiado: tiene 9 dígitos
    @api.one 
    @api.constrains('numColegiado')
    def _check_numColegiado(self):
        if len(self.numColegiado) != 9:
            raise models.ValidationError('El número de colegiado debe constar de 9 dígitos')
        
        