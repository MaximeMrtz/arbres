import json
from pathlib import Path

def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def filter_keys(entry, source):
    """Garde uniquement les colonnes essentielles"""
    if source == 'hauts_de_seine':
        return {
            'source': 'Hauts-de-Seine',
            'commune': entry.get('commune'),
            'code_insee': entry.get('code_insee'),
            'nom': entry.get('nom_francais'),
            'latin': entry.get('nom_latin'),
            'hauteur': entry.get('hauteur'),
            'circonference': entry.get('circonference'),
            'localisation': entry.get('geo_point_2d')
        }
    else:
        return {
            'source': 'Paris',
            'commune': entry.get('arrondissement'),
            'code_insee': None,
            'nom': entry.get('libellefrancais'),
            'latin': f"{entry.get('genre', '')} {entry.get('espece', '')}".strip(),
            'hauteur': entry.get('hauteurenm'),
            'circonference': entry.get('circonferenceencm'),
            'localisation': entry.get('geo_point_2d')
        }

def merge_json(file1, file2, output):
    data1 = load_json(file1)
    data2 = load_json(file2)
    
    print(f"Fichier 1: {len(data1)} entrees")
    print(f"Fichier 2: {len(data2)} entrees")
    
    merged = []
    for entry in data1:
        merged.append(filter_keys(entry, 'hauts_de_seine'))
    for entry in data2:
        merged.append(filter_keys(entry, 'paris'))
    
    print(f"Total: {len(merged)} entrees")
    
    with open(output, 'w', encoding='utf-8') as f:
        json.dump(merged, f, ensure_ascii=False, indent=2)
    
    return merged

def main():
    script_dir = Path(__file__).parent
    data_dir = script_dir / 'data-raw'
    
    file1 = data_dir / 'arbres-remarquables-du-territoire-des-hauts-de-seine-hors-proprietes-privees.json'
    file2 = data_dir / 'les-arbres.json'
    output = data_dir / 'mergeddata.json'
    
    result = merge_json(file1, file2, output)
    
    print(f"\nResultat sauvegarde: {output}")

if __name__ == "__main__":
    main()