from PIL import Image

def decode_lsb(image_path):
    img = Image.open(image_path)
    img = img.convert('RGB')
    pixels = img.load()

    binary_data = ""
    for y in range(img.height):
        for x in range(img.width):
            r, g, b = pixels[x, y]
            binary_data += str(r & 1)
            binary_data += str(g & 1)
            binary_data += str(b & 1)

    chars = [chr(int(binary_data[i:i+8], 2)) for i in range(0, len(binary_data), 8)]
    message = ''.join(chars)
    end_marker = message.find('$t0p$')
    if end_marker != -1:
        return message[:end_marker]
    return "❌ Tidak ditemukan pesan tersembunyi."


if __name__ == "__main__":
    file_name = input("Masukkan nama file gambar untuk dibaca (di folder output/, contoh: gambar_baru.png): ")
    path = f"output/{file_name}"
    hasil = decode_lsb(path)
    print("📨 Pesan tersembunyi:", hasil)
