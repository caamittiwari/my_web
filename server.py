"""my website project using flask   """
from flask import Flask , render_template ,request
from dotenv import load_dotenv
import csv 
load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/<pagename>')
def works(pagename):
    return render_template(pagename)


# @app.route('/work.html')
# def work():
#     return render_template("work.html") 
#
# @app.route('/about.html')
# def about():
#     return render_template("about.html") 
def data_in_text(data):
        with open("./data.txt",mode="a+")as df :
            mail = data["email"]
            sub = data["subject"]
            massage = data["message"]
            s_data = f"\n{mail} , {sub},{massage} "
            df.write(s_data)
            

def data_trf_in_csv(data):

    with open("data.csv" ,newline="", mode="r") as cf_r:

        fied_name = ["email" , "subject", "message" ]
        header = True
        cf_reder = csv.reader(cf_r)
        for line in cf_reder:

            if  line.__eq__(fied_name):
                header = False
                break

    with open("data.csv" ,newline="", mode="a") as cf:
        csv_writer =  csv.DictWriter(cf ,fieldnames=fied_name)
        if header :
            csv_writer.writeheader()
        
        csv_writer.writerow(data)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit():
    if request.method == "POST":
        data =request.form.to_dict()
        # data_in_text(data)    
        data_trf_in_csv(data)
        
        return  render_template("thanks.html")
    else:
        return " something went wrong "
