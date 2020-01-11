# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime


class medicamento(models.Model):
     _name = 'upopet.medicamento'

     _rec_name = 'nombre'
     nombre = fields.Char('Nombre', size=8, required=True)
     referencia = fields.Char('Referencia', size=13, required=True)
     precio = fields.Float('Precio', required=True, digits=(4, 3))
     fechaCaducidad = fields.Date('Fecha caducidad', required=True)
     subir_prospecto = fields.Binary(string="Subir prospecto")
     prospecto = fields.Char(string="Prospecto", required=True)
     foto_medicamento = fields.Binary('Foto')

     tratamiento_ids = fields.Many2many('upopet.tratamiento', string='Tratamiento') 
     laboratorio_ids = fields.Many2many('upopet.laboratorio', string='Laboratorio') 
     
     @api.one 
     @api.constrains('referencia')
     def _check_referencia(self):
      if len(self.referencia) != 13:
        raise models.ValidationError('El código de barras debe constar de 13 dígitos')
    
     @api.one 
     @api.constrains('fechaCaducidad')
     def _check_fechaCaducidad(self):       
      ahora = datetime.now()
      if str(ahora) > self.fechaCaducidad:
        raise models.ValidationError('La fecha de caducidad debe ser superior a la fecha actual')
    
    
    
    
    