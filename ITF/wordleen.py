# %% [markdown]
# <p align="center">
# <img src="https://docs.google.com/uc?id=14xeXxFrVRjvOoUYWn_GuyE-v84wVzrqr" class="img-fluid" alt="CLRWY" width="600" height="120" >
# </p>

# %% [markdown]
# <h1><p style="text-align: center; color:yellow">Python In-Class Session 16, <br>29 March 2022</p><h1>

# %%
# A dictionary/ words list
# grab 5 letters words
# grab according to green tiles
# grab according to gray tiles
# grab according to yellow tiles
# print possible words

# %%
import wordsen

# %%
def words_Letters():
    words_5letters = []
    for word in wordsen.words:
        if len(word) == 5 and word.isalpha():
            words_5letters.append(word.lower())
    return words_5letters

# %%
def grayWords(words_5letters, gray_letters):
    gray_words = []

    for word in words_5letters:
        gray_counter = 0
        for letter in gray_letters:
            if letter not in word:
                gray_counter +=1
            if gray_counter == len(gray_letters):
                gray_words.append(word)
    return gray_words


# %%
def greenWords(dictionary, green_letters):
    green_words = []
    how_many_letters = 0
    for i in green_letters:
        if i:
            how_many_letters += 1
    
    for word in dictionary:
        counter = 0
        for i in range(5):
            if word[i] == green_letters[i]:
                counter +=1
        if counter == how_many_letters:
            green_words.append(word)
    return green_words 


# %%
def yellowWords(dictionary, yellow_letters):
    yellow_words = []
    for word in dictionary:
        yellow_counter = 0
        for letter in yellow_letters:
            if letter in word:
                yellow_counter +=1
            if yellow_counter == len(yellow_letters):
                yellow_words.append(word)
    return yellow_words

# %%
def app():
    a = words_Letters()
    b = grayWords(a, gray_letters)
    c = greenWords(b, green_letters)
    d = yellowWords(c, yellow_letters)
    print(f"there are {len(d)} possible words. They are \n{d}")


# %%
gray_letters = "padin"
green_letters = ["","","","",""]
yellow_letters = "sty"
app()

# %%
def frequency():
    a = words_Letters()
    my_dict = {}
    for word in a:
        for letter in word:
            if letter not in my_dict:
                my_dict[letter] = 1
            else:
                my_dict[letter] += 1
    print(my_dict)
frequency()

# %%



