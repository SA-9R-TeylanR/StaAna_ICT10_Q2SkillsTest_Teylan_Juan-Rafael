from pyscript import document

# number: (name, type, height, weight)
pokedex = {
    "1": ("Bulbasaur", "Grass / Poison", "0.7 m", "6.9 kg"),
    "4": ("Charmander", "Fire", "0.6 m", "8.5 kg"),
    "6": ("Charizard", "Fire / Flying", "1.7 m", "90.5 kg"),
    "7": ("Squirtle", "Water", "0.5 m", "9.0 kg"),
    "25": ("Pikachu", "Electric", "0.4 m", "6.0 kg"),
    "39": ("Jigglypuff", "Normal / Fairy", "0.5 m", "5.5 kg"),
    "52": ("Meowth", "Normal", "0.4 m", "4.2 kg"),
    "54": ("Psyduck", "Water", "0.8 m", "19.6 kg"),
    "74": ("Geodude", "Rock / Ground", "0.4 m", "20.0 kg"),
    "94": ("Gengar", "Ghost / Poison", "1.5 m", "40.5 kg"),
    "95": ("Onix", "Rock / Ground", "8.8 m", "210.0 kg"),
    "129": ("Magikarp", "Water", "0.9 m", "10.0 kg"),
    "130": ("Gyarados", "Water / Flying", "6.5 m", "235.0 kg"),
    "131": ("Lapras", "Water / Ice", "2.5 m", "220.0 kg"),
    "132": ("Ditto", "Normal", "0.3 m", "4.0 kg"),
    "133": ("Eevee", "Normal", "0.3 m", "6.5 kg"),
    "143": ("Snorlax", "Normal", "2.1 m", "460.0 kg"),
    "149": ("Dragonite", "Dragon / Flying", "2.2 m", "210.0 kg"),
    "150": ("Mewtwo", "Psychic", "2.0 m", "122.0 kg"),
    "151": ("Mew", "Psychic", "0.4 m", "4.0 kg"),
}

not_found = ("Not in the Pokédex list", "-", "-", "-")


def pokemon_checker(event):
    number = document.getElementById("pokemon_number").value.strip()

    pokemon = pokedex.get(number, not_found)

   
    result = document.getElementById("result")
    result.innerHTML = (
        "<b>Pokédex No.:</b> " + number + "<br>"
        "<b>Name:</b> " + pokemon[0] + "<br>"
        "<b>Type:</b> " + pokemon[1] + "<br>"
        "<b>Height:</b> " + pokemon[2] + "<br>"
        "<b>Weight:</b> " + pokemon[3]
    )