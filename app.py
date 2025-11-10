from genericpath import exists
import os
import profile
from flask import Flask, redirect, render_template, request, send_from_directory, url_for
from forms.NewMahasiswa import NewMahasiswa
from werkzeug.utils import secure_filename
app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

app.config["SECRET_KEY"]="SECRET_KEY"
app.config["UPLOAD_FILE"]=UPLOAD_FOLDER
# //berapa mb maks yang di upload
app.config["MAX_CONTENT_LENGTH"]= 1* 1024 * 1024 

list_mahasiswa = []


@app.route("/")
def index():
    return render_template(
        "index.html", title="Home Page", name="Angky Adi Putra", npm="2428250034", list_mahasiswa=list_mahasiswa
    )


@app.route("/add-new-mahasiswa", methods=["GET", "POST"])
def add_new_mahasiswa():
    form = NewMahasiswa()
    if request.method == "POST":
        name = form.name.data
        npm = form.npm.data
        profile_picture = form.profile_picture.data

        file_name = secure_filename(profile_picture.filename)
        save_dir = os.path.join (UPLOAD_FOLDER,"media")
        os.makedirs(save_dir,exist_ok=True)
        profile_picture.save(os.path.join(save_dir, file_name))

        list_mahasiswa.insert(0,{
            "name": name,"npm":npm,"profile_picture": file_name}
        )

        return redirect (url_for("index" ))

    return render_template("add-new-mahasiswa.html", title="Add New Mahasiswa", form=form)

@app.route("/uploads/<path:filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FILE"], filename)
if __name__ == "__main__":
    
    app.run(debug=True, port=5000)