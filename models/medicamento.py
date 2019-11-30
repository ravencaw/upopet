# -*- coding: utf-8 -*-

from odoo import models, fields, api


class medicamento(models.Model):
     _name = 'upopet.medicamento'

     nombre = fields.Char('Nombre', size = 8, required = True)
     referencia = fields.Char('Referencia', size = 10, required = True)
     fechaCaducidad = fields.Date('Fecha caducidad', required = True)
     prospecto = fields.Text('Prospecto', required = True)
     foto_medicamento = fields.Binary('Foto')

     tratamiento_ids = fields.Many2many('upopet.tratamiento', string='Tratamiento') 
     laboratorio_ids = fields.Many2many('upopet.laboratorio', string='Laboratorio') 

     
