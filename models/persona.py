# -*- coding: utf-8 -*-
import re

from odoo import models, fields, api


class persona(models.Model):
    _name = 'upopet.persona'

    _rec_name = 'dni'
    dni = fields.Char('Dni', size=9, required=True)
    nombre = fields.Char('Nombre', size=60, required=True)
    apellidos = fields.Char('Apellidos', size=120, required=True)
    direccion = fields.Char('Dirección', size=120, required=True)
    telefono = fields.Integer('Teléfono', size=9, required=True)
    fechNac = fields.Date('Fecha de nacimiento', required=True)
    email = fields.Char('Email', size=120, required=True)

    mascota_ids = fields.One2many('upopet.mascota', 'persona_id', string='Mascota')

    _sql_constraints = [('persona_dni_unique','UNIQUE (dni)','El DNI debe ser único')]

    #Validacion mail: 
    @api.one 
    @api.constrains('email')
    def _check_email(self):
        if len(self.email) < 7:
            raise models.ValidationError('El mail debe constar de al menos 7 caracteres')
        if re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", self.email) == None:
            raise models.ValidationError('El formato del email debe ser example@mail.com')
        
    #Validación teléfono: tiene 9 dígitos
    @api.one 
    @api.constrains('telefono')
    def _check_telefono(self):
        if len(str(self.telefono)) != 9:
            raise models.ValidationError('El número de telefono debe constar de 9 dígitos')
    
    
    