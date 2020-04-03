# Gaussian Excited State Logfile Parser

Reads output files obtained from Gaussian calculations of excited states (using the keyword 'TD'). The script extracts the relevant data and prints it in the terminal as a table.

## Usage

Call the script `es_table.py` together with the path to the log file of interest. One example is provided in this folder: `pbe0_pyr_vertS.log`. This is a TD-DFT calculation producing the five lowest vertical singlet excited states of pyridine, using the DFT functional PBE0. A title to the printed table may be specified with the flag `-t` or `--title` along with the desired title as a string. If this is not provided, the default title will be printed.

### Roadmap

- [x] `models.py` to store data
- [x] `logparser.py` to parse log file
    - [x] States
    - [x] Transitions
- [x] Documentation
- [x] `render.py` to print the data in a simple table
- [x] Terminal interface

#### Future features
- [ ] `export.py` to present the data in a csv format or similar
- [ ] Make rendering customisable
- [ ] Pretty print classes
- [ ] Possibility to add character to the recognised orbitals