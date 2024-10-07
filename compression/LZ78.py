from dataclasses import dataclass

__version__ = "1.0"
__author__ = "Ahmed Tamer"

@dataclass
class Token:
  """
    Dataclass representing pair called token consisting of the dictionary index and a single character that follows the phrase in the dictionary.
  """
  
  index: int
  char: str
  
  def __repr__(self) -> str:
    return f"({self.index}, {self.char})"
  

class LZ78Compressor:
  """
    Class containing compress and decompress methods using LZ78 compression algorithm.
  """
  
  def compress(self, text: str) -> list[Token]:
    """
      Compress the given string text using LZ77 compression algorithm.

      Args:
          text: string to be compressed

      Returns:
          output: the compressed text as a list of Tokens
    """

    phrase_dict = {}
    tokens = []
    code = 1
    phrase = ''
    for char in text:
      phrase += char
      if phrase not in phrase_dict:
        phrase_dict[phrase] = str(code)
        if len(phrase) == 1:
          tokens.append(Token('0', phrase))
        else:
          tokens.append(Token(phrase_dict[phrase[:-1]], phrase[-1]))
        code += 1
        phrase = ''
    return tokens
  
  
  def decompress(self, tokens: list[Token]) -> str:
    """
        Convert the list of tokens into an output string.

        Args:
            tokens: list containing pairs (index, char)

        Returns:
            output: decompressed text
    """

    text = ''
    phrase_dict = {'0': ''}
    code = 1
    for token in tokens:
      phrase = phrase_dict[token.index] + token.char
      phrase_dict[str(code)] = phrase
      code += 1
      text += phrase
    return text
  
  
if __name__ == '__main__':
  # Example
  text = 'Hi, this is me!'
  lz78_compressor = LZ78Compressor()
  tokens = lz78_compressor.compress(text = text)
  print(lz78_compressor.decompress(tokens))
