import csv
from operator import itemgetter

def pendapatan_kk(x):
    if 0 <= x < 0.4:
        rendah = 1
    elif 0.4 < x <= 0.8:
        rendah = float(0.8 - x) / float(0.8 - 0.4)
    else:
        rendah = 0.0

    if 0 <= x <= 0.4:
        sedang = 0
    elif 0.4 < x <= 0.8:
        sedang = float(x - 0.4) / float(0.8 - 0.4)
    elif 0.8 <= x <= 1.2:
        sedang = 1
    elif 1.2 <= x <= 1.4:
        sedang = float(1.4 - x) / float(1.4 - 1.2)
    else:
        sedang = 0.0

    if 0 <= x <= 1.2:
        tinggi = 0
    elif 1.2 <= x <= 1.4:
        tinggi = float(x - 1.2) / float(1.4 - 1.2)
    elif 1.4 < x <= 1.8:
        tinggi = 1
    elif 1.8 < x < 1.9:
        tinggi = float(1.9 - x) / float(1.9 - 1.8)
    else:
        tinggi = 0

    if 0 <= x <= 1.8:
        sangattinggi = 0
    elif 1.8 < x <= 1.9:
        sangattinggi = float(x - 1.8)/float(1.9 - 1.8)
    else:
        sangattinggi = 1

    return (rendah, sedang, tinggi, sangattinggi)


def hutang_kk(x):
    
    if 0 <= x <= 20:
        rendah = 1
    elif 20 < x <= 30:
        rendah = float(30 - x) / float(30 - 20)
    else:
        rendah = 0.0

    if 0 <= x <= 20:
        sedang = 0
    elif 20 <= x <= 30:
        sedang = float(x - 20) / float(30 - 20)
    elif 30 < x <= 60:
        sedang = 1
    elif 60 < x <= 80:
        sedang = float(80 - x) / float(80 - 60)
    else:
        sedang = 0.0

    if 0 <= x <= 60:
        tinggi = 0
    elif 60 <= x <= 70:
        tinggi = float(x - 60) / float(70 - 60)
    elif 70 < x <= 80:
        tinggi = 1
    elif 80 < x <= 90:
        tinggi = float(90 - x) / float(90 - 80)
    else:
        tinggi = 0.0
        
    if 0 <= x <= 80:
        sangattinggi = 0
    elif 80 < x <= 90:
        sangattinggi = float(x - 80) / float(90 - 80)
    else:
        sangattinggi = 1

    return (rendah, sedang, tinggi, sangattinggi)

def rule(pendapatan, hutang):
    h_rendah, h_sedang, h_tinggi, h_sangattinggi = hutang
    p_rendah, p_sedang, p_tinggi, p_sangattinggi = pendapatan
    y = min(h_rendah, p_rendah)
    y2 = min(h_sedang, p_rendah)
    y3 = min(h_rendah, p_sedang)
    y4 = min(h_sedang, p_sedang)
    y5 = min(h_sedang, p_tinggi)
    y6 = min(h_tinggi, p_tinggi)
    y7 = min(h_tinggi, p_sangattinggi)
    y8 = min(h_sangattinggi, p_tinggi)
    y9 = min(h_sangattinggi, h_sangattinggi)
    t = min(h_tinggi, p_rendah)
    t2 = min(h_sangattinggi, p_rendah)
    t3 = min(h_tinggi, p_sedang)
    t4 = min(h_sangattinggi, p_sedang)
    t5 = min(h_rendah, p_tinggi)
    t6 = min(h_rendah, p_sangattinggi)
    t7 = min(h_sedang, p_sangattinggi)
    return max(y, y2, y3, y4, y5, y6, y7, y8, y9), \
           max(t, t2, t3, t4, t5, t6, t7)

def defuzzyfication(rule):
    y, x = rule
    score = (x * 100) + (y * 50) / (x + y)
    return score;

def fuzzy_system(pendapatan, hutang):
    fuzzy_pendapatan = pendapatan_kk(pendapatan)
    fuzzy_hutang = hutang_kk(hutang)
    val = rule(fuzzy_pendapatan, fuzzy_hutang)
    return defuzzyfication(val)

if __name__ == '__main__':
    score = []
    data = open('DataTugas2.csv', 'r')
    data.readline()
    count, accepted = 0, 0.0
    for row in data:
        count += 1
        nomor, pendapatan, hutang = row[:-1].split(',')
        prediction = fuzzy_system(float(pendapatan), float(hutang))
        score.append([])
        score[count - 1].append(count)
        score[count - 1].append(prediction)
    score = sorted(score, key=itemgetter(1), reverse=True)
    print("20 Kepala Keluarga yang mendapatkan BLT:")
    for i in range(20):
        print("Kepala Keluarga Nomor : ", score[i][0])


with open("TebakanTugas2.csv", 'w', newline='') as myfile:
    fieldnames=['Kepala Keluarga Nomor']
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    for i in range(20):
         wr.writerow([score[i][0]])
