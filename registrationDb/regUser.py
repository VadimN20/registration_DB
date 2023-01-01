import sqlite3


def writeIn(Log, Pas, regTime):
    if len(Log) < 5:
        return 'Логин должен содержать более 5 символов'
    elif len(Pas) < 6:
        return 'Пароль должен содержать более 6 символов'
    else:
        base_users = sqlite3.connect('user.db')
        cur = base_users.cursor()
        base_users.execute(
            'CREATE TABLE IF NOT EXISTS {}(login, password, time_registration, last_login_time)'.format('users_list'))
        base_users.commit()

        if checkUser(Log)[0]:
            cur.execute('INSERT OR REPLACE INTO users_list VALUES(?, ?, ?)', (Log, Pas, regTime))
            base_users.commit()
            showInfo(cur, base_users)
            return checkUser(Log)[1]
        else:
            showInfo(cur, base_users)
            return 'Пользователь с таким логином уже существует'


def logIn(Log, pas, lastTime):
    base_users = sqlite3.connect('user.db')
    cur = base_users.cursor()

    base_users.execute(
        'CREATE TABLE IF NOT EXISTS {}(login, password, time_registration, last_login_time)'.format('users_list'))
    base_users.commit()

    if not checkUser(Log)[0]:
        if not checkPass(Log, pas, lastTime)[0]:
            base_users.execute('UPDATE users_list SET last_login_time = ? WHERE login = ?', (lastTime, Log))
            base_users.commit()
            showInfo(cur, base_users)
        return checkPass(Log, pas, lastTime)[1]
    else:
        return checkUser(Log)[1]


def checkUser(Log):
    base_users = sqlite3.connect('user.db')
    cur = base_users.cursor()

    info = cur.execute('SELECT * FROM users_list WHERE login = ?', (Log,)).fetchone()
    if info is None:
        return (True, 'Пользователя с таким логином нет')
    else:
        return (False, 'Вы успешно зарегистрировались')


def checkPass(log, pas, lastTime):
    base_users = sqlite3.connect('user.db')
    cur = base_users.cursor()

    info = cur.execute('SELECT * FROM users_list WHERE login = ? AND password = ?', (log, pas))
    if info.fetchone() is None:
        return (True, 'Вы ввели неверный пароль')
    else:
        return (False, 'Вы вошли')


def showInfo(cur, base_users):
    info = cur.execute('SELECT * FROM users_list').fetchall()
    print(info)
    base_users.close()
