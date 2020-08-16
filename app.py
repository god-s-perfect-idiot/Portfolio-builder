from flask import Flask, render_template, request, render_template_string
import model
import service

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/hud")
def hud():
    return render_template('home.html')

@app.route("/build", methods=['POST'])
def build():
    if(request.method == 'POST'):
        Data = request.form.getlist('Data[]')
        project_count = request.form.get("projectCount")
        testi_count = request.form.get("testiCount")
        pf = service.update_pf(Data, project_count, testi_count)
        return render_template_string(pf)

if(__name__=="__main__"):
    app.run(debug=True)
