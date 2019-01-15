# CellML Validation tools

This repository brings together various validation tools for CellML.

## CellML 2.0 (Draft)

* [CellML 2.0 Schema](cellml_2_0/cellml_2_0.xsd)

## CellML 1.1

* [CellML 1.1 Schema](cellml_1_1/cellml_1_1.xsd) by Andrew Miller, Auckland Bioengineering Institute

## CellML 1.0

* [CellML 1.0 XML Schema](cellml_1_0/cellml_1_0_simple.xsd) written by Autumn Cuellar, Auckland Bioengineering Institute

* [CellML 1.0 DTD](cellml_1_0/cellml_1_0.dtd) by Warren Hedley, Auckland Bioengineering Institute

* [RELAX NG schema](cellml_1_0/cellml1.0.rnc) for CellML 1.0 written by Jonathan Cooper

## Tests

The validation files themselves can be tested using the following steps:

1. Create a virtual environment for python 3: `$ virtualenv venv -p python3` and activate it with `$ source venc/bin/activate`
2. Install the requirements using pip: `$p ip install -r requirements.txt`
3. Run the tests using pytest: `$ pytest`
