def process_file():
    while True:
        # Get input filename from user
        input_filename = input("Enter the input filename: ")
        
        try:
            # Try to open and read the input file
            with open(input_filename, 'r') as input_file:
                content = input_file.read()
                
           
            name_parts = input_filename.rsplit('.', 1)
            if len(name_parts) > 1:
                output_filename = f"{name_parts[0]}_modified.{name_parts[1]}"
            else:
                output_filename = f"{input_filename}_modified"
            
            
            modified_content = content.upper()
            
           
            try:
                with open(output_filename, 'w') as output_file:
                    output_file.write(modified_content)
                print(f"\nSuccess! Modified content written to {output_filename}")
                print(f"Original length: {len(content)} characters")
                print(f"Modified length: {len(modified_content)} characters")
                break
                
            except PermissionError:
                print("Error: Don't have permission to create output file.")
            except IOError as e:
                print(f"Error writing to output file: {e}")
                
        except FileNotFoundError:
            print(f"Error: File '{input_filename}' not found. Please try again.")
        except PermissionError:
            print("Error: Don't have permission to read the file.")
        except UnicodeDecodeError:
            print("Error: File contains invalid characters or is not a text file.")
        except IOError as e:
            print(f"Error reading file: {e}")
        
        retry = input("\nWould you like to try another file? (y/n): ")
        if retry.lower() != 'y':
            print("Program terminated.")
            break

if __name__ == "__main__":
    print("File Processing Program")
    print("======================")
    print("This program reads a text file, converts its contents to uppercase,")
    print("and saves the result to a new file with '_modified' added to the name.")
    print("======================\n")
    
    process_file()
