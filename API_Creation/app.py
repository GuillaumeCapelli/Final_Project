from flask import Flask, request, jsonify, abort
import pymysql
import os
import math

app = Flask(__name__)

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': os.getenv("MySQL_password"),
    'db': 'comment_toxicity',
    'cursorclass': pymysql.cursors.DictCursor
}

# Database connection function
def get_db_connection():
    return pymysql.connect(**db_config)

@app.route('/')
def homepage():
    return '''
    <html>
    <head>
        <title>Comment Toxicity API</title>
        <style>
            body { 
                text-align: center; 
                font-family: Arial, sans-serif;
            }
            .container {
                width: 80%;
                margin: 0 auto;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to the Comment Toxicity API</h1>
            <p>This API allows you to access and filter comments based on toxicity metrics and other criteria from various sources like Big Query, Reddit, and scraped data.</p>

            <h2>Available Endpoints:</h2>
            <ul style="list-style: none;">
                <li><b>/big_query_comments</b>: Fetch comments from Big Query. Can filter by username, likes, comment length, and date.</li>
                <li><b>/reddit_comments</b>: Fetch comments from Reddit. Filters similar to Big Query comments.</li>
                <li><b>/scraped_comments</b>: Fetch scraped comments. Filter options available.</li>
                <li><b>/filtered_train_comments</b>: Fetch comments from training data with specific toxicity metrics.</li>
            </ul>

            <h2>Example Usage:</h2>
            <p>To fetch Big Query comments with a specific username:</p>
            <code>http://localhost:5000/big_query_comments?username=johndoe</code>
            
            <p>To fetch Big Query comments with a specific username:</p>
            <code>http://localhost:5000/big_query_comments?username=johndoe</code>

            <p>To fetch Reddit comments with a comment length greater than 100:</p>
            <code>http://localhost:5000/reddit_comments?min_length=100</code>

            <p>To fetch comments from scraped data with likes greater than or equal to 50:</p>
            <code>http://localhost:5000/scraped_comments?min_like=50</code>

            <p>To fetch training comments marked as toxic and severe_toxic:</p>
            <code>http://localhost:5000/filtered_train_comments?toxic=1&severe_toxic=1</code>

            <p>To fetch Big Query comments within a specific date range:</p>
            <code>http://localhost:5000/big_query_comments?start_date=2021-01-01&end_date=2021-12-31</code>

            <h2>Filtering Tips:</h2>
            <ul style="list-style: none;">
                <li>Combine multiple query parameters to refine your search.</li>
                <li>Use the date format YYYY-MM-DD for date-related queries.</li>
                <li>Queries are case-sensitive, especially for usernames.</li>
            </ul>
        </div>
    </body>
    </html>
    '''



@app.route('/big_query_comments', methods=['GET'])
def get_big_query_comments():
    username = request.args.get('username')
    min_like = request.args.get('min_like', type=int)
    max_like = request.args.get('max_like', type=int)
    min_length = request.args.get('min_length', type=int)
    max_length = request.args.get('max_length', type=int)
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    query = "SELECT username, comment, date, `like`, comment_length FROM big_query_comment WHERE 1=1 "
    params = []

    if username:
        query += "AND username = %s "
        params.append(username)

    if min_like is not None:
        query += "AND `like` >= %s "
        params.append(min_like)

    if max_like is not None:
        query += "AND `like` <= %s "
        params.append(max_like)

    if min_length is not None:
        query += "AND comment_length >= %s "
        params.append(min_length)

    if max_length is not None:
        query += "AND comment_length <= %s "
        params.append(max_length)

    if start_date:
        query += "AND date >= %s "
        params.append(start_date)

    if end_date:
        query += "AND date <= %s "
        params.append(end_date)

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, tuple(params))
    comments = cursor.fetchall()
    conn.close()

    return jsonify(comments)


@app.route('/reddit_comments', methods=['GET'])
def get_reddit_comments():
    username = request.args.get('username')
    min_like = request.args.get('min_like', type=int)
    max_like = request.args.get('max_like', type=int)
    min_length = request.args.get('min_length', type=int)
    max_length = request.args.get('max_length', type=int)
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    query = "SELECT username, comment, date, `like`, comment_length FROM reddit_comment WHERE 1=1 "
    params = []

    if username:
        query += "AND username = %s "
        params.append(username)

    if min_like is not None:
        query += "AND `like` >= %s "
        params.append(min_like)

    if max_like is not None:
        query += "AND `like` <= %s "
        params.append(max_like)

    if min_length is not None:
        query += "AND comment_length >= %s "
        params.append(min_length)

    if max_length is not None:
        query += "AND comment_length <= %s "
        params.append(max_length)

    if start_date:
        query += "AND date >= %s "
        params.append(start_date)

    if end_date:
        query += "AND date <= %s "
        params.append(end_date)

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, tuple(params))
    comments = cursor.fetchall()
    conn.close()

    return jsonify(comments)



@app.route('/scrapped_comments', methods=['GET'])
def get_scrapped_comments():
    username = request.args.get('username')
    min_like = request.args.get('min_like', type=int)
    max_like = request.args.get('max_like', type=int)
    min_length = request.args.get('min_length', type=int)
    max_length = request.args.get('max_length', type=int)
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    query = "SELECT username, comment, date, `like`, comment_length FROM scrapped_comment WHERE 1=1 "
    params = []

    if username:
        query += "AND username = %s "
        params.append(username)

    if min_like is not None:
        query += "AND `like` >= %s "
        params.append(min_like)

    if max_like is not None:
        query += "AND `like` <= %s "
        params.append(max_like)

    if min_length is not None:
        query += "AND comment_length >= %s "
        params.append(min_length)

    if max_length is not None:
        query += "AND comment_length <= %s "
        params.append(max_length)

    if start_date:
        query += "AND date >= %s "
        params.append(start_date)

    if end_date:
        query += "AND date <= %s "
        params.append(end_date)

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, tuple(params))
    comments = cursor.fetchall()
    conn.close()

    return jsonify(comments)



@app.route('/filtered_train_comments', methods=['GET'])
def get_filtered_train_comments():
    toxic = request.args.get('toxic', type=int)
    severe_toxic = request.args.get('severe_toxic', type=int)
    obscene = request.args.get('obscene', type=int)
    threat = request.args.get('threat', type=int)
    insult = request.args.get('insult', type=int)
    identity_hate = request.args.get('identity_hate', type=int)

    query = "SELECT id, comment FROM train_comments WHERE 1=1 "
    params = []

    if toxic is not None:
        query += "AND toxic = %s "
        params.append(toxic)

    if severe_toxic is not None:
        query += "AND severe_toxic = %s "
        params.append(severe_toxic)

    if obscene is not None:
        query += "AND obscene = %s "
        params.append(obscene)

    if threat is not None:
        query += "AND threat = %s "
        params.append(threat)

    if insult is not None:
        query += "AND insult = %s "
        params.append(insult)

    if identity_hate is not None:
        query += "AND identity_hate = %s "
        params.append(identity_hate)

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, tuple(params))
    comments = cursor.fetchall()
    conn.close()

    return jsonify(comments)



#if __name__ == '__main__':
#    app.run(debug=True, port=5000)
