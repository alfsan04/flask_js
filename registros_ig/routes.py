from registros_ig import app
from registros_ig.models import select_all

@app.route("/")
def index():
    registros = select_all()
    return registros