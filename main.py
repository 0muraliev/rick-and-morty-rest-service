from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/api/seasons/')
def seasons():
    return jsonify(
        seasons={
            1: {
                'id': 1,
                'urlImage': 'https://static.wikia.nocookie.net/rickandmorty/images/7/70/Rick_and_Morty_Season_1.jpg/revision/latest?cb=20161125224650',
                'title': 'Season 1'
            },
            2: {
                'id': 2,
                'urlImage': 'https://static.wikia.nocookie.net/rickandmorty/images/d/d5/Season2.jpg/revision/latest?cb=20200718092925',
                'title': 'Season 2'
            },
            3: {
                'id': 3,
                'urlImage': 'https://static.wikia.nocookie.net/rickandmorty/images/b/be/Season3.jpg/revision/latest?cb=20200718093040',
                'title': 'Season 3'
            },
            4: {
                'id': 4,
                'urlImage': 'https://pisces.bbystatic.com/image2/BestBuy_US/images/products/3503/35033712_sa.jpg',
                'title': 'Season 4'
            }
        }
    )


if __name__ == '__main__':
    app.run()
