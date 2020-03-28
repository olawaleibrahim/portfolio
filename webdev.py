from flask import Flask, render_template, send_from_directory, request, redirect
import csv

app = Flask(__name__)
print(__name__)


@app.route('/<string:page_name>')
def my_home(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as my_file:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file1 = my_file.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as my_file2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(my_file2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])
        


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong, try again.'


# @app.route('/favicon.ico')
# def favicon():
 #   return send_from_directory(os.path.join(app.root_path, 'static'),
  #  'favicon.ico', mimetype='image/vnd.microsoft.icon')
