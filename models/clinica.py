# -*- coding: utf-8 -*-

from odoo import models, fields, api


class clinica(models.Model):
     _name = 'upopet.clinica'
     
     _rec_name = 'nombre'
     nombre = fields.Char('Nombre', size=70, required=True)
     direccion = fields.Char('Dirección', size=120, required=True)
     cp = fields.Integer('Codigo Postal', size=5, required=True)
     telefono = fields.Integer('Teléfono', size=9, required=True)
     logo_clinica = fields.Binary('Logo')

     pruebamedica_ids = fields.One2many('upopet.pruebamedica', 'clinica_id', string='Prueba Médica')
     cita_ids = fields.One2many('upopet.cita', 'clinica_id', string='Cita')

    #Validación cp: tiene 5 números
    
    #Validación teléfono: tiene 9 números