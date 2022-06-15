import socket
from _thread import *
from player import Player
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

players = [Player(), Player(), Player(), Player(), Player(), Player(), Player(), Player()]

def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    reply = ''

    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data

            if not data:
                print('Disconnected')
                break
            else:
                reply = rep()

                print('Received: ', data)
                print('Sending: ', reply)
            conn.sendall(pickle.dumps(reply))
        except:
            break

    print('Lost Connection')
    conn.close()

def rep(player):
    rep = ''
    if player == 1:
        rep = players[0]
    elif player == 2:
        rep = players[1]
    elif player == 3:
        rep = players[2]
    elif player == 4:
        rep = players[3]
    elif player == 5:
        rep = players[4]
    elif player == 6:
        rep = players[5]
    elif player == 7:
        rep = players[6]
    elif player == 8:
        rep = players[7]
    return rep

currentPlayer = 0
while True:
    conn, addr = s.accept()
    print('Connected to:', addr)

    start_new_thread(threaded_client(), (conn, currentPlayer))
    currentPlayer += 1