from wtforms import Form, FloatField, SelectField, BooleanField, validators


class GeometryInput(Form):
    steel_diameter_data = FloatField(label='',
                                     validators=[validators.InputRequired()])
    steel_diameter_unit = SelectField(label='',
                                      choices=[('inch', '[inch]'),
                                               ('mm', '[mm]')])
    corrosion_allowance = FloatField(label='(mm)',
                                     validators=[validators.InputRequired()])


class MaterialInput(Form):
    fabrication_method = SelectField(label='', choices=[('HFW', 'HFW'),
                                                        ('SMLS', 'SMLS'),
                                                        ('MWP', 'MWP')])
    pipe_material = SelectField(label='', choices=[('DNV360', 'DNV360'),
                                                   ('DNV415', 'DNV415'),
                                                   ('DNV450', 'DNV450'),
                                                   ('22Cr', '22Cr'),
                                                   ('25Cr', '25Cr')])
    max_design_temperature = FloatField(label='(°C)',
                                        validators=[validators.InputRequired()])
    supplimentary_d_fulfilled = SelectField(label='', choices=[('yes', 'YES'),
                                                               ('no', 'NO')])
    supplimentary_u_fulfilled = SelectField(label='', choices=[('yes', 'YES'),
                                                               ('no', 'NO')])
    any_inner_metal_layer = SelectField(label='', choices=[('yes', 'YES'),
                                                           ('no', 'NO')])
    cladded_or_lined = SelectField(label='', choices=[('Cladded', 'Cladded'),
                                                      ('Lined', 'Lined')])
    metal_layer_type = SelectField(label='', choices=[('UNS31603', 'UNS31603'),
                                                      ('UNSN06625', 'UNSN06625')])


class LoadInput(Form):
    design_pressure = FloatField(label='[Barg]',
                                 validators=[validators.InputRequired()])
    level = FloatField(label='(m)',
                       validators=[validators.InputRequired()])
    max_contents_density_at_operation = FloatField(label='(kg/m3)',
                                                   validators=[validators.InputRequired()])
    water_depth_for_bursting = FloatField(label='(m)',
                                          validators=[validators.InputRequired()])
    water_depth_for_collapse_and_prop_buckling = FloatField(label='(m)',
                                                            validators=[validators.InputRequired()])
    sea_water_density = FloatField(label='(kg/m3)',
                                   validators=[validators.InputRequired()])


class SafetyClass(Form):
    contents_type = SelectField(label='', choices=[('Non-flammable', 'Non-flammable'),
                                                   ('Flammable', 'Flammable')])
    operation_zone = SelectField(label='', choices=[('Zone2', 'Zone2'),
                                                    ('Zone1', 'Zone1'),
                                                    ('Both', 'Both')])


class CalWith(Form):
    pressure_containment = BooleanField(label='', validators=[validators.DataRequired()])
    collaps = BooleanField(label='', validators=[validators.DataRequired()])
    propgation_buckling = BooleanField(label='', validators=[validators.DataRequired()])
    reeling_screening_check = BooleanField(label='', validators=[validators.DataRequired()])
    vessel_if_reeling_check_is_requried = SelectField(label='', choices=[('7Oceans', '7Oceans'),
                                                                         ('7Navica', '7Navica')])
