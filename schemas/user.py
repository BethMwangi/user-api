from marshmallow import Schema, fields, EXCLUDE, post_load
from marshmallow.exceptions import ValidationError


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str()
    
class UserUpdateSchema(Schema):
    username = fields.Str()
    email = fields.Str()
    first_name = fields.Str()
    last_name = fields.Str()