


def  split_by_capitals(molecular_formula):
  if not molecular_formula:
    return[]
  result = []
  start = 0
  end = 1
  for i in molecular_formula[1:]:
    if i.isupper():
      result.append(molecular_formula[start:end])
      start = end
    end += 1
  result.append(molecular_formula[start:])
  return result

def split_at_number(atom):
    digit_location = 1
    for chr in atom[1:]:
      if chr.isdigit():
        break
      digit_location +=1
    if digit_location == len(atom):
      return atom,1
    return atom[:digit_location],int(atom[digit_location:])

def count_atoms_in_molecule(molecular_formula):
    """Takes a molecular formula (string) and returns a dictionary of atom counts.  
    Example: 'H2O' → {'H': 2, 'O': 1}"""

    atom_and_count={}

    for atom in split_by_capitals(molecular_formula):
        atom_name, atom_count = split_at_number(atom)
        if atom_name in atom_and_count:
          atom_and_count[atom_name]+=atom_count
        else:
          atom_and_count[atom_name]=atom_count
        
        

    return atom_and_count



def parse_chemical_reaction(reaction_equation):
    """Takes a reaction equation (string) and returns reactants and products as lists.  
    Example: 'H2 + O2 -> H2O' → (['H2', 'O2'], ['H2O'])"""
    reaction_equation = reaction_equation.replace(" ", "")  # Remove spaces for easier parsing
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")

def count_atoms_in_reaction(molecules_list):
    """Takes a list of molecular formulas and returns a list of atom count dictionaries.  
    Example: ['H2', 'O2'] → [{'H': 2}, {'O': 2}]"""
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
