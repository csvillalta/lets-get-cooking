from textgenrnn import textgenrnn
from random import randint

title_generator = textgenrnn('title_generator_weights.hdf5')
instruction_generator = textgenrnn('instruction_generator_weights.hdf5')

def generate():
    recipe_lines = randint(10,30)
    generated_title = title_generator.generate(n=1, max_gen_length=50, return_as_list=True)
    generated_instructions = instruction_generator.generate(n=recipe_lines, max_gen_length=1000, return_as_list=True)

    title_string = "".join(generated_title)
    instruction_string = "".join([instruction+"\n" for instruction in generated_instructions])

    return title_string, instruction_string

def generate_samples(n):
    for i in range(n):
        recipe_lines = randint(10,30)
        generated_title = title_generator.generate(n=1, max_gen_length=50, return_as_list=True)
        generated_instructions = instruction_generator.generate(n=recipe_lines, max_gen_length=1000, return_as_list=True)

        title = "".join(generated_title)
        generated_instructions = [instruction+"\n" for instruction in generated_instructions]
        salt = randint(0,1000) # to lower probability that filenames repeat
        file_name = "samples/{}_{}".format(title.replace(" ", "_").lower(), salt)

        with open(file_name, "w+") as f:
            f.write(title)
            f.write("\n\n")
            f.write("Instructions: \n")
            f.writelines(generated_instructions)

if __name__ == '__main__':
    generate_samples(2)
