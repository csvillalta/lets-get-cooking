from textgenrnn import textgenrnn

recipe_generator = textgenrnn(name="instruction_generator")
recipe_generator.train_from_file("data/instructions_spaced.txt", new_model=False,
                                    num_epochs=1,
									word_level=True,
									max_length=1000,
									max_gen_length=1000,
									max_words=1000)
