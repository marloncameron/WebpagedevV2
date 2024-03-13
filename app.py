from flask import Flask, render_template 

app = Flask(__name__)

JOB = [
  {
    'id': 1,
    'title': 'Conuntry 1',
    'Technician 1': 'Name 1',
    'Technician 2': 'Name 2',
    'Technician 3': 'Name 3',
    'Technician 4': 'Name 4',
    
  },
  {
    'id': 2,
    'title': 'Conuntry 2',
    'Technician 1': 'Name 1',
    'Technician 2': 'Name 2',
    'Technician 3': 'Name 3',
    'Technician 4': 'Name 4',

  },
  {    
    'id': 3,
    'title': 'Conuntry 3',
    'Technician 1': 'Name 1',
    'Technician 2': 'Name 2',
    'Technician 3': 'Name 3',
    'Technician 4': 'Name 4',
    
  },
  {
    'id': 4,
    'title': 'Conuntry 4',
    'Technician 1': 'Name 1',
    'Technician 2': 'Name 2',
    'Technician 3': 'Name 3',
    'Technician 4': 'Name 4',
    
  }
]



@app.route("/")
def ITWEBsa():
    return render_template('home.html', jobs=JOB)



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
  

