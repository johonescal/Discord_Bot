from janome.tokenizer import Tokenizer

t = Tokenizer()

def main(discord_msg: str):
    
    # 単語分割
    for word in t.tokenize(discord_msg):
        # 単語の正規化
        return_str: str = normalization(str(word.surface))

        if return_str == 'カレー':
            return 0
        else:
            return 1


# 単語の正規化をする関数
def normalization(word: str):
    word = word.lower()
    return token


if __name__ == '__main__':
    main(dis_str)
