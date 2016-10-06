# -*- coding: utf-8 -*-

from datetime import timedelta

from openerp import api, exceptions, fields, models, _

#
# CLASE CURSO
#
class Curso(models.Model):
  _name = 'ie.curso'  #  Model odoo name

  name = fields.Char(string='Titulo', required=True, help="Ingrese el nombre")   
  codigo = fields.Char(required=True)
  tipo = fields.Char()
  inicio = fields.Date(string='Fecha de inicio', default=fields.Date.today)
  fin = fields.Date(string='Fecha de fin', default=fields.Date.today)
  baja = fields.Boolean(default=True)

  #campos relacionales
  inscripcion_ids = fields.One2many('ie.inscripcion', 'curso_id', string="Inscripciones")
  cuotas_ids = fields.One2many('ie.cuota', 'curso_id', string="Cuotas")
  sede_id = fields.Many2one('ie.sede', ondelete='cascade', string="Sede", required=True)



#
# CLASE ALUMNO
#
class Alumno(models.Model):
  _name = 'ie.alumno'
  _rec_name = 'apellido'
  
  dni = fields.Integer(string="D.NI.", required=True)
  nombre = fields.Char(string='Nombre', required=True)
  apellido = fields.Char(string='Apellido', required=True)
  domicilio = fields.Char()
  telefono = fields.Char()
  email = fields.Char(string='E-mail', required=True)
  fecha = fields.Date(string='Fecha de nacimiento', default=fields.Date.today)
  baja = fields.Boolean(default=False)
  
  #campos relacionales
  inscripcion_ids = fields.One2many('ie.inscripcion', 'alumno_id', string="Inscripciones")
  ciudad_id = fields.Many2one('ie.ciudad', ondelete='cascade', string="Ciudad", required=True)
  sede_id = fields.Many2one('ie.sede', ondelete='cascade', string="Sede", required=True)

  _sql_constraints = [
  # que no se pueda repetir el dni
      ('dni_unique',
       'UNIQUE(dni)',
       "El DNI ingresado ya existe"),
  # que no se pueda repetir el email
      ('email_unique',
       'UNIQUE(email)',
       "Ya existe un alumno con ese email"
      ),
  ]


  # sobreescribir el metodo para que muestre nombre y apellido
  def name_get(self, cr, uid, ids, context=None):
      res = []    
      for alumno in self.browse(cr, uid, ids, context):
          res.append((alumno.id, alumno.apellido + ', ' + alumno.nombre))
      return res


  # que el dni no sea un numero negativo 
  @api.onchange('dni')
  def _verify_valid_dni(self):
      if self.dni < 0:
          return {
              'warning': {
                  'title': "Valor incorrecto",
                  'message': "El número de DNI no puede ser negativo",
              },
          }


#
# CLASE CUOTA
#
class Cuota(models.Model):
  _name = 'ie.cuota'

  name = fields.Char(string='Modulo', required=True)
  monto = fields.Integer(required=True)
  baja = fields.Boolean(default=True)

  #campos relacionales
  curso_id = fields.Many2one('ie.curso', ondelete='cascade', string="Curso", required=True)



#
# CLASE RECURSO
#
class Recurso(models.Model):
  _name = 'ie.recurso'

  name = fields.Char(string='Filename', required=True)
  descripcion = fields.Char(required=True)

  #campos relacionales
  cuota_id = fields.Many2one('ie.cuota', ondelete='cascade', string="Cuota", required=True)



#
# CLASE INSCRIPCION
#
class Inscripcion(models.Model):
  _name = 'ie.inscripcion'

  legajo = fields.Char(compute='_compute_legajo')
  fecha = fields.Date(default=fields.Date.today)
  baja = fields.Boolean(default=True)
  modalidad = fields.Selection([
   ('1', "Presencial"),
   ('2', "Semipresencial"),
   ('3', "Distancia"),
   ], default='1')

  #campos relacionales
  curso_id = fields.Many2one('ie.curso', ondelete='cascade', string="Curso", required=True)
  alumno_id = fields.Many2one('ie.alumno', ondelete='cascade', string="Alumno", required=True)
  sede_id = fields.Many2one('ie.sede', ondelete='cascade', string="Sede", required=True)
  observacion_ids = fields.One2many('ie.observacion', 'inscripcion_id', string="Observaciones")


  @api.one
  @api.depends('curso_id.name')
  def _compute_legajo(self):
    self.legajo=self.curso_id.name


#
# CLASE OBSERVACION
#
class Observacion(models.Model):
  _name = 'ie.observacion'

  name = fields.Char(string='Descripción', required=True)
  fecha = fields.Date(default=fields.Date.today, readonly=True)
  baja = fields.Boolean(default=True)

  #campos relacionales
  inscripcion_id = fields.Many2one('ie.inscripcion', ondelete='cascade', string="Inscripcion", required=True)



#
# CLASE PAGO
#
class Pago(models.Model):
  _name = 'ie.pago'

  fecha = fields.Date(default=fields.Date.today)
  estado = fields.Char()
  baja = fields.Boolean(default=True)

  #campos relacionales
  sede_id = fields.Many2one('ie.sede', ondelete='cascade', string="Sede", required=True)
  alumno_id = fields.Many2one('ie.alumno', ondelete='cascade', string="Alumno", required=True)
  cuota_id = fields.Many2one('ie.cuota', ondelete='cascade', string="Cuota", required=True)


#
# CLASE PROVINCIA
#
class Provincia(models.Model):
  _name = 'ie.provincia'  #  Model odoo name

  name = fields.Char(string='Nombre', required=True)
  baja = fields.Boolean(default=True)

  #campos relacionales
  ciudad_ids = fields.One2many('ie.ciudad', 'provincia_id', string="Ciudades")



#
# CLASE CIUDAD
#
class Ciudad(models.Model):
  _name = 'ie.ciudad'

  name = fields.Char(string='Nombre', required=True)
  baja = fields.Boolean(default=True)

  #campos relacionales
  provincia_id = fields.Many2one('ie.provincia', ondelete='cascade', string="Provincia", required=True)
  sede_ids = fields.One2many('ie.sede', 'ciudad_id', string="Sedes")



#
# CLASE SEDE
#
class Sede(models.Model):
  _name = 'ie.sede'

  name = fields.Char(string='Nombre', required=True)
  domicilio = fields.Char()
  telefono = fields.Char()
  email = fields.Char(string='E-mail', required=True)
  ciudad_id = fields.Many2one('ie.ciudad', ondelete='cascade', string="Ciudad", required=True)
  baja = fields.Boolean(default=True)

  #campos relacionales
  ciudad_id = fields.Many2one('ie.ciudad', ondelete='cascade', string="Ciudad", required=True)



#
# CLASE NOTICIA
#
class Noticia(models.Model):
  _name = 'ie.noticia'

  name = fields.Char(string='Título', required=True)
  descripcion = fields.Char(required=True)
  baja = fields.Boolean(default=True)