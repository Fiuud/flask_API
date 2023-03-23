from application import create_app
from utils.jwt_token import jwt
from utils.turbo import turbo
from extensions.database_extension import init_db

app = create_app()

jwt.init_app(app)
turbo.init_app(app)
init_db(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, )
