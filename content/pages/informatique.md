---
title: Les cours d'informatique en MP2I
subtitle: Une brève introduction
date: 2021-12-20T00:07:18+01:00
---

Qui dit nouvelle filière, dit nouveaux professeurs et nouveaux cours.
Vous vous demandez surement en quoi consiste le cours d'informatique en MP2I, et bien cette page est là pour vous éclairer !

## Répartition horaire

* Au premier semestre, les cours d'info sont composés de 2h de cours, 1h de *TP* et 1h de *TD*
* Si vous choisissez de continuer l'informatique, vous aurez 2h de cours supplémentaire (ce qui fait 4h de cours au second semestre et en 2ᵉ année)

{{< admonition info "Répartition horaire" true >}}
**Cours** : cours théorique en classe entière, comme en maths.

**TD** : exercices en demi groupe, où l'objectif est de pratiquer pour maitriser les concepts et progresser

**TP** : travail sur machine pour implémenter ce que vous avez vu en cours: c'est là où on code !
{{< /admonition >}}

Remarquez que ce nombre d'heures peut varier : ce n'est pas rare qu'un prof d'informatique rajoute des heures de TP pour vous faire plus pratiquer en début d'année par exemple !

## La théorie

La première chose à comprendre est que ce cours d'informatique est principalement **théorique**.

La plupart des notions abordées font d'ailleurs plus précisément partie de l'*algorithmique*, c'est-à-dire l'étude des algorithmes.

Un premier critère pour savoir si cette filière est faite pour vous est donc :
*Est-ce que j'aime les maths ?*

Voici les principaux domaines pouvant être abordés en première année :

* Systèmes formels et logique
* Structures de données
* Analyse et conception d'algorithmes
* Bases de données
* Gestion des ressources

## La pratique

Pendant les TP, la programmation se fait en C et en Ocaml.

On utilise quelquefois Python lors de TP de physique, mais c'est davantage une compétence de traitement de données que des algorithmes complexes.

Le but principal des TP est de faire fonctionner un algorithme étudié en cours (avant ou après) sur un ordinateur, et de créer de nouveaux algorithmes pour des tâches connexes.

Voici un exemple classique de tâche pour lequel on va construire un algorithme:

