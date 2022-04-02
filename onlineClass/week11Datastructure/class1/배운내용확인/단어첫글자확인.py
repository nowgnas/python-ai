# 트럼프 대통령 트윗을 공백 기준으로 분리한 리스트입니다. 수정하지 마세요.
trump_tweets = ['thank', 'you', 'to', 'president', 'moon', 'of', 'south', 'korea', 'for',
                'the', 'beautiful', 'welcoming', 'ceremony', 'it', 'will', 'always', 'be', 'remembered']


def print_korea(tweet):
    '''
    문자열로 구성된 리스트에서 k로 시작하는 문자열을 출력합니다.
    '''
    for item in tweet:
        if item.startswith('k'):
            print(item)


# 아래 주석을 해제하고 결과를 확인해보세요.
print_korea(trump_tweets)
