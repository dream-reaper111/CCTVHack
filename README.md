# CCTV Directory Browser

A Python terminal tool for browsing camera listings indexed by Insecam, featuring four browsing modes and a customizable terminal interface.

**creator :** [deadbyte.dll](https://github.com/dream-reaper111)  
**Instagram:** @DeadByte.dll  
<pre>
===============++++++++++++==================================--------==========---=======
===============+++++++++++*+++===============================------============----===---
=============++++++++++*+==+**+===============================----==============----=----
====+++++++++++**********+==++++===========================----=================----===--
====*********+++**++#*****+=====+===========================-====--=======---===----===--
===++==++*+*=====*++=+==+++==========+==++======================----===---------========-
=========*=++=====+===============+==----------------==========----===---------====---===
==========+======================--------====-----------========-====------------------==
========+=====================---------=-=--========----------==-=====-------------------
============================--------==-==--===-==-===-----------=======------------------
=====================++++=--------=====-----=----=-=====--==------======-----------------
====================+***=-------=-===-----------=-==-====-=====----====------------------
=================+++==+----=+--===-=====-------------=-==========----===-----------------
======================----=+--==---=---=-=---=---------------=====---==----------------==
=================+=++----++=-==-------=====---=--=======-==----===----==-----------------
===============*+***+---===-------==-=-+------==-=+=+*+===-------===---------------------
====+=============*+----===-------====+--=----=+=++*++*++===-----===---------------------
===**+================---=------===+======-----+=****+*+++===----====-==-----------=-----
++**+===+===============--------=**+++=====++--+**+*++*++++==----------=--------====--==-
++**+=+*++====+=*=======-------==*+***====++=--=*#+**+*++++++=---------===----======-====
+++=+==+**+++*+++=======-------=+++*+*=+*++==---*#*++++++*====--------=====---------=====
======================---------++*++*+==+=+*+---+++++*+==-------------====-========-=-==-
==================-=-----------++==*=*+=+*+=+---=+=+*=--------------=-==-===========-----
==================-=-----------=-------=++===*--=+++----------=--------=-======--=-------
==================-------------=-----------==+---==----------==-------===================
==================-------------==------------=--------------====-------==========--------
===================-------------==-----------+=--==--------===----------=-==--==-=-------
==================-=------------=++=--------==----===---=====--=-------======---==-----=-
============-=======--------------++===-====---------+=====----=-----======---=--=-==----
===========-========-========--=---++=+=====---------+===-----------=====----===--==-----
=================----==-======----------====------=====-==----=--=======-----=======-----
==================-===--=====---=-------=-++=====--++=--==---==-=======-------=======-*+-
=============-======----====-----+=-=----=--+===---===------==-========--------=======*==
==--==================--===------====-=--=---===---=--=-----=----=======---------========
-------===================---------==-----=--=---=--====--=-----=========----------------
==---====================-----------==---=-====--=-=====-=------==========---------====--
=-=========-========---=---------------=====+-=-=-=======------===========--------======-
=-=-==============----------------==-----====-+-=-=+==-------============-----------=====
================---------------==+===--------==+++-+--------=============----------=====-
===============--------------========------------------------===========--=-------====---
=============-=------------========-------------------------=================--======----
==============----------=+=======---------------------------=====-===================-===
==============--------+========--------------------------------=--==================-===-
-=============------=========-------------------------------=---=====================----
====-=-=======-----========------------------------------===-----======================--
=====--=======+=+========---------------------------------==-------====================--
-===---=====++=========--------=-------------------------=-=--==========================-
==----==================-----------------------=-----------=---===========--==-=---====--
-=----=======================--------------------==-------=--=============--=-===-=====--
------==========+++==========----------------------==-------======================-===---
------======================-----------------------====-==--====================---------
-----==================+=====-----------------------===========================----------
-----========================-----------------------============================---------
-----=======================--==-----------------=--=======================--=-----------
----=====================-----------------------==--=======================--------------
----====================--------------------=-=============================--------------
---=====================----------------------============-===============---------------
---======+=+===========-----------------------============================---------------
--=======++===========------------------------===========================-------=--------
-=============+++-==--------------------------============================-------=-===---
=====-=--+====--=*==-*++---------------------------===============-======-=-----=====----
======--===========----=---------------------------===============--===-----------====---
==#===============-----------------------------=----==============--==-----==-------==-=-
=================-------------------------------===------===-=====-=======---=-------===-





  
</pre>

## Overview

This program requests camera-directory pages, extracts listed camera URLs, and prints them in the terminal.

It does not exploit cameras, bypass authentication, or verify that a listed stream is available. A publicly listed address does not establish permission to access or record its footage. Use only for authorized research and cameras you own or have permission to assess.

## Features

- Browse listings by time zone.
- Browse listings by location/category.
- Browse listings by country.
- Browse listings by manufacturer.
- Colored terminal output.
- Animated text and loading effects.
- Customizable banners and menu artwork.
- Readable Python source with the original encoding removed.

“Location” refers to categories such as restaurant, park, beach, and traffic—not a precise geographic search.

## Project Structure

```text
CCTV/
├── hackcctv.py                  # Main menu and directory browsing
├── logos.py                    # Colors, banners, and display helpers
├── p.png                       # Optional project screenshot
├── deadbyte_banner_giant.txt    # Optional custom terminal banner
└── README.md
```

The banner text file is needed only if you added the external-banner customization.

## Requirements

- Python 3
- Requests
- Internet connection
- Terminal supporting UTF-8 and ANSI colors

Python already includes `re`, `os`, `sys`, `time`, and `subprocess`. These modules do not need separate installation.

## Installation

Open a terminal in your project folder:

### Original Dependency Installer

The original decoded source contains an `install_dependencies()` function that attempts to upgrade pip on launch and may attempt to install `re`.

Before running, remove that function and its call:

```python
install_dependencies()
```

Install dependencies explicitly using the virtual-environment commands above instead.

If your decoded files were downloaded as `.txt` files, save their contents as:

```text
hackcctv.py
logos.py
```

Keep both files in the same folder.

## Usage

```bash
source .venv/bin/activate
python hackcctv.py
```

Choose a mode:

| Option | Mode |
| --- | --- |
| 1 | Time zone |
| 2 | Location/category |
| 3 | Country |
| 4 | Manufacturer |

Enter the numbered selection shown on the next screen.

The program prints URLs extracted from matching directory pages.

At the exit prompt:

- Enter `n` to return to the main menu.
- Enter `y` to exit.

`Ctrl+C` interrupts the program, although the original broad exception handlers may catch it inside a browsing mode.

## Interface Customization

The screen text is stored in `logos.py`:

| Variable | Screen |
| --- | --- |
| `chois` | Main banner and menu |
| `timeline` | Time-zone selection |
| `loc_n` | Location/category selection |
| `coun_n` | Country selection |
| `cam_n` | Manufacturer selection |

Each screen has its own banner. Changing `chois` does not change the country screen or other selection screens.

### Custom External Banner

Place `deadbyte_banner_giant.txt` beside `logos.py`.

Add this after your color definitions:

```python
from pathlib import Path

custom_banner = Path(__file__).with_name(
    "deadbyte_banner_giant.txt"
).read_text(encoding="utf-8")
```

Then use the artwork in your main-menu string:

```python
chois = f"""{white}{bold}{custom_banner}

{cyan}1 - Time zone
2 - Location/category
3 - Country
4 - Manufacturer
"""
```

The giant banner requires at least 160 terminal columns to prevent wrapping. Use a monospace font with support for Unicode Braille characters.

### Result Labels

The handle printed above search results is defined separately in `hackcctv.py`.

To customize it, replace occurrences of:

```python
print(f'\n{bold + yellow}@Mohammadmahdi_termux')
```

with:

```python
print(f'\n{bold + yellow}@deadbyte.dll')
```

Preserve original authorship and applicable license notices when distributing modifications.

## Known Limitations

The decoded source preserves the original implementation and its existing bugs.

- Directory parsing depends on the website’s HTML structure.
- Requests use HTTP and have no explicit timeout.
- HTTP status codes are not checked.
- Missing pagination markup can cause errors.
- Pagination starts at zero.
- Results are not deduplicated.
- Camera availability is not checked.
- Some URL patterns contain unescaped dots.
- Country menu labels and country-code mappings contain inconsistencies.
- The time-zone list contains duplicate/placeholder entries and an input-range mismatch.
- The time-zone branch uses `time` as a string variable, shadowing the imported module in the main script’s namespace.
- Broad exception handlers hide detailed error messages.
- Dependency installation occurs at startup unless removed.

The program does not include a stream viewer, authentication testing, vulnerability scanning, or built-in result export.

## Troubleshooting

### Requests Is Missing

Activate the virtual environment and install Requests:

```bash
source .venv/bin/activate
python -m pip install requests
```

### Logos Module Is Missing

Confirm that these files are in the same directory:

```text
hackcctv.py
logos.py
```

### Custom Banner Is Missing

Confirm that `deadbyte_banner_giant.txt` is beside `logos.py` and that its filename matches the loading code.

### Wrong Banner Appears

Check which variable the active screen displays.

For example:

```python
type_text(coun_n)
```

prints the country screen, while:

```python
type_text(chois)
```

prints the main menu.

### Artwork Wraps

Widen the terminal or reduce the font size. Use a compatible monospace font.

### Generic Error or No Results

Possible causes include:

- Directory service unavailable.
- Network connection failure.
- Changed page structure.
- Missing pagination information.
- Empty category.
- Invalid selection.

The original generic error handler does not distinguish these conditions.

## Future Development

The following improvements are planned ideas, not implemented features:

- Consolidate repeated browsing logic.
- Add request timeouts and HTTP status checks.
- Replace broad exception handlers with specific diagnostics.
- Correct menu mappings and input ranges.
- Improve pagination handling.
- Deduplicate results.
- Add optional CSV and JSON export.
- Add terminal-width-aware banners.
- Add a no-color mode.
- Remove automatic dependency installation.
- Add offline HTML fixtures for parser verification.

<img width="373" height="498" alt="be" src="https://github.com/user-attachments/assets/9cd567a4-cb27-4b64-81e4-f117258c2f03" />
<img width="281" height="498" alt="hacked-get-hacked" src="https://github.com/user-attachments/assets/fe67df77-e74d-476d-b10c-016a43eae1f1" />
#PS: maybe next time Mohammed don't encrypted your program in base64 faggot get touched skid hope you like the improvements I'll be making since i was able to "hack" an get your Source LULZSEC
