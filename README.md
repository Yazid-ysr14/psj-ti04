# psj-ti04
subprocess
p1 = subprocess.Popen([“ping”,"IP","address"], stdout=subprocess.PIPE)
p2 = subprocess.Popen([“echo”, “Gagal: IP address belum diberikan”], stdin=p1.stdout, stdout=subprocess.PIPE)
p1.stdout.close()
output = p2.communicate()[0]
print(output)
