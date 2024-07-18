import os
import subprocess

def list_files(directory):
    files = []
    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file)):
            files.append(file)
    return files

def main():
    output_dir = os.path.expanduser("~/outputs")
    
    # Check if the directory exists
    if not os.path.isdir(output_dir):
        print(f"Directory {output_dir} does not exist.")
        return
    
    while True:
        # List files in the directory
        files = list_files(output_dir)
        if not files:
            print(f"No files found in {output_dir}. Exiting.")
            return
        
        print("Files in outputs:")
        for i, file in enumerate(files, 1):
            print(f"{i}. {file}")
        
        choice = input("Enter the number of the file to play (or 'q' to quit): ")
        
        if choice.lower() == 'q':
            print("Exiting.")
            break
        
        try:
            choice_idx = int(choice) - 1
            if 0 <= choice_idx < len(files):
                selected_file = files[choice_idx]
                file_path = os.path.join(output_dir, selected_file)
                print(f"Playing {selected_file}...")
                subprocess.run(["mpv", file_path])
            else:
                print("Invalid number. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit.")
        
        print("----------------------------------")

if __name__ == "__main__":
    main()
