from flask import Flask, render_template, jsonify
from cassandra.cluster import Cluster

app = Flask(__name__)

# Connect to Cassandra
cluster = Cluster(['localhost'])  # Change this to your Cassandra cluster address if different
session = cluster.connect('telecom_data')  # Change 'telecom_data' to your keyspace name


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data')
def get_data():
    # Query data from Cassandra
    rows = session.execute(
        "SELECT state, churn FROM customer_churn")  # Ensure 'customer_churn' is your table name

    # Convert rows to a list of dictionaries
    data = [{"state": row.state,"churn": row.churn} for row in rows]

    return jsonify(data)


if __name__ == "__main__":
    # Run the Flask app
    app.run(debug=True)

    # Print the URL where the server is running
    print("Flask server running at:", "http://127.0.0.1:5000/")
