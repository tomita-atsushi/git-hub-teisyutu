import time

# レベル水位作動辞書
level_dict = {
    0: '試運転終了',
    1: '起動ポンプ停止',
    2: 'ポンプ起動',
    3: '水位警報',
    4: '2台目ポンプ起動'
    }



# レベルスイッチの試運転入力指令のプログラミング
while True:
    testlevel = int(input('試運転したい動作を入力してください> '))
    if testlevel in level_dict:
        action = level_dict[testlevel]
        print(action)
        time.sleep(5)
    
    # レベル水位作動辞書にない場合
    else:
        print('レベル水位作動にないのでもう一度お願いします')
        time.sleep(5)
    
        
# レベル水位作動辞書にない場合(解決）
# もし、レベル水位作動辞書があってｎ秒後にテスト終了を自動的にする場合(解決)
# 試運転を終了するには

