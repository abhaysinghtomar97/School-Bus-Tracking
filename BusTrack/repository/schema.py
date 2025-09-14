# contains marshmallow schema models,which should be return as json output on api call

from BusTrack import ma
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from BusTrack.repository.models.User import User
from BusTrack.repository.models.Kid import Kid
from BusTrack.repository.models.Bus import Bus

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
    id = auto_field()
    first_name = auto_field()
    last_name = auto_field()
    phone = auto_field()
    address = auto_field()



from BusTrack.repository.models.UserLogin import UserLogin

class UserLoginSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = UserLogin
        load_instance = True
    id = auto_field()
    email = auto_field()
    phone = auto_field()
    api_token = auto_field()
    user_id = auto_field()


class BasicBusSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'vehicle_number')


class KidProfileSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Kid
        load_instance = True
    id = auto_field()
    name = auto_field()
    section = auto_field()
    photo = auto_field()
    parent = ma.Nested(UserSchema)
    bus = ma.Nested(BasicBusSchema)



class KidsProfileSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Kid
        load_instance = True
    id = auto_field()
    name = auto_field()
    section = auto_field()
    photo = auto_field()


# prop to export
user_schema = UserSchema()
users_schema = UserSchema(many=True)

user_login_schema = UserLoginSchema()

kid_profile_schema = KidProfileSchema()

kids_profile_schema = KidsProfileSchema(many=True)
