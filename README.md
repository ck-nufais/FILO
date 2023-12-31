# File Organizer(FILO)

This Python program is designed to organize files in a directory based on their file extensions. It helps in decluttering your workspace by categorizing files into different folders.

## Features

- Automatically sorts files into categories such as Web, Picture, Video, Document, Compressed, Audio, and Python based on their file extensions.
- Provides the flexibility to specify the source and destination directories for organization.
- Allows the user to specify certain files to be ignored during the organization process.

## Usage

1. Ensure you have Python installed on your system.
2. Download or clone the repository to your local machine.
3. Open a terminal or command prompt and navigate to the directory containing the main.py file.
4. Run the program by executing the following command:

        python main.py
    

5. After execution, the files in the current directory will be organized based on their types into separate folders.

## Configuration

The data dictionary in the main.py file contains the file extensions associated with different categories. You can modify this dictionary to suit your specific file categorization needs.

## Options

The program allows for the following options while creating an instance of the Filo class.:

- Ignoring certain files from the organization process by specifying them in the ignore parameter
- Add custom dictionary mapped to file extension in data parameter 
## Example

        from FILO.main import Filo
        #Ignore the file "example_file.txt" during organization
        #Add custom dictionary with different extensions
        
        organizer = Filo("/path/to/source_directory", "/path/to/destination_directory", ignore=["important.py"],data={"web":[".html",".htm",".css"],"Python":[".py"]})
        organizer.OrganiseDir()

