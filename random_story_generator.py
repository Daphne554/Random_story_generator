import random

story_title = ['Sapphire', 'Topaz', 'Opal', 'Garnet','Hyacinth', 'Coral']

# Defining list of phrases which will help to build a story
starter = ['About 100 years ago', 'In the 20 BC', 'Once upon a time']

character = [' there lived a king.', ' there was a man named Jack.', ' there was a classy lady.', 'there lived a '
                                                                                                  'farmer.']

time = [' One day', ' One full-moon night', ' One hot afternoon']

story_plot = [' he was passing by', ' he was going for a picnic to', ' he was returning from the vineyard']

place = [' the mountains,', ' the souk,', ' the garden,']

second_character = [' he saw a man', ' he saw a small innocent creature', ' he saw a young lady']

age = [' who seemed to be in late 20s', ' who was hurt and in a lot of pain', ' who seemed very old and feeble']

work = [' shivering in the rain', ' in search of shelter and help.', ' sitting in the rain by the roadside.']

print(random.choice(story_title))
print(
    random.choice(starter) + random.choice(character) + random.choice(time) + random.choice(story_plot) + random.choice(
        place) + random.choice(second_character) + random.choice(age) + random.choice(work))
