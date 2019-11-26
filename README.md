# Attempt the Fake News Challenge
*UniGe Project Academic memory work.*

A proposal to use Stance detection to better anticipate Fake News.

## short abstract

This thesis is a proposal to improve the results of the [Fake news Challenge](http://www.fakenewschallenge.org/).

My proposal is a ensemble learning neural network from the winning systems of the FNC.

Read the memoir [here](https://github.com/poggioenzo/memoir_true/blob/master/memoir.pdf)

---
# Tenter la Fake News Challenge

## Une proposition d’utilisation de la Stance Detection pour mieux anticiper le phénomène des Fake News

### Enzo Poggio

### Superviseuse: Pr. Paola Merlo

#### Faculté des Lettres

#### Université de Genève Mai 2018

### Résumé

Dans ce mémoire nous apportons des réponses à ces questions : y a-t-il une bonne définition des
fausses nouvelles (Fake News)? Peut-on parler deFake Newsde manière objective? Qu’implique le
termeFake News? D’ou proviennent ces fameusesFake Newset que font-elles? Et pourquoi est-ce
important d’en parler?
Puis nous présentons un bref état actuel de laStance Detection. Nous montrons comment elle peut
être utile pour détecter lesFake Newsen présentant deux tâches, à savoir la SemEval-2016 Task 6 et la
Fake News Challenge.
Enfin nous présentons et discutons nos propres résultats à laFake News Challenge(dont certains
dépassent l’état de l’art) et notre utilisation des combinaisons de modèles et de l’apprentissage par
ensemble.

## Table des matières

- 1 Introduction : Qu’est-ce qu’uneFake News? Liste des tableaux xiii
   - 1.1 Vers une définition du concept deFake News.
      - 1.1.1 Produire desFake News; une intention de tromper
      - 1.1.2 Limites de la définition
   - 1.2 Pourquoi produire desFake News?
      - 1.2.1 Le contexte desFake News.
      - 1.2.2 Le système monétaire desFake News
      - 1.2.3 Raisons idéologiques
   - 1.3 Les origines desFake News.
      - 1.3.1 Des médias négligents
      - 1.3.2 Des organisations malveillantes internationales
   - 1.4 La propagation desFake News
      - 1.4.1 Les réseaux sociaux : médiations desFake News
      - 1.4.2 Le biais de confirmation
      - 1.4.3 Tri de l’information selon Kahneman
   - 1.5 Les risques desFake News
      - 1.5.1 Les risques politiques
      - 1.5.2 Les risques sanitaires
      - 1.5.3 Détournement des news vers des sujets clivants
   - 1.6 Légitimité du projet et motivations
   - 1.7 Comment détecter uneFake News?
      - 1.7.1 Comment vérifier des informations?
      - 1.7.2 Méthode informatique actuelle :Stance Detection.
- 2 État de l’art :Stance Detection
   - 2.1 Vers une définition
      - 2.1.1 Formalisation de laStance Detection
      - 2.1.2 Domaine de laStance Detection
      - 2.1.3 La genèse de laStance Detection.
      - 2.1.4 Application générale et relative auFake News. x Table des matières
   - 2.2 SemEval-2016 Task
      - 2.2.1 Description générale de la tâche
      - 2.2.2 Les participants
   - 2.3 Fake News Challenge
      - 2.3.1 Description générale de la tâche
      - 2.3.2 Solat in the Swen[5]
      - 2.3.3 Athene (UKP Lab)[15]
      - 2.3.4 UCL Machine reading[22]
      - 2.3.5 Discussion comparative des modèles et des résultats
- 3 Recherches et résultats
   - 3.1 Analyse des résultats des participants et création d’hypothèses
      - 3.1.1 Un aperçu de l’ensemble de test
   - 3.2 Les résultats et les scores des participants
      - 3.2.1 Solat in the Swen
      - 3.2.2 Le système Athene
      - 3.2.3 UCL Machine Reader
   - 3.3 Analyses et hypothèses
   - 3.4 Modèles par combinaison : le vote de majorité
      - 3.4.1 Explication du modèle
      - 3.4.2 Les résultats des votes de majorité
   - 3.5 Modèles par combinaison : par moyenne
      - 3.5.1 Modèles utilisant un50/50 weighted average
      - 3.5.2 Résultats
   - 3.6 Apprentissage par ensemble :Single Layer Learner
      - 3.6.1 Légitimation de l’apprentissage par ensemble
      - 3.6.2 Explication du modèle
      - 3.6.3 Résultats
   - 3.7 Discussions
- 4 Conclusions
- Bibliographie
- Annexe A Les soumissions complètes des gagnants du FNC


### Remerciements

J’aimerais remercier en premier lieu l’Université de Genève, ma superviseuse, la Professeure Paola
Merlo et les membres de mon jury.
J’aimerais remercier pour leurs nombreuses relectures, corrections et conseils ma mère, Édith
Certain, mon ami, David Burkhard et mon amie, Alice Badel.
Pour leurs précieux conseils sur lateX, en math et en rédaction, je remercie mes amis Allan Fries,
Miguel Van Vlasselaer, Sahar Al Jalbout et Timothée Premat.
Enfin pour m’avoir aidé à garder le moral tout au long de la rédaction je remercie mes amis
Delphine Vidal et Léandre Phillippon.
Pour m’avoir aidé à décompresser, je remercie toutes les personnes du Centre Saint-Boniface.
Et pour les nombreuses inspirations sceptiques, je souhaite remercier les propriétaires des chaînes
Youtube suivantes : Aude WTFake, Esprit Critique, Hygiène Mental, Instant Sceptique, La statistique
expliquée à mon chat, La Tronche en Biais, Le Pharmacien, Mycéliums, Officiel DEFAKATOR,
Sciences4All, Un Monde Riant et Les Shadoks : Shadok Tube.
