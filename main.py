from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/api/test_video')
def test():
    return jsonify(
        url='https://docs.google.com/file/d/0B4BsAbG4atWHQzVfLUU3UnhhZTA/edit?resourcekey=0-LSbA63dXOK1G-76LJT4SLw'
    )


if __name__ == '__main__':
    app.run()
