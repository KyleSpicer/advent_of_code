
SAMPLE_FILE = "sample.txt"
DATA_FILE = "data.txt"

def main():
    with open(SAMPLE_FILE, "r") as file:
        data = file.read()

    print(f"{data = }")
    
if __name__=="__main__":
    main()