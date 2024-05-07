# learn-python

Each .py file is a stand alone python file unless otherwise specified to give you a few examples of what I created when learning and messing around with python

## Importing Modules

- List installed packages.

    ```powershell
    pip list
    ```

- Show information about installed package(s).

    ```powershell
    pip show Package
    ```

    In the package's information the 'Location' must be listed in the sys.path which is the location python checks for modules. To check the paths python is currently checking run the following in the command line

    ```powershell
    python -c "import sys; print(sys.path)" # -c is to path python code which imports the sys module aka system then prints the sys path
    ```

    If the location is not present in the sys path then you must add it to the PYTHONPATH environment variable

### Dealing with the PYTHONPATH

#### Set PYTHONPATH

```powershell
$env:PYTHONPATH = "c:\users\user\appdata\local\programs\python\python310\lib\site-packages"
```

### My Research
