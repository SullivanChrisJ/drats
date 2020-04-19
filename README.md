# drats
Taking a shot at bringing d-rats up to date. Mostly using a brute force run it and see what breaks approach.

# Dependencies: Within reason, use well-supported/regarded libraries that can be installed with pip
pyserial            3.4
pyspellchecker      0.5.4       (spell module converted from piping to daemon to direct call)

# Things of note:
> File d_rats.platform.py collides with the Python built-in module. Worked around it by using explicit file path
  There may be an opportunity to use the built-in instead if there is enough overlap in function.
> The GTK module for the UI is difficult to install and incompatible with Python 3. Opting to use Tkinter & ttk
  which is a bit of a journey into the unknown. Will take  it 1 day at a time.
> Changing everything to f-strings where I see them. Sometimes I skip over them but may loop back some day and
  get the rest. There's a lot of opportunities as there is a lot of string formatting (using C-like formatting)
> The file() function in Python 2 is gone. With it, the debug log is opened with unbuffered I/O, which is not
  allowed in the replacement function open() for text files. If it turns out that buffering is a problem, due to
  the last item of a debug log not getting written before a program crash, it might be necessary to write a 
  custom class to flush the buffers after each write. 