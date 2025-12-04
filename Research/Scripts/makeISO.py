import pycdlib, os

src = r"C:\Users\pprokhorov\Downloads\cosmonaut.com"
dst = r"C:\Users\pprokhorov\Downloads\challenge.iso"

if not os.path.exists(src):
    raise FileNotFoundError(src)

iso = pycdlib.PyCdlib()
iso.new(interchange_level=3)

iso.add_file(src, "/COSMONAU.COM;1")

iso.write(dst)
iso.close()

print("ISO created:", dst)
