from book import Book

buku1 = Book(1, "Belajar Python", "Affan", 2025)
buku2 = Book(2, "Belajar JAVA", "Albert", 2026)
buku3 = Book(3, "Belajar PBO", "Gibran", 2026)
buku4 = Book(4, "Belajar JAVA", "Albert", 2026)

print(buku1.judul)
print(buku1.get_update_terakhir())

buku1.update_judul("Belajar Python Bersama Albert")

print(buku1.judul)
print(buku1.get_update_terakhir())



print(buku2.judul)
print(buku2.get_update_terakhir())

buku2.update_judul("Belajar JAVA Bersama Albert")

print(buku2.judul)
print(buku2.get_update_terakhir())
