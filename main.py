import os
import sys
import shutil



data = {
    "Web": [".html5", ".html", ".htm", ".xhtml"],
    "Picture": [
        ".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
        ".heif", ".psd"
    ],
    "Video": [
        ".avi", ".mkv", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob",
        ".mng", ".qt", ".mpg", ".mpeg", ".3gp"
    ],
    "Document": [
        ".oxps", ".epub", ".pages", ".docx", ".txt", ".pdf", ".doc", ".fdf",
        ".ods", ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
        ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", "pptx"
    ],
    "Compressed": [
        ".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z", ".dmg",
        ".rar", ".xar", ".zip"
    ],
    "Audio": [
        ".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", ".msv",
        "ogg", "oga", ".raw", ".vox", ".wav", ".wma"
    ],
    "python": [".py"]
}


class Filo:

  def __init__(self,
               path: str = "",
               dest: str = "",
               data: dict = data,
               ignore: list = []) -> None:
    self.ignore = ignore
    self.computed = {
        value.lower(): key
        for key, values in data.items() for value in values
    }

    #This Block checks if source path is valid
    if path == "":
      self.src = os.getcwd()
    else:
      self.src = self.path_check(path, False)

    #This Block checks if source path is valid
    if dest == "":
      self.dest = self.src
    else:
      self.dest = self.path_check(dest, True)
    #This function call coordinates the whole program
    self.Main()

  def Main(self):

    print("Setting destination to " + self.dest)
    print("\n\n\n.....................................\n")
    print("Organizing files in directory\n")
    self.OrganiseDir(self.src)
    print(".....................................\n\n\n")

  def path_check(self, path, bool):
    if not os.path.exists(path):
      if bool == False:
        print("\nPath not found. \nCheck if the passed path exists \n")
        sys.exit(1)
      else:
        print(
            "the Path you requested is not found ?\n do you want to create Path directory?(y/n)"
        )
        choice = input(":")
        if choice == "y":
          os.makedirs(path)
          print("Directory Created")
        else:
          print("Directory not created")
          print("Exixting program")
          sys.exit(1)
    return path

  def OrganiseStructure(self, dest, src, filename):
    if not os.path.exists(dest):
      os.mkdir(dest)
    shutil.copyfile(src, (os.path.join(dest, filename)))

  def OrganiseDir(self, path):
    #This function will get and display all files in the directory
    #this function also organize entire files
    print("+ " + (os.path.basename(path)))
    lists = []
    for each in os.scandir(path):
      if each.is_file():
        print("\t- " + (each.name))
        list = os.path.splitext(each)
        ext = list[1].lower()
        filename = each.name
        if (ext in self.computed) and filename not in self.ignore:
          self.OrganiseStructure(os.path.join(self.dest, self.computed[ext]),
                                 each.path, filename)
        else:
          lists.append(ext)
    print("\n\nPatterns not found for the following extensions\n")
    print(*lists)
    print("So they are not organized")


test = Filo("/home/runner/FileorganizerDiffe",
            "/home/runner/FileorganizerDiffe/newbro/test",
            ignore=["main.py"])


