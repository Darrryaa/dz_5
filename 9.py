p = input('Собака короткошерстной породы? ')
n = input('Рост собаки менее 50 см? ')
if p.lower() == 'да' and n.lower() == 'да':
    h = input('У собаки короткий хвост? ')
    if h.lower() == 'да':
        print('английский бульдог')
    else:
        u = input('У собаки длинные уши? ')
        if u.lower() == 'да':
            print('гончая')
        else:
            t = input('У собаки короткое тело? ')
            if t.lower() == 'да':
                print('мопс')
            else:
                print('чихуахуа')
elif p.lower() == 'да' and n.lower() == 'нет':
    v = input('Собака весит более 50 кг? ')
    if v.lower() == 'да':
        print('датский дог')
    else:
        print('фоксхаунд')
elif p.lower() == 'нет' and n.lower() == 'да':
    d = input('У собаки доброжелательный характер? ')
    if d.lower() == 'да':
        print('кокер-спаниэль')
    else:
        print('ирландский сеттер')
else:
    r = input('У собаки рост менее 70 см? ')
    if r.lower() == 'да':
        l = input('У собаки длинные уши? ')
        if l.lower() == 'да':
            print('большой вандейский грифон')
        else:
            print('колли')
    else:
        o = input('Окрас рыжий с белыми отметинами? ')
        if o.lower() == 'да':
            print('сенбернар')
        else:
            x = input('Белоснежный окрас? ')
            if x.lower() == 'да':
                print('ирландский волкодав')
            else:
                print('ньюфаундленд')