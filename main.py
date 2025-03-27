import os
    
# Function to load the file
def load_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
        
    except IOError as e:
        print(f'Error reading file {filename}: {e}')
        
#Choosing file from the working directory
def file_from_dir(dir='.'):
    # List all the files in the dir
    files = [f for f in os.listdir(dir) 
            if os.path.isfile(os.path.join(dir, f)) and f.lower().endswith('.txt')]
    if not files:
        print('No text files found in director', dir)
        return None
    # Printing all files in dir
    print('\nFiles found in Directory: ')
    for idx, file in enumerate(files, start=1):
        print(f'{idx}. {file}')
        
    while True:
        try:
            choice = int(input('Files You wanna select:'))
            if 1 <= choice <= len(files):
                selected = os.path.join(dir, files[choice-1])
                print(f'Selected: {selected}')
                return selected
            else:
                print('Please choose a nber btn 1 and ', len(files))
                
        except:
            print('Invalid Input.Try again')

#Checking the file
def compare_text():
    print('Select the First file')
    file1 = file_from_dir()
    if file1 is None:
        return
    print('\nSelect the Second file')
    file2 = file_from_dir()
    if file2 is None:
        return
    
    vc = plagiarism()
    con1 = vc.into_set(file1)
    con2 = vc.into_set(file2)
    vc.check(con1, con2)

def menu():
    while True:
        print("\n---- Plagiarism Checker Menu ----")
        print("1. Check Plagiarism")
        print("2. Search")
        print("3. Exit")
        choice = input("Enter your choice : ").strip()
        if choice == "1":
            compare_text()
        elif choice == "3":
            print("Exiting ...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()