import socket
from _thread import *
from game import Game
import pickle

server = '192.168.1.219'
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(8)
print('Waiting for a connection...')

connected = set()
games = {}
idCount = 0

def threaded_client(conn, p, p2, gameId):
    global idCount
    conn.send(str.encode(str(p)))

    reply = ''
    while True:
        data = conn.recv(4096).decode()

        try:
            if gameId in games:
                game = games[gameId]

                if not data:
                    break
                else:
                    if data == 'reset':
                        game.reset()
                    elif data == 'request':
                        game.request(p, data)
                    elif data == 'reply':
                        game.reply(p, data)
                    elif data == 'action':
                        game.action(p, data)


                    reply = game
                    conn.sendall(pickle.dumps(reply))
            else:
                break
        except:
            break
    print('Lost Connection')
    try:
        del games[gameId]
        print('Closing Game:', gameId)
    except:
        pass
    idCount -= 1
    conn.close()





while True:
    conn, addr = s.accept()
    print('Connected to:', addr)

    idCount += 1
    p = 0
    p2 = 1
    gameId = (idCount - 1) // 8

    if idCount % 8 == 1:
        games[gameId] = Game(gameId)


    start_new_thread(threaded_client(), (conn, p, p2, gameId))
