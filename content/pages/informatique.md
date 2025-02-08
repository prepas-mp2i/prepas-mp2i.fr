---
title: Les cours d'informatique en MP2I et MPI
subtitle: Une brève introduction à cette matière magique !
url: /informatique
date: 2021-12-20T00:07:18+01:00
tags:
    - lycéens
categories:
    - MP2I/MPI
menu:
    main:
        name: Informatique
        weight: 2
---

Qui dit nouvelle filière, dit nouveaux professeurs et nouveaux cours.
Vous vous demandez sûrement en quoi consiste le cours d'informatique en MP2I et MPI, et bien cette page est là pour vous éclairer !

{{< admonition info "Programme complet d'informatique" true >}}
Vous pouvez le télécharger [en cliquant ici](/documents/informatique_mp2i_et_mpi.pdf).
{{< /admonition >}}

## Répartition horaire

| Année | Cours | Travaux Dirigés | Travaux Pratiques |
|:-----:|:-----:|:---------------:|:-----------------:|
| MP2I・semestre I | 2h | 1h | 1h |
| MP2I・semestre II</br>*Voie Informatique* | 4h | 1h | 1h |
| MPI | 4h | 1h | 1h |

{{< admonition tip "MP2I・Second semestre : Voie SI" true >}}
Les élèves choisissant de se réorienter vers la SI au second semestre de MP2I n'auront plus qu'**1h30 d'informatique tronc commun** par semaine.
{{< /admonition >}}

- **Cours** : cours théorique en classe entière, comme pour les mathématiques par exemple.
- **Travaux Dirigés (TD)** : exercices en demi-groupe, où l'objectif est de pratiquer pour maîtriser les concepts et progresser.
- **Travaux Pratiques (TP)** : travaux sur machine pour implémenter ce que vous avez vu en cours : c'est là qu'on code !

Remarquez que ce nombre d'heures peut varier : il n'est pas rare qu'un professeur d'informatique rajoute des heures de TP pour vous faire pratiquer un peu plus en début d'année par exemple !

## La théorie

La première chose à comprendre est que ce cours d'informatique est principalement **théorique**.

Beaucoup des notions abordées font d'ailleurs plus précisément partie de l'*algorithmique*, c'est-à-dire l'étude des algorithmes.

Un premier critère pour savoir si cette filière est faite pour vous est donc :
*Est-ce que j'aime les mathématiques ?*

### Programme en MP2I

| Thème général | Domaine étudié | Semestre |
|:-------------:|:--------------:|:--------:|
| **Méthodes de programmation** | Algorithmes et programmes | 1 |
| 〃 | Discipline de programmation | 1 & 2 |
| 〃 | Validation, test | 1 |
| **Récursivité et induction** | - | 1 & 2 |
| **Structures de données** | Types et abstraction | 1 |
| 〃 | Structures de données séquentielles | 1 & 2 |
| 〃 | Structures de données hiérarchiques | 2 |
| 〃 | Structures de données relationnelles | 2 |
| **Algorithmique** | Exploration exhaustive | 2 |
| 〃 | Décomposition d'un problème en sous-problèmes | 2 |
| 〃 | Algorithmique des textes | 2 |
| 〃 | Algorithmique des graphes | 2 |
| **Gestion des ressources de la machine** | Gestion de la mémoire d'un programme | 1 |
| 〃 | Gestion des fichiers et entrées-sorties | 1 |
| **Logique** | Syntaxe des formules logiques | 2 |
| 〃 | Sémantique de vérité du calcul propositionnel | 2 |
| **Bases de données** | - | 2 |

### Programme en MPI