Calculer les termes de la [suite de Fibonacci](https://fr.wikipedia.org/wiki/Suite_de_Fibonacci).

### En Python

Dans le chapitre récursivité, vous avez vraisemblablement déjà rencontré la suite de Fibonacci.

```python
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2) # On pourrait omettre les "else" mais ils peuvent aider à la compréhension.
```

### En OCaml

En "traduisant" simplement la syntaxe :

```ocaml
let rec fibo n = 
    if n = 0 then 0
    else if n = 1 then 1
    else fibo (n-1) + fibo (n-2) 
    (* Les parenthèses ne sont pas systématiques en OCaml. 
       On doit les utiliser lorsque notre expression n'est pas associative, pour dissocier les différents cas. 
       (ici nous voulons bien passer n-1 en paramètre, et non faire fibo n puis décrémenter le résultat.)*)
```

On pourrait rendre cela plus élégant en utilisant le [pattern matching](https://ocaml.org/learn/tutorials/a_first_hour_with_ocaml.html#Pattern-matching) et rendre le tout plus propre en précisant le type des paramètres utilisé ainsi que le type de l'expression renvoyée. (Il existe quelque chose de ressemblant en python, mais ça n'est que du sucre syntaxique).

Cela permet de déceler plus vite une incohérence, et donc de produire un code plus sécurisé et apte à réaliser exactement ce que l'on veut. On dit qu'OCaml est [fortement typé](https://fr.wikipedia.org/wiki/Typage_fort).

```ocaml
(* La fonction fibo prend en paramètre un entier n, et renverra aussi un entier. *)
let rec fibo (n:int) : int = 
    match n with 
    (* On filtre la variable n. 
       Si la valeur ne correspond pas au filtre, on passe au filtre suivant. *)
    | 0 -> 0 (* première valeur de la suite de fibonnaci *)
    | 1 -> 1 (* deuxième valeur *)
    | n -> fibo (n-1) + fibo (n-2) 
    (* Ce filtre prend toute valeur de n, il permet d'effectuer un filtrage exhaustif.
       En conséquent, aucun autre filtre suivant ne sera pris en compte. *)
```

Vous verrez, quand vous aurez pratiqué ce langage, vous trouverez que son écriture est très proche de sa définition mathématique !
<!-- TODO: Remplacer ou ajouter un exemple en OCaml plus simple, permettant d'introduire le langage de façon moins violente, une proposition avancée est l'utilisation d'une suite arithmético-géométrique. -->

### Une optimisation

Comme vous le verrez en cours, les algorithmes précédents sont peu efficaces, car ils calculent de nombreuses fois les mêmes termes (deviennent très vite lents lorsque la taille de l'entrée augmente) et peuvent finir par faire "exploser la pile d'appel".

Afin de réduire la quantité de mémoire utilisée par le programme, il est possible d'appiquer le principe de [récursivité terminale](https://pcaboche.developpez.com/article/programmation-fonctionnelle/recursivite-terminale/), comme le fait l'exemple ci-dessous :

```ocaml
let fibo (n: int): int =
    (* On crée une fonction auxiliaire pour stocker les valeurs de la suite *)
    let rec aux i f1 f2 = 
        match i with
            | 0 -> f1
            | 1 -> f2
            | _ -> aux (i - 1) f2 (f1 + f2)
    in aux n 0 1 (* Et on renvoie sa valeur ici *)
```
<!-- C'est peut-être un peu plus intuitif et représentatif des optimisations que peut faire le compilateur en termes d'OCaml récursif -->

Dans le programme ci-dessus, chaque valeur de la suite est calculé une seule fois, et est stocké dans les arguments de la fonction auxiliaire. Cela nous permet d'atteindre une [complexité linéaire](https://cahier-de-prepa.fr/psi-michelet/download?id=239) en réduisant le nombre d'opérations effectuées par la fonction.

### En C

Dans la même idée, il est possible d'écrire cette même fonction dans le langage C :

```c
int fibo(int n)
{
    /* En C, un double égal permet de comparer deux valeurs. Un simple égal est considéré comme une assignation.
    Des parenthèses sont nécéssaires autour de chaque expression logique. */
    if (n == 0) /* On peut omettre les accolades si il y a qu'une seule expression dans le bloc */
        return 0;
    else if (n == 1) /* Pareil qu'en Python, on peut aussi omettre les else ici */
        return 1; 
    else
        return fibo(n - 1) + fibo(n - 2);
}

/* fonction main */
```

Ici, chaque appel à la fonction `fibo` recalcule chaque valeur de la suite, ce qui augmente l'usage en mémoire et la complexité du programme. Il est possible d'appliquer le même principe de récursivité terminale en C, avec le coût ajouté des arguments supplémentaires dans la signature de la fonction (il est impossible de définir des fonctions dans les fonctions en C). Si on cherche à l'optimiser un peu en appliquant la récursivité terminale, ça donnerait :

```c
int fibo(int n, int n0, int n1)
{
    if (n == 0)
        return n0;
    if (n == 1)
        return n1;
    return fibo(n - 1, n1, n0 + n1);
}

/* Ne vous souciez pas de ce que contient cette fonction, vous verrez tous les détails du fonctionnement du langage en cours :) */
int main()
{
    int fibo10 = fibo(10, 0, 1); /* On appellerait cette fonction comme la fonction auxiliaire dans l'implémentation récursive en OCaml */
    
    return 0;
}
```

Bien sûr, il est toujours possible d'aller un peu plus loin et de s'amuser avec le côté obscur de l'informatique :

```c
long int fibo(int n){ 
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

Ce code est en fait basé sur un [XOR swap](https://en.wikipedia.org/wiki/XOR_swap_algorithm).
Comme quoi, on peut s'amuser en MP2I, même avec une tâche aussi simple !

Ne prenez pas peur si vous ne savez écrire dans aucun de ces langages, leurs compilateurs respectifs vous accompagneront tout du long en vous indiquant les erreurs et comment les corriger :)

{{< admonition tip "Liens annexes" true >}}
Vous pouvez télécharger le programme complet d'informatique [en cliquant ici](/documents/informatique_mp2i_et_mpi.pdf).
{{< /admonition >}}
