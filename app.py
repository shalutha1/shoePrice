import string
import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

def prediction(lst):
    filename = 'model/shoe_predictor(1).pickle'
    with open(filename, 'rb') as file:
        model = pickle.load(file)
        pred_value = model.predict([lst])
        return pred_value

def traverse(lst, item):
    filename = 'model/shoe_predictor(1).pickle'
    with open(filename, 'rb') as file:
        model = pickle.load(file)
        traverse_value = model.traverse([lst, item])
        return traverse_value

@app.route('/', methods=['POST', 'GET'])
def index():
    pred = None  # Initialize pred with a default value

    if request.method == 'POST':
        brand = request.form['brand']
        type = request.form['type']
        gender = request.form['gender']
        size = request.form['size']
        color = request.form['color']
        material = request.form['material']

        feature_list = []
        feature_list.append(len(gender))
        feature_list.append(int(size))

        brand_list = ['nike', 'adidas', 'reebok', 'converse', 'puma', 'vans', 'new balance', 'asics', 'fila', 'skechers']
        type_list = ['sport', 'casual', 'fashion', 'lifestyle', 'slides', 'retro']
        color_list = ['black', 'white', 'grey', 'black/white', 'pink', 'other']
        material_list = ['mesh', 'leather', 'canvas', 'primeknit', 'leather/synthetic', 'synthetic', 'suede/mesh', 'suede/canvas', 'suede', 'flyknit', 'knit', 'nylon', 'other']

        for item in brand_list:
            if item == brand:
                feature_list.append(1)
            else:
                feature_list.append(0)

        traverse(brand_list, brand)
        traverse(type_list, type)
        traverse(color_list, color)
        traverse(material_list, material)

        pred = prediction(feature_list)
        print(pred)

    return render_template("index.html", pred=pred)

if __name__ == '__main__':
    app.run(debug=True)
