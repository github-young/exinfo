# exinfo

A python script to extract and plot EXIF info from RAW images


## Requirements

- Install the [ExifTool by Phil Harvey](https://exiftool.org/) and make sure `exiftool` is accessible.
- Install the python modules listed in the `requirements.txt`. For `pyexiftool`, make sure you install the correct one from: <https://pypi.org/project/PyExifTool/>.

## Usage

- Modify the path to your RAW images in both python files.
- Change the `tags` and labels, plotting ranges if necessary
- Run `exinfo.py` first to get the EXIF data, and then `plot.py` to plot them.
