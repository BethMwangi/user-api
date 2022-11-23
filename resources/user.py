from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from extensions import db
from models.user import UserModel
from schemas.user import UserSchema

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


@blp.route("/user")
class UserList(MethodView):
    @blp.response(200, UserSchema(many=True))
    def get(self):
        return UserModel.query.all()

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

