import json
from pathlib import Path

def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def merge_json(file1, file2, output):
    """Fusionne deux fichiers JSON en gardant TOUTES les donnees"""
    data1 = load_json(file1)
    data2 = load_json(file2)
    
    print(f"Fichier 1: {len(data1)} entrees")
    print(f"Fichier 2: {len(data2)} entrees")
    
    # Simple concatenation
    merged = data1 + data2
    
    print(f"Total: {len(merged)} entrees")
    
    # Sauvegarder
    with open(output, 'w', encoding='utf-8') as f:
        json.dump(merged, f, ensure_ascii=False, indent=2)
    
    return merged

def main():
    # Repertoire actuel (ou est le script)
    script_dir = Path(__file__).parent
    data_dir = script_dir / 'data-raw'
    
    file1 = data_dir / 'arbres-remarquables-du-territoire-des-hauts-de-seine-hors-proprietes-privees.json'
    file2 = data_dir / 'les-arbres.json'
    output = data_dir / 'mergeddata.json'
    
    result = merge_json(file1, file2, output)
    
    print(f"\nResultat sauvegarde: {output}")

if __name__ == "__main__":
    main()