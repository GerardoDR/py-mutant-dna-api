from flask import Flask, request, make_response  # type: ignore
from mutant import find_four_in_a_row

app = Flask(__name__)


@app.route('/mutant', methods=['POST'])
def isMutant():
    print(request)
    dna = request.get_json()['dna']
    if request.get_json()['dna']:
        mutant = find_four_in_a_row(dna)[0]
        if mutant:
            print(mutant)
            return make_response('OK', 200)
        else:
            return make_response('Forbidden', 403)
    else:
        return make_response('BAD REQUEST', 400)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
