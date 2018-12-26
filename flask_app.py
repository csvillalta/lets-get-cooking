from flask import Flask, render_template, jsonify
from textgenrnn import textgenrnn
from random import randint
import tensorflow as tf


app = Flask(__name__)

def generate():
    with tf.Session() as sess:
        title_generator = textgenrnn('models/title_generator_weights.hdf5')
        instruction_generator = textgenrnn('models/instruction_generator_weights.hdf5')
        recipe_lines = randint(10,30)
        generated_title = title_generator.generate(n=1, max_gen_length=randint(30,60), return_as_list=True)
        generated_instructions = instruction_generator.generate(n=recipe_lines, max_gen_length=randint(500, 1500), return_as_list=True)

        title_string = "".join(generated_title)
        instruction_string = "".join([instruction+"\n" for instruction in generated_instructions])
        return title_string, instruction_string

@app.route('/')
def index():
    return render_template('index.html',
                            recipe_title = "",
                            recipe_instructions = "")

@app.route('/_get_new_recipe')
def get_new_recipe():
    new_title, new_instructions = generate()
    return jsonify(title=new_title, instructions=new_instructions)
