import subprocess
import csv


sytes = ['google.com', 'wikipedia.org', 'ru.hexlet.io', 'reddit.com', 'pythonworld.ru',
         'linux.org.ru', 'sky.pro', 'pyneng.readthedocs.io', 'stackoverflow.com', 'archlinux.org']
word = ['отправлено', 'получено', 'потеряно', 'Максимальное', 'Среднее', 'Минимальное']
heap = ['Adres', 'IP', 'Pack. sent', 'Pack. rec.','Pack. lost', 'Min time', 'Max time', 'Average time']
file = open('ping_sytes.csv', 'w')
writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
writer.writerow(heap)

for i in range (len(sytes)):
    arr = []
    arr.append(sytes[i])
    result = subprocess.run(['ping', '-n', '5', sytes[i]], capture_output=True).stdout
    result = result.decode('cp866').split(' ')
    for k in range(len(result)):

        if result[k] == sytes[i]:
            r = ((result[k + 1][1:-1]).encode()).decode('utf-8')
            arr.append(r)

        if result[k] in word[0:3]:
            r = ((result[k + 2][:-1]).encode()).decode('utf-8')
            arr.append(r)

        #if result[k] == word[3] or result[k] == word[4]:
        if result[k] in word[3:5]:
            r = ((result[k + 2]).encode()).decode('utf-8')
            arr.append(r)

        if result[k] == word[5]:
            r = ((result[k + 2][:-5]).encode()).decode('utf-8')
            arr.append(r)

    writer.writerow(arr)

file.close()
