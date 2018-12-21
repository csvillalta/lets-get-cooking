from textgenrnn import textgenrnn
from random import randint

title_generator = textgenrnn('title_generator_weights.hdf5')
instruction_generator = textgenrnn('instruction_generator_weights.hdf5')

recipe_lines = randint(10,30)
generated_title = title_generator.generate(n=1,
                                            max_gen_length=50,
                                            return_as_list=True)
generated_instructions = instruction_generator.generate(n=recipe_lines,
                                                max_gen_length=1000,
                                                return_as_list=True)

print("Title: {}".format("".join(generated_title)))
print("Instructions:")
print(" ".join(generated_instructions))
