from marshmallow import Schema, fields, EXCLUDE, post_load
from marshmallow.exceptions import ValidationError


class UserSchema(Schema):
    class Meta:
        ordered = True

        id = fields.Int(dump_only=True)
        username = fields.Str(required=True)
        email = fields.Str(required=True)
        first_name = fields.Str(required=True)
        last_name = fields.Str()