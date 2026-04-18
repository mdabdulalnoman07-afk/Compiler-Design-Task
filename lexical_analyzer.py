import re
KEYWORDS = {"int", "float", "if", "else", "return"}
OPERATORS = {"=", "+", "-", "*", "/"}

def tokenize(source):
    token_re = re.compile(r"\s*(?:(\d+)|([A-Za-z_]\w*)|(\S))")
    tokens = []

    for number, word, symbol in token_re.findall(source):
        if number:
            tokens.append(("INT", number))
        elif word:
            kind = "KEYWORD" if word in KEYWORDS else "IDENTIFIER"
            tokens.append((kind, word))
        else:
            kind = "OPERATOR" if symbol in OPERATORS else "SYMBOL"
            tokens.append((kind, symbol))
    return tokens

if __name__ == "__main__":
    sample = "This is a int sum=a+b=20;"
    for kind, value in tokenize(sample):
        print(f"{kind}: {value}")