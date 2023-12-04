import math

# Fungsi a(x) adalah untuk mengembalikan nilai kuadrat dari x.
def a(x):
    return x**2
print(a(4))

# Fungsi al melakukan hal yang sama dengan fungsi a(x).
al = lambda x: x ** 2
print(al(5))

# Fungsi b(x, y) adalah untuk mengembalikan nilai akar kuadrat dari jumlah kuadrat dari x dan y.
def b(x, y):
    return math.sqrt(x**2 + y**2)
print(b(2, 4))

# Fungsi bl melakukan hal yang sama dengan fungsi b(x ,y).
bl = lambda x, y: math.sqrt(x ** 2 + y ** 2)
print(bl(3, 5))

# Fungsi c(*args) adalah untuk mengembalikan rata-rata dari semua nilai yang diberikan sebagai argumen.
def c(*args):
    return sum(args)/len(args)
print(c(1, 3, 5, 7, 9))

# Fungsi cl melakukan hal yang sama dengan fungsi c(*args).
cl = lambda *args: sum(args) / len(args)
print(cl(2, 4, 6, 8, 10))

# Fungsi d(s) adalah untuk mengembalikan string unik dari karakter dalam s.
# Fungsi set untuk menghapus duplikat dan kemudian join untuk menggabungkan karakter-karakter tersebut menjadi satu string.
def d(s):
    return "".join(set(s))
print(d("TerimakasihSeseorang"))

# Fungsi dl melakukan hal yang sama dengan fungsi d(s).
dl = lambda s: "".join(set(s))
print(dl("SamaSamaSeseorang"))