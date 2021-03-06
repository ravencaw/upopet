# -*- coding: utf-8 -*-

from odoo import models, fields, api


class mascota(models.Model):
    _name = 'upopet.mascota'

    _rec_name = 'mascotaID'
    mascotaID = fields.Integer('ID mascota', compute='compute_mascota_log', store=False)
    
    numChip = fields.Char('Número de chip', required=True)
    nombre = fields.Char('Nombre', size=15, required=True)
    especie = fields.Char('Especie', size=20, required=True)
    raza = fields.Char('Raza', size=20, required=True)
    edad = fields.Float('Edad')
    color = fields.Char('Color', size=20)
    peso = fields.Float('Peso', required=True, digits=(4, 4))
    tam = fields.Float('Tamaño', required=True, digits=(1, 2))
    sexo = fields.Selection([('m', 'Macho'),
                                     ('h', 'Hembra'), ],
                                     'Sexo')
    foto_mascota = fields.Binary('Foto')

    cita_ids = fields.One2many('upopet.cita', 'mascota_id', string='Cita')
    tratamiento_ids = fields.One2many('upopet.tratamiento', 'mascota_id', string='Tratamiento')
    pruebamedica_ids = fields.One2many('upopet.pruebamedica', 'mascota_id', string='Prueba Médica')
    persona_id = fields.Many2one('upopet.persona', string='Persona')
    
    
    #Validación edad: No puede ser negativa
    @api.constrains('edad')
    def _check_edad(self):       
        if (self.edad <= 0):
            raise models.ValidationError('La edad no puede ser negativa')
    
    @api.onchange('numChip')
    def onchange_numChip(self):
        if (self.persona_id != False and self.nombre != False):
            chip = self.persona_id.dni
            id = self.nombre
            chip = str(chip) + "-" + str(id)
            self.numChip = chip
            #raise models.ValidationError(chip)

    
    
    @api.one
    def compute_mascota_log(self):
      self.mascotaID = self.id
    
    