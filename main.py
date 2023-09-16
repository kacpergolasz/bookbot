from typing import Dict, NoReturn


def count_chars(text: str) -> Dict[str,int]:
  letters = {}
  for character in text.lower():
    try:
      letters[character]
    except KeyError:
      letters[character] = 0
    
    letters[character] += 1
  
  return letters

def get_sorted_alpha_dict(dict: Dict[str,int]) -> Dict[str,int]:
    letters = []
    for key in dict:
      if key.isalpha():
        letters.append(key)
    letters.sort()
    res = {}
    for letter in letters:
      res[letter] = dict[letter]
    
    return res

def print_letters(d: Dict[str,int]) -> NoReturn:
  for letter in d:
    print(f"The '{letter}' character was found {d[letter]} times")


with open("books/frankenstein.txt") as file:
  content = file.read()
  words = content.split()
  wordsCount = len(words)

  charactersDict = count_chars(content)
  lettersDict = get_sorted_alpha_dict(charactersDict)
  print_letters(lettersDict)



