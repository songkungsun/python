try:
    list = []
    print(list[0])

    text = 'abc'
    number = int(text)
except IndexError as e:
    print('Fail',e)
except Exception as ex:
    print('Fail2',ex)