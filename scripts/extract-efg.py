#!python

import os
import sys
import argparse

from magres.utils import load_all_magres, get_numeric

parser = argparse.ArgumentParser(description='Extract and print EFG values from a set of calculations.')
parser.add_argument('-N', '--numbers', action="store_const", help="Parse numbers from path and print. This is useful for e.g. convergence calculations.", default=False, const=True)
parser.add_argument('source_dir', help='Directory to look for calculations below.')
parser.add_argument('atom_species', nargs='?', type=str, default=None, help='Only print this atomic species.')
parser.add_argument('atom_index', nargs='?', type=int, default=None, help='Only print this atom.')

a = parser.parse_args(sys.argv[1:])

find_s = a.atom_species
find_i = a.atom_index

#tensors = ['efg', 'efg_local', 'efg_nonlocal']
tensors = ['efg']

lines = []

#print "# Number\tAtom\tCq\tCq_local\tCq_nonlocal\tEta\tEta_local\tEta_nonlocal\tPath"
print "# Number\tAtom\tCq\tEta\tPath"

magres_atoms = load_all_magres(a.source_dir)

for i, atoms in enumerate(magres_atoms):
  num = get_numeric(atoms.magres_file.path)

  if num:
    idx = num
  else:
    idx = [i]

  for atom in atoms: 
    if atom.species == find_s and \
      (find_i is None or atom.index == find_i) and \
      hasattr(atom, 'efg'):

      lines.append((idx,
                    atoms.magres_file.path,
                    str(atom),
                    ["%.2f" % getattr(atom, tensor).Cq for tensor in tensors],
                    ["%.2f" % getattr(atom, tensor).eta for tensor in tensors]))

lines = sorted(lines, key=lambda xs: xs[0])

for idx, path, atom, data1, data2 in lines:
  if a.numbers:
    print " ".join(map(str,idx)) + "\t" + atom + "\t" + "\t".join(data1) + "\t" + "\t".join(data2), path
  else:
    print atom + "\t" + "\t".join(data1) + "\t" + "\t".join(data2), path


