from PIL import Image
import os

def encode_lsb(image_path, message, output_path):
    img = Image.open(image_path)
    img = img.convert('RGB')
    pixels = img.load()

    message += "$t0p$"
    binary_message = ''.join(format(ord(c), '08b') for c in message)
    msg_index = 0

    for y in range(img.height):
        for x in range(img.width):
            r, g, b = pixels[x, y]

            if msg_index < len(binary_message):
                r = (r & ~1) | int(binary_message[msg_index])
                msg_index += 1
            if msg_index < len(binary_message):
                g = (g & ~1) | int(binary_message[msg_index])
                msg_index += 1
            if msg_index < len(binary_message):
                b = (b & ~1) | int(binary_message[msg_index])
                msg_index += 1

            pixels[x, y] = (r, g, b)

            if msg_index >= len(binary_message):
                break
        if msg_index >= len(binary_message):
            break

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path)
    print("✅ Pesan berhasil disisipkan ke:", output_path)


if __name__ == "__main__":
    input_filename = input("Masukkan nama file gambar (di folder input/, contoh: gambar_asli.png): ")
    message = input("Masukkan pesan yang ingin disisipkan: ")
    output_filename = input("Masukkan nama file output (contoh: gambar_baru.png): ")

    input_path = f"input/{input_filename}"
    output_path = f"output/{output_filename}"

    encode_lsb(input_path, message, output_path)
