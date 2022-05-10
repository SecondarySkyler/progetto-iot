def parse_json(measurement, field_name, value):
    json = {
       'measurement' : measurement,
       'fields':  {
           field_name : value
       }
    }
    return json