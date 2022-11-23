from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy import func

from extensions import db
from utils import CursorPage
from models.user import UserModel
from schemas.user import UserSchema, UserUpdateSchema, UserQueryArgsSchema

blp = Blueprint("users", __name__, description="Operations on users")

@blp.route("/user/<int:id>")
class User(MethodView):
    @blp.response(200, UserSchema)
    def get(self, id):
        user = UserModel.query.get_or_404(id)
        return user

    def delete(self, id):
        user = UserModel.query.get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted"}, 200

    @blp.arguments(UserUpdateSchema)
    @blp.response(200, UserSchema)
    def put(self, user_data, id):
        user = UserModel.query.get(id)

        if user:
            user.username = user_data["username"]
            user.email = user_data["email"]
            user.first_name = user_data["first_name"]
            user.last_name = user_data["last_name"]
        else:
            user = UserModel(id=id, **user_data)

        db.session.add(user)
        db.session.commit()

        return user


@blp.route("/users")
class UserList(MethodView):
    @blp.arguments(UserQueryArgsSchema, location="query")
    @blp.response(200, UserSchema(many=True))
    @blp.paginate(CursorPage) 
    def get(self, args):
        if not args:
            users = UserModel.query.order_by(UserModel.id)
            return users

        username = args.pop('username', None)
        users = UserModel.query.filter(UserModel.username == username)
        if username is not None:
            return users

        first_name = args.pop('first_name', None)
        users = UserModel.query.filter(func.lower(UserModel.first_name) == func.lower(first_name))
        if first_name is not None:
            return users

        last_name = args.pop('last_name', None)
        users = UserModel.query.filter(func.lower(UserModel.last_name) == func.lower(last_name))
        if last_name is not None:
            return users

    @blp.arguments(UserSchema)
    @blp.response(200, UserSchema)
    def post(self, user_data):
        user = UserModel(**user_data)

        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            abort(400, message="A user with that name already Exists")
        except SQLAlchemyError:
            abort(500, "An error occurred")
        return user

