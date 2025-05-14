from flask import Flask, render_template, request
import pymysql


def sql_connector():
    conn = pymysql.connect(user='root', password='root', db='inventory_management_system', host='127.0.0.1')
    c = conn.cursor()
    return conn, c


app = Flask(__name__)
          
        
@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        batsman = request.form.get('batsman')
        runs = request.form.get('runs')
        conn, c = sql_connector()
        c.execute("INSERT INTO batsman VALUES ('{}', {})".format(batsman, int(runs)))
        conn.commit()
        conn.close()
        c.close()
    return render_template('index.html')


@app.route('/sales', methods=['GET', 'POST'])
def sales():
    if request.method == 'POST':
        product_id = request.form.get('product_id')
        sale_date = request.form.get('sale_date')
        quantity = request.form.get('quantity_sold')  # Match the form name
        unit_price_total = request.form.get('sale_price_unit') # Match the form name
        customer_id = request.form.get('customer_id')
        conn, c = sql_connector()
        c.execute("INSERT INTO sales VALUES ('{}', '{}', {}, {}, {})".format(product_id, sale_date, int(quantity), int(unit_price_total), int(customer_id)))
        conn.commit()
        conn.close()
        c.close()
    return render_template('sales_entry.html')

if __name__ == '__main__':
    app.run(debug=True)
    
    
    
# pymysql, mysql-connector, mysql-connector-python
