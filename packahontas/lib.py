def try_me(text):
    return ' '.join([word[::-1] for word in text.split()])

if __name__=='__main__':
    print(try_me('Hello world'))