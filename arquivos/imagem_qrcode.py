import qrcode
# pip install qrcode Pillow
data = "voce é meu amor "

img = qrcode.make(data)

img.save("qrcode_imagem.png")