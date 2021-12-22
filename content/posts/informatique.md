---
title: "Les cours d'informatique en MP2I"
date: 2021-12-21
draft: false
---

Qui dit nouvelle filière, dit nouveaux professeurs et nouveaux cours.

Vous vous demandez surement en quoi consiste le cours d'informatique en MP2I, et bien cette page est là pour vous éclairer !


Nous avons 2h de TP par semaine ainsi que 2h de théorie qui nous servent à étudier les algorithmes de manière formelle.

## Répartition horaire

* Au premier semestre, les cours d'info sont composés de 2h de cours, 1h de *TP* et 1h de *TD*
* Si vous choisissez de continuer l'informatique, vous aurez 2h de cours supplémentaire (ce qui fait 4h de cours au second semestre et en 2eme année) 

> *Cours* : cours théorique en classe entière, comme en maths.

> *TD* : exercices en demi classe, où l'objectif est de pratiquer pour maitriser les concepts et progresser

> *TP* : travail sur machine pour implémenter ce que vous avez vu en cours: c'est là où on code !

Remarquez que ce nombre d'heures peut varier: ce n'est pas rare qu'un prof d'informatique rajoute des heures de TP pour vous faire plus pratiquer au début d'année par exemple !


## La théorie

La première chose à comprendre est que ce cours d'informatique est principalement **théorique**.

La plupart des notions abordées font d'ailleurs plus précisément partie de l'*algorithmique*, c'est à dire l'étude des algorithmes.

Un premier critère pour savoir si cette filière est faite pour vous est donc: 
> Est-ce que j'aime les maths ?

Voici les principaux domaines pouvant être abordés en première année:
- systèmes formels et logique
- structures de données
- analyse d'algorithmes
- bases de données
- gestion des ressources


## La pratique

Pendant les TP, la programmation se fait en C et en Ocaml.

On utilise quelquefois Python lors de TP de physique, mais c'est d'avantage une compétence de traitement de données que des algorithmes complexes.


Le but principal des TP est de faire fonctionner un algorithme étudié en cours (avant ou après) sur un ordinateur, et de créer de nouveaux algorithmes pour des tâches connexes.

Voici un exemple classique de tâche pour lequel on va construire un algorithme:

Calculer la [suite de Fibonacci](https://fr.wikipedia.org/wiki/Suite_de_Fibonacci)

### première approche en python:

Si vous aimez l'informatique, vous êtes probablement à l'aise avec le code suivant:

```python
def fibo(n):
    if n < 2:
        return n
    return fibo(n-1, n-2)
```

Mais comme vous le verrez en cours, cette fonction est très peu efficace car elle calcule de nombreuses fois les mêmes termes et fait "exploser sa pile d'appel"


### une meilleure approche en ocaml
```ocaml
let rec fibo(n) = match n with
  | 0 -> (0, 1)
  | _ -> let a, b = fibo(n-1) in (b, a+b)
```

Vous verrez, quand vous aurez pratiqué ce langage, vous trouverez que son écriture est très proche de sa définition mathématique !!!


### un code incompréhensible en c:

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

Comme quoi on peut s'amuser en MP2I, même avec une tâche aussi simple !


## Liens annexes

Vous pouvez retrouver le programme complet d'informatique à [cette adresse](https://cache.media.education.gouv.fr/file/SPE1-MEN-MESRI-4-2-2021/64/6/spe777_annexe_1373646.pdf).
