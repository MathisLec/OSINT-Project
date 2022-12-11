import DnsScan

def write(file_name, txt):
    with open(os.path.join(os.getcwd(),"resources","example.json"), 'w+') as f:
        f.write(txt)

def main():
    DnsScan.scanL("www.google.fr")
main()