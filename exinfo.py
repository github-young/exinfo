from exiftool import ExifToolHelper
from pathlib import Path
import pandas as pd
import sys

# tags can be first extracted by ExifTool
tags = ["Composite:Aperture", "EXIF:FocalLength"]
labels = tags + ["SourceFile"]

# files = ["IMG_5270.CR2"]
files = list(Path("/path/to/your/raw/images/").rglob("*.CR2"))

csvname = "exinfo_data.csv"


def extract_info(files: list, tags: list, thresh=20):
    # judge whether continue run
    if len(files) > thresh:
        if not can_continue_run(thresh):
            sys.exit(-1)
    # extract info with ExifTool
    with ExifToolHelper() as et:
        df = []
        for d in et.get_tags(files=files, tags=tags):
            df += [[d[key] for key in tags] + [f"{Path(d[labels[-1]]).name}"]]
    # output to pd.DF
    columns = labels
    return pd.DataFrame(df, columns=columns)


def can_continue_run(thresh):
    if len(files) > thresh:
        user_input = "N"
        user_input = input("It might take long to process so many images. Continue? [y/N]: ").strip().lower()
        if user_input == "y":
            print("Continuing the program...")
            return True
        else:
            print("Exiting the program...")
        return False


df = extract_info(files, tags)
print(df)
df.to_csv(csvname, sep=",", index=True)
