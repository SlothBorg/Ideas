from itertools import combinations

SETTINGS = {
    'Al-Qadim': ['Arabian mythology', 'power of Fate', 'genies', 'elemental wizards', 'holy assassins'],
    'Ars Magica': ['historically grounded version of Europe', '1200 AD', 'Order of Hermes'],
    'Birthright': ['realm management', 'divinely empowered rulers', 'tactical gameplay', 'nation scale', 'political'],
    'Council of Wyrms': ['Dragons'],
    'Dark Sun': ['harsh desert', 'defiler magic', 'city states', 'Sorcerer-Kings', 'psionics', 'little metal', 'no gods', 'isolated from other planes', 'getting in is much, much easier than getting out'],
    'Dragon Fist': ['wuxia films', 'Kung fu', 'Chinese folklore and legend'],
    'Dragonlance': ['High Fantasy', 'Good vs. Evil', 'Dragons'],
    'Eberron': ['Magic as technology', 'Post Great war'],
    'Forgotten Realms': ['Kitchen sink fantasy'],
    'Freeport': ['Swashbuckling', 'Medieval fantasy', 'piracy', 'Lovecraftian horror', 'action-packed'],
    'Ghostwalk': ['Ghosts', 'Land of the dead', 'mausoleum city'],
    'Greyhawk': ['sword and sorcery', 'powerful single Empire', 'barbarian tribes', 'decadent empire', 'wildlands'],
    'Hollow World': ['underground', 'refuge and preserve', 'world inside the world', 'getting in is much, much easier than getting out'],
    'Jakandor': ['divided island', 'wizards', 'barbarians', 'necromancy', 'barbarians vs wizards'],
    'Kara-Tur': ['oriental', 'martial arts', 'samurais', 'ninjas', 'spirit folk', 'China', 'Japan', 'Korea'],
    'Mahasarpa': ['South Asian', 'India', 'surviving fractured kingdoms'],
    'Malatra': ['Living Jungle', 'verdant', 'isolated', 'little technology', 'True gods, money, and books are all unheard'],
    'Masque of the Red Death': ['Limited planar travel', 'Isolated', 'restricted magic', 'Gothic Earth', 'Dark powers', 'corruption', '19th century literary characters', '1890s'],
    'Maztica': ['Pre-Columbian Mesoamerica', 'Aztec culture', 'Mayan culture', 'animal spirits', 'jungles', 'lost cities & ruins'],
    'Midnight': ['Tolkienesque', 'Forces of darkness won', 'Evil Empire'],
    'Planescape': ['cosmopolitan', 'philosophical', 'urban', 'Lady of Pain', 'Central planr city', 'planar', 'has it\'s own slang', 'belifes mean more than alignment'],
    'Ptolus': ['Urban', 'megadungeon', 'ice age world', 'world covered in water', 'two moons'],
    'Ravenloft': ['Demiplane of Dread', 'Gothic horror', 'Dark powers', 'Dark lords rule domains', 'magic works differently',               'trapped'],
    'Red Steel': ['coastline', 'powerful metal that corrupts', 'disease held at bay', 'corruption', 'desperation'],
    'Spelljammer': ['wildspace', 'fantasy spaceships', 'age of exploration ships in space', 'travel between worlds',                 'epic fantasy'],
}

def python_list_to_md_list(python_list):
    md_list = ''
    for item in python_list:
        md_list += '* ' + item + '\n'

    return md_list

mashuped_settings = list( combinations(SETTINGS.keys(), 2) )

for mashup in mashuped_settings:
    tags = list( set(SETTINGS[mashup[0]]) | set(SETTINGS[mashup[1]]) )
    tags = list( map( lambda x:x.capitalize(), tags ) )
    tags.sort()

    print('## ' + mashup[0] + ' + ' + mashup[1] + '\n')
    print( python_list_to_md_list(tags) )
    print('---' + '\n')
