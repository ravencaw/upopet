from odoo import models, fields, api

class medicamento(models.Model):
     _name = 'medicamento.upopet'

     cif_lab = fields.Char('CIF Laboratorio', size = 9, required = True)
     nombre = fields.Char('Nombre', size = 8, required = True)
     referencia = fields.Char('Referencia', size = 10, required = True)
     fechaCaducidad = fields.Datetime('Fecha caducidad', required = True, readonly = True, select = True)
     prospecto = fields.Char('Prospecto', size = 10, required = True)

     tratamiento_ids = fields.One2many('tratamiento.upopet', string='Tratamiento')  