| Thème général | Domaine étudié |
|:-------------:|:--------------:|
| **Méthodes de programmation** | Discipline de programmation |
| **Structures de données** | Structures de données hiérarchiques |
| **Algorithmique** | Algorithmes probabilistes, algorithmes d’approximation |
| 〃 | Exploration exhaustive |
| 〃 | Décomposition d'un problème en sous-problèmes |
| 〃 | Algorithmique des graphes |
| 〃 | Algorithmique pour l’intelligence artificielle et l’étude des jeux |
| **Gestion des ressources de la machine** | Gestion de la concurrence et de la synchronisation |
| **Logique** | Déduction naturelle |
| **Langages formels** | Langages réguliers |
| 〃 | Automates finis |
| 〃 | Grammaires non contextuelles |
| **Décidabilité et classes de complexité** | - |

## La pratique

Le but principal des TP est de faire fonctionner un algorithme étudié en cours (avant ou après) sur un ordinateur, et de créer de nouveaux algorithmes pour des tâches connexes.

### Langages de programmation

Pendant les TP, la programmation se fait en **C**  et en **OCaml**.

{{< center >}}
{{< image src="/images/logo_C.svg" width="10%" >}}
{{< image src="/images/logo_Ocaml.svg" width="36%" >}}
{{< /center >}}
> Retrouvez la documentation en ligne du [C](https://devdocs.io/c/) ainsi que le site [OCaml](https://ocaml.org/).

On utilise quelquefois **Python** lors de TP de physique, mais c'est davantage une compétence de traitement de données que des algorithmes complexes.

### Exemples

Voici un exemple classique de tâche pour lequel on va construire un algorithme : calculer les termes de la [suite de Fibonacci](https://fr.wikipedia.org/wiki/Suite_de_Fibonacci). Pour rappel, les premiers termes de cette suite valent 0 et 1, puis on construit le terme suivant en additionnant les deux précédents.

#### En Python

Dans le chapitre récursivité, vous avez vraisemblablement déjà rencontré la suite de Fibonacci.

```python
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)
    
# On pourrait omettre les "else" mais ils peuvent aider à la compréhension.
```

#### En OCaml

En "traduisant" simplement la syntaxe :

```ocaml
let rec fibo n = 
    if n = 0 then 0
    else if n = 1 then 1
    else fibo (n-1) + fibo (n-2) 
    
(* Les parenthèses ne sont pas systématiques en OCaml. 
   On doit les utiliser lorsque notre expression n'est pas associative, 
   pour dissocier les différents cas. 
   Ici, nous voulons bien passer n-1 en paramètre, 
   et non faire fibo n puis décrémenter le résultat. *)
```

{{< newline >}}

Cependant, le [pattern matching](https://ocaml.org/learn/tutorials/a_first_hour_with_ocaml.html#Pattern-matching) permet d'obtenir une écriture plus élégante pour ce genre de codes ; il est également possible de préciser le type des paramètres utilisés ainsi que celui de l'expression renvoyée.

(*Il existe quelque chose de ressemblant en python, mais ça n'est que du sucre syntaxique*)

Ces optimisations syntaxiques permettent de déceler plus vite une incohérence, et donc de produire un code plus sécurisé en s'assurant qu'il réalise exactement ce que l'on veut. On dit qu'OCaml est [fortement typé](https://fr.wikipedia.org/wiki/Typage_fort).

```ocaml
(* La fonction fibo prend en paramètre un entier n, et renverra aussi un entier. *)
let rec fibo (n:int) : int = 
    match n with 
    (* On filtre la variable n. 
       Si la valeur ne correspond pas au filtre, on passe au filtre suivant. *)
    | 0 -> 0 (* Première valeur de la suite de fibonnaci *)
    | 1 -> 1 (* Deuxième valeur *)
    | n -> fibo (n-1) + fibo (n-2) 
    (* Ce filtre prend toute valeur de n, il permet d'effectuer un filtrage exhaustif.
       En conséquent, aucun autre filtre suivant ne sera pris en compte. *)
```

</br>
Vous verrez, quand vous aurez pratiqué ce langage, vous trouverez que son écriture est très proche de sa définition mathématique !
<!-- TODO: Remplacer ou ajouter un exemple en OCaml plus simple, permettant d'introduire le langage de façon moins violente, une proposition avancée est l'utilisation d'une suite arithmético-géométrique. -->

Cependant, comme vous le verrez en cours, les algorithmes précédents sont peu efficaces, car ils calculent de nombreuses fois les mêmes termes (donc ils deviennent très vite lents lorsque la taille de l'entrée augmente) et peuvent finir par faire "exploser la pile d'appel".

Afin de réduire la quantité de mémoire utilisée par le programme, il est possible d’appliquer le principe de [récursivité terminale](https://pcaboche.developpez.com/article/programmation-fonctionnelle/recursivite-terminale/), comme le fait l'exemple ci-dessous :

```ocaml
let fibo (n:int) : int =
    (* On crée une fonction auxiliaire pour stocker les valeurs de la suite *)
    let rec aux i f1 f2 = 
        match i with
            | 0 -> f1
            | 1 -> f2
            | _ -> aux (i - 1) f2 (f1 + f2)
    in aux n 0 1 (* Et on renvoie sa valeur ici *)
```
<!-- C'est peut-être un peu plus intuitif et représentatif des optimisations que peut faire le compilateur en termes d'OCaml récursif -->

{{< newline >}}
Dans le programme ci-dessus, chaque valeur de la suite est calculée une seule fois, et est stockée dans les arguments de la fonction auxiliaire. Cela nous permet d'atteindre une [complexité linéaire](https://cahier-de-prepa.fr/psi-michelet/download?id=239) en réduisant le nombre d'opérations effectuées par la fonction.

#### En C

Dans la même idée, il est possible d'écrire cette même fonction dans le langage C :

```c
int fibo(int n)
{
    /* En C, un double égal permet de comparer deux valeurs. 
     * Un simple égal est considéré comme une assignation.
     * Des parenthèses sont nécessaires autour de chaque expression logique. 
     */
    if (n == 0)      // On peut omettre les accolades si il y a qu'une seule expression dans le bloc
        return 0;
    else if (n == 1) // Pareil qu'en Python, on peut aussi omettre les else ici
        return 1; 
    else
        return fibo(n - 1) + fibo(n - 2);
}
```

Ici, chaque appel à la fonction `fibo` recalcule chaque valeur de la suite, ce qui augmente l'usage en mémoire et la complexité du programme. Il est possible d'appliquer le même principe de récursivité terminale en C, avec le coût ajouté des arguments supplémentaires dans la signature de la fonction (il est impossible de définir des fonctions dans les fonctions en C).

Si on cherche à l'optimiser un peu en appliquant la récursivité terminale, ça donnerait :

```c
int fibo(int n, int n0, int n1)
{
    if (n == 0)
        return n0;
    if (n == 1)
        return n1;
    return fibo(n-1, n1, n0+n1);
}

/* Ne vous souciez pas de ce que contient cette fonction, 
 * vous verrez tous les détails du fonctionnement du langage en cours :) 
 */
int main()
{
    int fibo10 = fibo(10, 0, 1); /* Correspond au premier appel récursif en OCaml */
    return 0;
}
```

{{< newline >}}
Bien sûr, il est toujours possible d'aller un peu plus loin et de s'amuser avec le côté obscur de l'informatique :

```c
long int fibo(int n)
{ 
    int a = 0, b = 1;
    for (int i=0; i<n; i++){
        a+=b;
        a^=b;
        b^=a;
        a^=b;
    }   
    return a;
}
```

Ce code est en fait basé sur un [XOR swap](https://en.wikipedia.org/wiki/XOR_swap_algorithm). Comme quoi, on peut s'amuser en MP2I/MPI, même avec une tâche aussi simple !

Ne prenez pas peur si vous ne savez écrire dans aucun de ces langages, leurs compilateurs respectifs vous accompagneront tout du long en vous indiquant les erreurs et comment les corriger :wink:
