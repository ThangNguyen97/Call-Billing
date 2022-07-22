from flask import jsonify


def handle_error(message, code):
    response = jsonify({
        'message': message,
    })
    response.status_code = code
    return response


def handle_success(message, code):
    response = jsonify({
        'message': message,
    })
    response.status_code = code
    return response
