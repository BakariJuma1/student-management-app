
from controllers import CoreController,CoreControllerOne
from flask import Blueprint
from flask_restful import Api


def controller(name,model):
    bp = Blueprint(name,__name__)
    api = Api(bp)

    api.add_resource(CoreController,'/',resource_class_args =(model,))
    api.add_resource(CoreControllerOne,'/<int:id>',resource_class_args =(model,))
    return bp
    