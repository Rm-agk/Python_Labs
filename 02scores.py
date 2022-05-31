scores = list(input('Please enter a list of scores:'))
win = 0
draw = 0
loss = 0

for i in scores:
    if i == '3':
        win = win + 1
    if i == '1':
        draw = draw + 1
    if i == '0':
        loss = loss + 1

print('Draws:',draw)
print('Losses:',loss)
print('Wins:',win)
