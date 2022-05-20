import os
from flask import Flask, make_response, render_template
from requests import request

script_dir = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, template_folder=f"{script_dir}/templates")


@app.route('/')
def app_rules():
        return make_response(render_template("formulaire.php"))
        #return 'JM rules !\n'
if __name__ == '__main__' :
    app.run(host='0.0.0.0', debug = True)

@app.route('/templates', methods=['POST', 'GET'])
def monChateau():
    if request.method == 'POST':
        nom = request.form['chateau']
    return nom


# # application Flask
# script_dir = os.path.dirname(os.path.abspath(__file__))
# print(script_dir)
# app = Flask(__name__, template_folder=f"{script_dir}/templates")

# @app.route('/')
# def index():
#     # affichage de la page
#     return make_response(render_template("balises.html"))


# #main
# if __name__ == '__main__' :
#     app.config.update(DEBUG=True)
#     app.run()
