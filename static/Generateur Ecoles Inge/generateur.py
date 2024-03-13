import json
import csv

def format_ecole(ecoles_conf, ecole):
    markdown = f"\n\n## {ecole}"

    if not ecole in ecoles_conf.keys():
        # print(f"Ecole {ecole} n'a pas d'informations renseignées dans ecoels.json")
        print('\t"', ecole, '":{},', sep="") # On affiche les lignes à rajouter dans ecoles.json si l'école n'est pas présente
        ecole_conf = {}
    else:
        ecole_conf = ecoles_conf[ecole]

    if "Ville" in ecole_conf.keys():
        markdown += f" ({ecole_conf['Ville']})"

    if "Places" in ecole_conf.keys():
        markdown += f" - ({ecole_conf['Places']}) places"
    markdown += "\n\n"

    return markdown

def format_temoignage(categorie, temoignage):
    markdown = temoignage[categorie].strip()
    markdown += "{{< right >}}*"
    markdown += temoignage["Speudo"].strip()

    if temoignage["Contact"].strip() != "":
        markdown += f" ({temoignage['Contact'].strip()})"

    markdown += "*{{< /right >}}"

    return markdown

def main():
    markdown = ""
    with open('header.md', 'r') as fichier:
        markdown += fichier.read()

    temoignages = []
    with open('temoignages.json') as json_file:
        fichier = json.load(json_file)
        questions = fichier["questions"]

        for temoignage in fichier["responses"]:
            tem = {}
            for question, reponse in temoignage.items():
                if question in questions.keys():
                    tem[questions[question]] = reponse.strip()
            temoignages.append(tem)

    ecoles_conf = {}
    with open('ecoles.json') as json_file:
        ecoles_conf = json.load(json_file)

    par_ecoles = {}
    for temoignage in temoignages:
        ecole = temoignage["Ecole"]
        if not ecole in par_ecoles.keys():
            par_ecoles[ecole] = []
        par_ecoles[ecole].append(temoignage)

    for ecole in sorted(list(par_ecoles.keys())):
        markdown += format_ecole(ecoles_conf, ecole)

        eleves = par_ecoles[ecole]

        markdown += '{{< admonition tip "Points positifs" false >}}\n'
        for eleve in eleves:
            markdown += format_temoignage("Positif", eleve)
        markdown += '{{< /admonition>}}'

        markdown += '{{< admonition warning "Points négatifs" false >}}\n'
        for eleve in eleves:
            markdown += format_temoignage("Negatif", eleve)
        markdown += '{{< /admonition>}}'

    with open('footer.md', 'r') as fichier:
        markdown += fichier.read()

    with open("../../content/pages/scei.md", "w+") as fichier:
        fichier.write(markdown)

if __name__ == "__main__":
    main()
