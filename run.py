from flask import Flask, render_template, request
import sqlite3
app = Flask(__name__)
@app.route("/")
def run():
	conn = sqlite3.connect('wanggun.db')
	conn.row_factory=sqlite3.Row
	c = conn.cursor()
	c.execute('SELECT * FROM general')
	rows = c.fetchall(); 
	return render_template("index.html",rows = rows)
@app.route('/modi')
def modi():
   id = request.args.get("id") 
   
   conn = sqlite3.connect('wanggun.db')
   conn.row_factory=sqlite3.Row
   c = conn.cursor()
   c.execute('SELECT * FROM general where id='+str(id))
   rows = c.fetchall(); 
   
   return render_template('modi.html',rows = rows)
@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         war = request.form['war']
         id = request.form['id']
         
         with sqlite3.connect("wanggun.db") as con:
            cur = con.cursor()
            
            cur.execute("update general set war="+str(war)+" where id="+str(id))
            
            con.commit()
            msg = "정상적으로 입력되었습니다."
      except:
         con.rollback()
         msg = "입력과정에서 에러가 발생했습니다."
      
      finally:
         return render_template("result.html",msg = msg)
         con.close()
app.run(host='0.0.0.0', port=8787, debug=True) 