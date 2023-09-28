import socket

def compare_files(file1 , file2):
    with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
        content1 = f1.readlines()
        content2 = f2.readlines()

        # Check if the number of lines is different
        if len(content1) != len(content2):
            return False
        
        # Compare each line
        for line_num, (line1, line2) in enumerate(zip(content1, content2)):
            if line1 != line2:
                print(f"Difference found at line {line_num + 1}:\n")
                print(f"File 1: {line1.strip()}\n")
                print(f"File 2: {line2.strip()}\n")
                return False
    

        # if content1 == content2:
        #     return "Files are Identical"
        # else:
        #     return "Files are different"
        
def main():

    a = compare_files("../Data/abc.txt","../Data/pqrs.txt")
    print(a)

if __name__ == "__main__":
    main()

