from flask import Flask, render_template, request
import util
import psycopg2

app = Flask(__name__)

# Configuration variables for database connection
username = 'postgres'
password = 'Undertale-135'
host = '127.0.0.1'
port = '5432'
database = 'dvdrental'

# route is used to map a URL with a Python function
# complete address: ip:port/
# 127.0.0.1:5000/
@app.route('/')
# this is how you define a function in Python
def index():
    # this is your index page
    # connect to DB
    cursor, connection = util.connect_to_db(username,password,host,port,database)
    # execute SQL commands
    record = util.run_and_fetch_sql(cursor, "SELECT * from customer;")
    if record == -1:
        # you can replace this part with a 404 page
        print('Something is wrong with the SQL command')
    else:
        # this will return all column names of the select result table
        # ['customer_id','store_id','first_name','last_name','email','address_id','activebool','create_date','last_update','active']
        col_names = [desc[0] for desc in cursor.description]
        # only use the first five rows
        log = record[:5]
        # log=[[1,2],[3,4]]
    # disconnect from database
    util.disconnect_from_db(connection,cursor)
    # using render_template function, Flask will search
    # the file named index.html under templates folder
    return render_template('index.html', sql_table = log, table_title=col_names)

# New route to insert a new row into basket_a
@app.route('/api/update_basket_a', methods=['GET'])
def update_basket_a():
    # Connect to the PostgreSQL database
    cursor, connection = util.connect_to_db(username, password, host, port, database)
    
    # Insert a new row into basket_a
    try:
        cursor.execute("INSERT INTO basket_a (a, fruit_a) VALUES (5, 'Cherry');")
        connection.commit()
        return "Success!"
    except psycopg2.Error as e:
        return f"Error: {e}"
    finally:
        # Disconnect from the database
        util.disconnect_from_db(connection, cursor)

# New route to display unique fruits in basket_a and basket_b
@app.route('/api/unique', methods=['GET'])
def unique_fruits():
    # Connect to the PostgreSQL database
    cursor, connection = util.connect_to_db(username, password, host, port, database)
    
    # Fetch unique fruits from basket_a and basket_b
    try:
        cursor.execute("SELECT DISTINCT fruit_a FROM basket_a;")
        basket_a_fruits = [row[0] for row in cursor.fetchall()]

        cursor.execute("SELECT DISTINCT fruit_b FROM basket_b;")
        basket_b_fruits = [row[0] for row in cursor.fetchall()]

        return render_template('unique.html', basket_a_fruits=basket_a_fruits, basket_b_fruits=basket_b_fruits)
    except psycopg2.Error as e:
        return f"Error: {e}"
    finally:
        # Disconnect from the database
        util.disconnect_from_db(connection, cursor)

if __name__ == '__main__':
    app.debug = True
    ip = '127.0.0.1'
    app.run(host=ip)
