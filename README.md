# Let's Get Cooking

Final project for CMSC 208: Speech Synthesis and Recognition

## Concept

I wanted to create a simple recipe generator using a recurrent neural network. I chose Max Woolf's implementation of [textgenrnn](https://github.com/minimaxir/textgenrnn) as my language model due to it's ease of use and flexibility. In designing this project I aimed more to generate humurous yet understandable recipes.

## Design

I ended up deciding to train two seperate models:
- A title generator
- An instruction generator

The original plan was to try to integrate some information from the generated title to the instruction generator for context, but I have yet to find an easy way to do this with the current model.

## Corpus

I gathered my data using the [Spoonacular API](https://spoonacular.com/food-api) and the [Spoonacular Python wrapper](https://github.com/johnwmillr/SpoonacularAPI). Unfortunately, the wrapper stopped working halfway through this project, so I did not end up collecting as much data as I would have liked. I have left the script to gather the recipes for documentation purposes.

## Future Plans

- Find another way to gather more recipe data
- Play around with different model parameters and models
- Create a visual interface for this project
- Try to integrate title and instruction contexts
