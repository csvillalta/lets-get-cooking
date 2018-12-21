from textgenrnn import textgenrnn

recipe_generator = textgenrnn(name="title_generator")
recipe_generator.train_from_file("data/titles.txt", new_model=False,
                                    num_epochs=20,
									word_level=True,
									max_length=50,
									max_gen_length=50,
									max_words=1000)
