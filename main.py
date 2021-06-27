from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/api/seasons/')
def seasons():
    all_seasons = {
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
    return jsonify(seasons=all_seasons)


@app.route('/api/seasons/<int:id>/')
def season(id):
    season_1 = {
                   1: {
                       'id': 1,
                       'title': 'Episode 1',
                       'urlImage': 'https://m.media-amazon.com/images/M/MV5BNzlhNGI0MTUtOWZlNS00ZmQ2LTk2NTYtMGMwMzRmOGViZWIyXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_FMjpg_UX1280_.jpg',
                   },
                   2: {
                       'id': 3,
                       'title': 'Episode 3',
                       'urlImage': 'https://m.media-amazon.com/images/M/MV5BM2I0Nzg0YTktYTc2Zi00NTk4LWI5ZDQtMmVhYjBjZmRmNGM0XkEyXkFqcGdeQXVyNjg4ODczODM@._V1_FMjpg_UX1000_.jpg'
                   }
               },
    season_2 = {
                   1: {
                       'id': 3,
                       'title': 'Episode 3',
                       'urlImage': 'https://m.media-amazon.com/images/M/MV5BOTExYzYxODYtOGRiMi00MzBmLTkwNzMtY2Q5ZDU2ZjdmOGZmXkEyXkFqcGdeQXVyNTkyMjE3NDU@._V1_FMjpg_UX1000_.jpg',
                   },
                   2: {
                       'id': 10,
                       'title': 'Episode 10',
                       'urlImage': 'https://m.media-amazon.com/images/M/MV5BNmVjM2IzOTQtNzZmNi00MzFjLTg3MGUtYTIwNzk3MDBhMWEwXkEyXkFqcGdeQXVyNTkyMjE3NDU@._V1_FMjpg_UX1000_.jpg'
                   }
               },
    season_3 = {
                   1: {
                       'id': 1,
                       'title': 'Episode 1',
                       'urlImage': 'https://m.media-amazon.com/images/M/MV5BMTRmYzZmZjAtOTBlMy00ODJiLTgwMzEtMTVjN2Y2NzBjYzU3XkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_FMjpg_UX1000_.jpg',
                   },
                   2: {
                       'id': 3,
                       'title': 'Episode 3',
                       'urlImage': 'https://m.media-amazon.com/images/M/MV5BYWM5N2ZlMDEtNmFjZS00NDE3LWI1OWQtMGUxMzBhNzFhMTMzXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_FMjpg_UX1000_.jpg',
                   }
               },
    season_4 = {
                   1: {
                       'id': 3,
                       'title': 'Episode 3',
                       'urlImage': 'https://m.media-amazon.com/images/M/MV5BNTU3NjEwODQtY2JmMC00ZDUzLTkyMzgtODIwMDc0YzdhYzM2XkEyXkFqcGdeQXVyNjgzNDU2ODI@._V1_FMjpg_UX1000_.jpg',
                   },
                   2: {
                       'id': 5,
                       'title': 'Episode 5',
                       'urlImage': 'https://m.media-amazon.com/images/M/MV5BZGM2MjFlZTAtYzEzMy00ZTc3LTliNzAtMWQ1ODBiYTVlZTZhXkEyXkFqcGdeQXVyMzQ0MTAyNjY@._V1_FMjpg_UX1000_.jpg',
                   }
               },

    if id == 1:
        return jsonify(episodes=season_1)
    elif id == 2:
        return jsonify(episodes=season_2)
    elif id == 3:
        return jsonify(episodes=season_3)
    elif id == 4:
        return jsonify(episodes=season_4)


@app.route('/api/seasons/<int:season_id>/episode/<int:episode_id>/')
def episode(season_id, episode_id):
    if season_id == 1:
        if episode_id == 1:
            return jsonify({
                'id': episode_id,
                'videoUrl': 'https://drive.google.com/file/d/1j0KLej8InlHAEd5lKaRdIRmR-Dg2Z8_N/view?usp=sharing',
                'videoPreviewImage': 'https://m.media-amazon.com/images/M/MV5BNzlhNGI0MTUtOWZlNS00ZmQ2LTk2NTYtMGMwMzRmOGViZWIyXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_FMjpg_UX1280_.jpg',
                'title': 'Pilot',
                'description': 'A strangely eccentric genius scientist and inventor, moves into the home of his daughter and her family and begins to strongly influence his young grandson.'
            })
        elif episode_id == 3:
            return jsonify({
                'id': episode_id,
                'videoUrl': 'https://drive.google.com/file/d/1nRQC8peCupj-7apqnTiy_7RWwB6rf1Y6/view?usp=sharing',
                'videoPreviewImage': 'https://m.media-amazon.com/images/M/MV5BM2I0Nzg0YTktYTc2Zi00NTk4LWI5ZDQtMmVhYjBjZmRmNGM0XkEyXkFqcGdeQXVyNjg4ODczODM@._V1_FMjpg_UX1000_.jpg',
                'title': 'Anatomy Park',
                'description': "It's Christmas. Rick shrinks Morty, injecting him into a homeless man to save Anatomy Park. Jerry tries to have a Christmas free of electronic devices, but regrets his decision when his parents introduce him to their new friend."
            })
    elif season_id == 2:
        if episode_id == 3:
            return jsonify({
                'id': episode_id,
                'videoUrl': 'https://drive.google.com/file/d/1kGw2VVfmdLzUP8WaZPDOYcWm7hEmBlAP/view?usp=sharing',
                'videoPreviewImage': 'https://m.media-amazon.com/images/M/MV5BOTExYzYxODYtOGRiMi00MzBmLTkwNzMtY2Q5ZDU2ZjdmOGZmXkEyXkFqcGdeQXVyNTkyMjE3NDU@._V1_FMjpg_UX1000_.jpg',
                'title': 'Auto Erotic Assimilation',
                'description': 'Rick gets emotional. Beth and Jerry get into a fight.'
            })
        elif episode_id == 10:
            return jsonify({
                'id': episode_id,
                'videoUrl': 'https://drive.google.com/file/d/1J18Qhh6A53n7hwXaovcPhp5Z5TXB0jPJ/view?usp=sharing',
                'videoPreviewImage': 'https://m.media-amazon.com/images/M/MV5BNmVjM2IzOTQtNzZmNi00MzFjLTg3MGUtYTIwNzk3MDBhMWEwXkEyXkFqcGdeQXVyNTkyMjE3NDU@._V1_FMjpg_UX1000_.jpg',
                'title': 'The Wedding Squanchers',
                'description': "The Smith family is invited to the wedding of Rick's best friend, Birdperson. Things go south when it's discovered that the bride isn't who she says she is."
            })
    elif season_id == 3:
        if episode_id == 1:
            return jsonify({
                'id': episode_id,
                'videoUrl': 'https://drive.google.com/file/d/1Mql2ROKMT6ShMYq97EQjbkcNvCjQYaL3/view?usp=sharing',
                'videoPreviewImage': 'https://m.media-amazon.com/images/M/MV5BMTRmYzZmZjAtOTBlMy00ODJiLTgwMzEtMTVjN2Y2NzBjYzU3XkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_FMjpg_UX1000_.jpg',
                'title': 'The Rickshank Rickdemption',
                'description': 'Rick, still in galactic prison, puts an intricate escape plan into action. Back on Earth, which is now under federation control, Morty and Summer have an argument about their grandpa.'
            })
        elif episode_id == 3:
            return jsonify({
                'id': episode_id,
                'videoUrl': 'https://drive.google.com/file/d/1XNxjGnO8Qgrp42UOTjeH0QVwN4jeIrbw/view?usp=sharing',
                'videoPreviewImage': 'https://m.media-amazon.com/images/M/MV5BYWM5N2ZlMDEtNmFjZS00NDE3LWI1OWQtMGUxMzBhNzFhMTMzXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_FMjpg_UX1000_.jpg',
                'title': 'Pickle Rick',
                'description': 'Rick turns himself into a pickle while Beth, Summer, and Morty go to family therapy.'
            })
    elif season_id == 4:
        if episode_id == 3:
            return jsonify({
                'id': episode_id,
                'videoUrl': 'https://drive.google.com/file/d/1c7k9lWSlERO5gbnspAFSVn2rCw9hMzEo/view?usp=sharing',
                'videoPreviewImage': 'https://m.media-amazon.com/images/M/MV5BNTU3NjEwODQtY2JmMC00ZDUzLTkyMzgtODIwMDc0YzdhYzM2XkEyXkFqcGdeQXVyNjgzNDU2ODI@._V1_FMjpg_UX1000_.jpg',
                'title': "One Crew over the Crewcoo's Morty",
                'description': 'On a treasure-seeking expedition in an alien temple, Rick and Morty discover that a heist expert has snatched the prize from under their noses. Further twists, turns and double-crosses abound.'
            })
        elif episode_id == 5:
            return jsonify({
                'id': episode_id,
                'videoUrl': 'https://drive.google.com/file/d/1eYxHpnM_ajn4tbk_giAu5ZCUJ724yWM9/view?usp=sharing',
                'videoPreviewImage': 'https://m.media-amazon.com/images/M/MV5BZGM2MjFlZTAtYzEzMy00ZTc3LTliNzAtMWQ1ODBiYTVlZTZhXkEyXkFqcGdeQXVyMzQ0MTAyNjY@._V1_FMjpg_UX1000_.jpg',
                'title': 'Rattlestar Ricklactica',
                'description': "Morty discovers a race of intelligent space snakes after suffering a potentially lethal bite. Jerry attempts to prove that he isn't completely incompetent."
            })


if __name__ == '__main__':
    app.run()
