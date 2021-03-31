while True:
    try:
        height = input('身長(m)?:')
        if len(height) == 0:
            #Enterキーだけが押された場合は終了する
            break

        #入力は文字列なので、少数に変換する
        height = float(height)
        weight = float(input('体重(kg)?:'))
        #組み込み関数powで累乗を計算する
        bmi = weight / pow(height, 2)

        #少数点以下第一位までの出力のフォーマット（format）する
        print('BMI値は{:.1f}です。'.format(bmi))
        if bmi < 18.5:
            print('少し痩せすぎです。')
        elif 18.5 <= bmi < 25.0:
            print('標準的な体型です。')
        elif 25.0 <= bmi < 30.0:
            print('少し太っています。')
        else:
            print('高度の肥満です。')
    except:
        print('半角英数字で入力してください。')
        