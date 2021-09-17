from flask import Flask, redirect, url_for, request, render_template, send_file
import time
from flask import send_from_directory
import os

app = Flask(__name__)


@app.route('/success/<cname>/<age>/<dataset>')
def success(cname, age, dataset):
    return 'This is {cname}. Age is {age}. Likes to eat {datasets}'\
        .format(cname=cname, age=age, datasets=dataset)

# @app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
# def download(filename):
#     print(app.root_path)
#     full_path = os.path.join(app.root_path, 'uploads')
#     print(full_path)
#     return send_from_directory(full_path, filename)

# @app.route('/download/<path:filename>')
# def download_file(filename):
#     # For windows you need to use drive name [ex: F:/Example.pdf]
#     path = os.path.join(app.root_path, 'uploads/', filename)
#     return send_file(path, as_attachment=True)


@app.route('/', methods=['POST', 'GET'])
def get_specifications():
    # htmlpath = os.path.join(app.root_path, 'templates\\', 'helloWorld.html')
    if request.method == 'POST':
        country = request.form['nam']
        numrows = request.form['age']
        datasets = request.form.getlist('datasetname')
        return redirect(url_for('success', cname=country, age=numrows, dataset=datasets))
        # return redirect(url_for('download_file', filename='Capture15.PNG'))
    else:
        return render_template('helloWorld.html')
        # return redirect(url_for('success', cname=country, rows=numrows, dataset=datasets))


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
