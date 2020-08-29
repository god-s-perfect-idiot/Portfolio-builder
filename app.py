from flask import Flask, render_template, request, render_template_string, send_from_directory, abort, safe_join
import model
import service
import os

prev=''
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/hud")
def hud():
    return render_template('home.html')

@app.route("/build", methods=['POST'])
def build():
    global prev
    if(request.method == 'POST'):
        Data = request.form.getlist('Data[]')
        project_count = request.form.get("projectCount")
        testi_count = request.form.get("testiCount")
        temp = service.update_pf(Data, project_count, testi_count)
        try:
            os.remove(prev)
        except:
            print("Cleanup failed", prev)
        prev = temp+".zip"
        print(temp+".zip")
        try:
            return send_from_directory("/",filename=temp+".zip", as_attachment=True)
        except FileNotFoundError:
            abort(404)

if(__name__=="__main__"):
    app.run(debug=True)
