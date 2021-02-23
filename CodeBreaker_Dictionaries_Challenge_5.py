#!/usr/bin/env python3

# Code Breaker app

# Create program that will encode or decode a secret message 
# based off a letter distribution (see previous Challenge 4 Letter Frequency Distribution program) of a pre-determined key text
# Determine the frequency analysis of two texts 
# And use the letter distributions to create a cypher
# to either encode or decode a text string entered by user
# 
# No longer asked to enter key phrase, instead use pre-determined key phrase
# 
# Analyze both phrases
# Decide if encoding or decoding
# Enter phrase
# Show encoded message and copy it
# Then rerun program and select decode and decode that message
# Verify that it matches original message

# Import
import FrequencyAnalysis_Dictinaries_Challenge_4 as fa

ipsum_text_1 = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed fermentum orci venenatis est faucibus venenatis. Mauris euismod quam quis neque rutrum cursus. Vivamus at diam massa. Nullam sit amet accumsan purus. Nullam metus turpis, aliquet id pharetra suscipit, fringilla in ex. Aliquam condimentum non lectus non aliquet. Nunc est tellus, vestibulum et ipsum non, mattis varius velit. Integer lobortis turpis in eros ornare lacinia.

Sed mollis, nibh non pellentesque porttitor, dui felis ornare magna, ac elementum erat sapien vitae ante. Ut quis magna mi. Integer quis bibendum sem. Morbi ac purus lorem. Morbi a sem rhoncus, varius metus in, consequat neque. Nulla nisi turpis, bibendum a ante vitae, ornare dictum quam. Integer quis nulla mi. Vivamus varius cursus est, a auctor mi aliquam quis.

Sed augue quam, aliquam at nunc at, sodales sagittis nunc. Sed vel arcu ac mauris mollis blandit non convallis leo. Mauris euismod nulla at eleifend fringilla. Praesent tempus lorem leo, sed consectetur quam varius at. Mauris bibendum ut neque eleifend cursus. Suspendisse pharetra, ante ac tempus consequat, lacus neque hendrerit orci, aliquam pellentesque lectus sapien imperdiet tortor. Cras at urna ac purus rhoncus elementum. Nam condimentum risus ac mattis blandit. In aliquam at lorem vel blandit. Ut maximus orci sapien, consectetur fermentum ex elementum sed. Vestibulum nec tempor dui. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.

Maecenas non ipsum id nunc sollicitudin ullamcorper. Nam vehicula lacinia turpis in fringilla. Nullam vel nisl sed eros pharetra ultrices ut sit amet nunc. Quisque vestibulum elementum nulla nec vulputate. Maecenas quam leo, posuere vel congue sed, dictum et lacus. Donec non aliquam lorem. Nam tempus lacinia nisi nec elementum. Donec sit amet tortor vitae augue pulvinar consectetur vitae non ante. Curabitur condimentum convallis lectus, id pharetra ex ultricies sed. Integer vitae aliquam lacus. In ultrices nisi ac ipsum imperdiet, vel mattis dui hendrerit.
"""

# analyze the text
sorted_db = fa.make_db(ipsum_text_1)

# display occurrences of each letter
fa.show_occurrence(sorted_db)
