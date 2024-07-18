import os

def list_files(directory):
    files = []
    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file)) and not file.endswith("watermarked.mp4"):
            files.append(file)
    return files

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, "outputs")
    
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
        
        choice = input("Enter the number of the file to delete (or 'q' to quit): ")
        
        if choice.lower() == 'q':
            print("Exiting.")
            break
        
        try:
            choice_idx = int(choice) - 1
            if 0 <= choice_idx < len(files):
                selected_file = files[choice_idx]
                file_path = os.path.join(output_dir, selected_file)
                os.remove(file_path)
                print(f"Deleted {selected_file}.")
            else:
                print("Invalid number. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit.")
        except Exception as e:
            print(f"An error occurred: {e}")
        
        print("----------------------------------")

if __name__ == "__main__":
    main()
