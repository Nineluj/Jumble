from flask import render_template, redirect, url_for, flash, request
from flask_restplus import fields, Api, Resource
import marshmallow
from app.api import bp
from app.api import api

task_model = api.model('Task',
    {
        'id'   : fields.Integer,
        'task' : fields.String
    }
)

@api.route('/task')
class Task(Resource):
    def get(self):
        return {
            'id' : 0,
            'task' : 'This is a task.'
        }

@bp.route('/test', methods=['GET', 'POST'])
def test():
    return "Test"