import subprocess

def collect_info_with_theharvester(domain):
  command = "theharvester -d {} -b all".format(domain)
  result = subprocess.run(command.split(), stdout=subprocess.PIPE)
  return result.stdout.decode()

# Exemple d'utilisation
info = collect_info_with_theharvester("google.com")
print(info)