SQLALCHEMY_DATABASE_URI = 'sqlite:///detabase.db'

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = "1234"


SECRET_KEY = 'asdfghjklpoiuytrewqzxcvbnmzvxbnmadsfdgfhjkwtyui'

PAYMENT_MERCHANT= 'sandbox'
PAYMENT_CALLBACK= 'http://localhost:5000/verify'
PAYMENT_VARIFY_REQUEST_URL= 'https://sandbox.shepa.com/api/v1/verify'