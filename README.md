magres-format
=============

Code for parsing the CCP-NC ab-initio magnetic resonance file format as used in the latest version of [CASTEP](http://www.castep.org), coming soon to other codes such as [Quantum ESPRESSO](http://www.quantum-espresso.org). See [more on this page](http://www.ccpnc.ac.uk/pmwiki.php/CCPNC/Fileformat)

Documentation for the Python API is [available here](http://tfgg.github.io/magres-format/build/html/).

A few IPython notebooks have been written using the library as examples. You can [see them here](https://github.com/tfgg/magres-format/tree/master/notebooks).

IPython is an enhanced interpreter for Python and offers an excellent in-browser workbook experience,
similar to Matlab or Mathematica. This is particularly useful when developing code using this library
to process your magnetic resonance calculations. You can [read instructions for installing it here](http://ipython.org/install.html).

<p align="center">
  <img src='https://github.com/tfgg/magres-format/raw/master//samples/ethanol.png' /><br/>
  A calculated J-coupling network in ethanol.
</p>

Installing
----------

Clone the repository or download and extract the .zip file somewhere. From the command line, run:

    sudo python setup.py install
    
to install it globally, or

    python setup.py install --user
    
to install it just for your user account ([read more here](http://docs.python.org/2/install/#alternate-installation)), and the Python module and associated scripts should now be installed.

If you have installed it locally with --user, you may have to add ~/.local/bin to your PATH. You can do this by adding

    export PATH=$HOME/.local/bin:$PATH
    
to your ~/.bashrc and restarting your session or running "source ~/.bashrc". If you use tcsh you do

    setenv PATH $HOME/.local/bin:$PATH
    
and then restart your session.

Extraction scripts
------------------

Some utility scripts for extracting values from a large number of calculation output files are provided.

`extract-ms.py` extracts magnetic shielding parameters. Call, optionally, with a species and, also optionally, an atomic index.

    extract-ms.py .

will print all magnetic shieldings for all atoms in all `.magres` files found in the current directory.

    extract-ms.py . Zn

will print only the magnetic shieldings of zinc atoms in all the `.magres` files found in the current directory.

    extract-ms.py . Zn1 

will print only the magnetic shielding of the first zinc atom in all the `.magres` files found in the current directory.

More generally, you can use an atom list format such as

    H,O
  
to show all hydrogen and oxygen atoms, and

    H1-5,O1
    
to show the first five hydrogen atoms and the first oxygen atom.

The `-N` flag optionally outputs in the first columns of the output an attempt at parsing out numbers in a path. This is useful for convergence tests. E.g. the path `grid_scale=2/energy_cut_off=80/ethanol.magres` will output the numbers 2.0 and 80.0 in the first two output columns.

The `extract-efg.py` and `extract-jc.py` scripts extract, respectively, EFG and J-coupling parameters, with a similar syntax. Call the scripts with a `-h` flag to view the full help information.

Conversion script usage
-----------------------

The `convertoldmagres.py` script converts an old-style Castep magres file to the new-style CCP-NC format for use with the new tools. You use it from the command line like:

    magres-convert.py sample.magres > sample.new.magres

and optionally with the associated job's .castep file, to capture the lattice information,

    magres_convert.py sample.magres sample.castep > sample.new.magres

Python module usage
-------------------

The `magres.format` and `magres.atoms` modules contain code for, respectively, a low level parser of the CCP-NC ab-initio magres format and a high-level collection of objects to represent its contents.

The module also include the useful `magres.constants` module, which gives the best-known gamma constants and quadrupole moments for all isotopes, the most common isotopes used in experiments.

More documentation is [available here](http://tfgg.github.io/magres-format/build/html/). Also, see the IPython notebooks linked at the top of this document.

JSON schema
-----------

We use the [JSONschema](http://json-schema.org/) definition to provide a specification for the internal datastructure used by the parser and the format of the JSON emitted and consumed by .as_json() and .load_json() on MagresFile.

To dump the JSON representation of a .magres simply do

    magresjson.py sample.magres > sample.magres.json

and sample.magres.json should now contain a schema-compliant JSON representation of sample.magres.
