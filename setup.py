from cx_Freeze import setup, Executable

base = None    

executables = [Executable("formulario.py", base=base)]

packages = ["idna","os","sys"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Formulario",
    options = options,
    version = "1.0",
    description = 'prova',
    executables = executables
)