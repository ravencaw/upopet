# -*- coding: utf-8 -*-
import re
from re import findall

from odoo import models, fields, api


class persona(models.Model):
    _name = 'upopet.persona'

    _rec_name = 'dni'
    dni = fields.Char('Dni', size=9, required=True)
    nombre = fields.Char('Nombre', size=60, required=True)
    apellidos = fields.Char('Apellidos', size=120, required=True)
    direccion = fields.Char('Dirección', size=120, required=True)
    telefono = fields.Char('Teléfono', size=9, required=True)
    fechNac = fields.Date('Fecha de nacimiento', required=True)
    email = fields.Char('Email', size=120, required=True)

    mascota_ids = fields.One2many('upopet.mascota', 'persona_id', string='Mascota')


    #Validacion dni: tiene 8 letras y 1 letra al final
    @api.one 
    @api.constrains('email')
    def _check_email(self):
        if len(self.email) < 7:
            raise models.ValidationError('El mail debe constar de al menos 7 caracteres')
        if re.match("^.+@([?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", self.email) != None:
            raise models.ValidationError('El formato del email debe ser example@mail.com')
    #Validacion telefono: tiene 9 digitos
    @api.one 
    @api.constrains('telefono')
    def _check_telefono(self):
        if len(self.telefono) != 9:
            raise models.ValidationError('El número de telefono debe constar de 9 dígitos')
        if self.telefono.isdigit() == False:
            raise models.ValidationError('El número de telefono debe constar SOLO de dígitos')
    
    
    