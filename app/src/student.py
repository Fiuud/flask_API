from flask import jsonify, abort

from app.controllers import StudentController


def create_student(request):
    if not request or 'email' not in request or 'displayName' not in request or 'googleId' not in request or 'photoUrl' not in request:
        abort(400)

    student = StudentController.get_student(request['email'])
    if not student:
        student = StudentController.create_student(request)

    return jsonify({'email': student.email,
                    'displayName': student.displayName,
                    'googleId': student.googleId,
                    'publicKey': student.publicKey,
                    'photoUrl': request['photoUrl']}), 201
