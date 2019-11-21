 

[Tenter la *Fake News Challenge*.\
[Une proposition d’utilisation de la *Stance detection* pour mieux
anticiper les *Fake News*. ]{} ]{}

[Enzo POGGIO ]{}

Ce mémoire est le travail final du\
Master d’informatique pour sciences humaines\
de la\
Faculté des Lettres\
Université de Genève

Superviseuse: Professeure Paola Merlo

Mai 2018

Fake News; un problème?
=======================

faire une introductionà l’intro

Qu’est-ce qu’une Fake News?
---------------------------

### Définition d’une Fake News.

#### Produire des Fake News; une intention de tromper.

Un énoncé peut être vrai ou faux. Il est vrai : s’il est en adéquation
avec le monde. Il est faux : s’il ne correspond pas à la réalité. Les
nouvelles (news) sont des énoncés. Est-ce que l’énoncé J’aime les
tartes. est une news ? Non, toutes les news sont des énoncés; mais seul
certains énoncés sont des news. Des journalistes ont fait une liste non
exhaustive des critères d’une news ([Tony Harcup et Deirdre O’Neill,
2016](http://www.tandfonline.com/doi/full/10.1080/1461670X.2016.1150193)).
La news est une histoire d’une personne de pouvoir ou célèbre. Elle est
parfois une bonne ou une mauvaise nouvelle. Souvent elle est une
surprise ou un phénomène qui concerne beaucoup de personnes. Certaines
sont juste des suivis, des divertissements ou des faits divers. En
somme, retenons qu’une nouvelle est une histoire en lien avec la
réalité. Ce qui nous intéresse c’est sa véracité selon l’interprétation
du monde réel. Cependant, leurs sujets sont variés, mais ce n’est pas
pertinent pour nous. De manière, plus générale une nouvelle est une
histoire relayée par un média.

L’erreur est une opinion, un jugement ou une information non conforme
avec la réalité ou la vérité. L’erreur est inconsciente. Elle n’est pas
faite exprès. Celle-ci démasquée, elle tend à être corrigée. Une
nouvelle erronée est donc une histoire médiatisée qui n’est pas vraie.
Elle ne correspond pas à la vérité. La nouvelle erronée est due à une
erreur scientifique ou bien une erreur journalistique. C’est-à-dire une
mauvaise manipulation de l’information par l’un de ces deux corps. Les
médias précautionneux corrigent leurs nouvelles erronées par des
articles de démenti. Ceci devrait être le code de déontologie des
journalistes pour l’honnêteté intellectuelle. Une Fake News[^1] n’est
pas une nouvelle erronée. Cependant elles sont souvent confondues.

Parfois des nouvelles sont volontairement erronées. On dit alors
qu’elles sont fausses. Il faut distinguer deux types de fausses
nouvelles. Le point important ici est l’intention derrière.

Les fausses nouvelles dans un but bien-veillant s’appellent satire ou
information parodique. Ces parodies imitent les médias. Ils volent même
jusqu’à leur nom parfois (le Gorafi est l’anagramme du Figaro). Mais au
lieu de diffuser de vraies informations, les parodies proposent un
contenu décalé, sarcastique ou canularesque. Le but premier de ce genre
de nouvelle est le divertissement. Même si l’on trompe le lecteur, on ne
cherche pas à lui nuire mais plutôt à le faire rire. Enfin il y a
toujours des exceptions où l’information semble tellement crédible
qu’elle est ensuite utilisée comme source fiable. Les parodies donnent
des informations délibérément fausses. La tromperie est totalement
assumée et même souvent revendiquée.

Les fausses nouvelles dans le but de volontairement tromper sont ce que
l’on appelle Fake News. Elle se distingue de l’erreur car elle n’est pas
le produit du hasard ou d’une mauvaise manipulation. Et elle se
distingue de la satire et de la parodie car elle n’est ni assumée ni
revendiquée fausse. La Fake News provient d’un ensemble de médias. Elle
participe à la désinformation via les médias et les réseaux sociaux.
Souvent, les Fake News sont écrites par des anonymes difficilement
contestables et calomniables.

#### Limites de la définition.

Certes une erreur peut arriver dans le traitement ou la création de
l’information. Mais ces erreurs sont-elles légitimes ? La science
progresse en faisant des erreurs. D’ailleurs, dans la définition de
l’étude scientifique l’erreur joue un rôle important. L’étude
scientifique est la recherche perpétuelle de l’erreur. À défaut de nous
apprendre ce qu’est la vérité, la science nous montre ce qu’elle n’est
pas. Donc l’erreur scientifique est légitime au bon fonctionnement de la
science. Peut-on en dire autant de l’erreur journalistique ? Le
journaliste doit faire un compte rendu exhaustif, objectif et
vraisemblable du sujet qu’il traite. Si une erreur non scientifique
vient se faufiler dans son article c’est qu’il a mal fait son travail.

Par exemple, on voit toujours des médias relayer l’information que les
vaccins causent l’autisme chez l’enfant. Cette croyance persiste après
une publication d’Andrew Wakefield [^2]. Cette publication fut démentie
des centaines de fois par des autorités compétentes, mais les médias de
grande audience relayent toujours ce message de méfiance vaccinale. Le
devoir du journaliste n’est alors pas respecter . Les médias
traditionnels entretiennent le discours erroné des antivax [^3].
Celui-ci fait s’écouler beaucoup d’encre. Mais cette controverse est de
la désinformation pure et d’une grande malhonnêteté intellectuelle.

### Pourquoi produire des Fake News?

#### Le contexte des Fake News.

L’invention qui a le plus contribué à l’essor des médias est
certainement l’imprimerie. Elle nous fait passer des histoires orales à
la presse. L’information est figée sur du papier. Elle n’est plus perdue
ou transformée par le locuteur de l’histoire. À partir de ces documents,
on peut faire des versions officielles et approuvées par une autorité.
L’information fut pendant très longtemps partagée de manière verticale.
La source d’autorité de la connaissance était plus ou moins légitime et
compétente. La connaissance était donnée par les médias et leur vision.
Il n’y avait pas de sources contestataires.

Puis fut créé internet ! Internet permet un partage des connaissances
horizontal. Tout le monde disposant d’une connexion au réseau peut
participer à la connaissance générale. Chacun peut écrire, partager et
relayer des informations. Les médias se sont développé sur internet et
surtout ils s’y sont multipliés. La pluralité du web qui permet de mieux
recroiser ses sources. Nous ne sommes plus dans la vision dogmatique des
grands groupes qui possèdent les chaînes télévisuelles.

Nous avons acquis une énorme liberté d’expression avec l’avènement
d’internet comme média souverain de la pluralité. Mais ce nouveau régime
pluriel a aussi des désavantages. La démocratie de la connaissance
permet aux profanes de s’exprimer sur des sujets de pointe. Ainsi,
nombreux sont les opinions et les préjugés qui sont travestis en
pseudo-vérités. La liberté d’expression et la facilité d’accès à
internet participent grandement à la désinformation globale.

De plus la multiplicité qu’engendre internet pose un problème à notre
compréhension du monde. En effet comme le dit Michael Lynch, internet
c’est connaître plus et comprendre moins \[...\][^4]. M. Lynch conteste
la notion largement acceptée qu’internet est un avantage parce qu’il
rend plus d’informations disponibles à plus de gens plus rapidement et
facilement.

#### Le système monétaire des Fake News.

Le clickbait désigne un contenu web qui vise à attirer le maximum de
passages d’internautes afin de générer des revenus publicitaires en
ligne. Le clickbait affiche des gros titres racoleurs. Il est souvent
mensonger et sensationnel. L’exactitude et les sources de l’article sont
inexistantes. Le but du clikbait est d’être partagé massivement sur les
réseaux sociaux.

Maintenant que la presse virtuelle est multiple, pour être rentable,
elle doit générer une offre publicitaire non négligeable. Le clickbait
est un effet pervers d’internet. Les possesseurs de contenu peuvent
gagner de l’argent par le biais de la publicité. Cela crée des nouveaux
systèmes monétaires.

Les Fake News et le clickbait associés répondent à la crise profonde de
la presse papier au profit des réseaux sociaux comme médias. De plus les
Fake News alimentent une méfiance envers les médias traditionnels. Elles
font croire avec leurs faits alternatifsqu’on tente de cacher quelque
chose à la population.

#### Raisons idéologiques.

Les raisons idéologiques de produire des Fake News ne manquent pas. En
particulier en politique, où elles sont utilisées à tout va. Un exemple
probant est le Pizzagate. En résumé le Pizzagate est une
théorieconspirationniste prétendant qu’il existe un réseau de pédophilie
autour de John Podesta, l’ancien directeur de campagne d’Hillary
Clinton. Cette histoire fut rapidement démentie par les services de
police et une majorité des médias américains. Mais les conséquences ne
sont pas négligeables. Un fusillade, heureusement sans blessé, a eu lieu
dans la pizzeria où étaient soi-disant séquestrés les enfants du réseau
pédophile de Podesta.

### Les origines des Fake News.

#### Des médias négligents.

La négligence et l’unicité des médias fait que les Fake News peuvent se
propager facilement. Comme nous l’avons dit précédemment, les médias
traditionnels traversent une crise. La production de contenus doit être
faites le plus rapidement possible. Dans le but de répondre à la course
à l’information de plus en plus grande et déloyale, la qualité des
articles est revue à la baisse. Certains journalistes ne font pas le
travail de vérifier leurs sources pour accélérer le procédé de
publication.

#### Des organisations malveillantes internationales.

L’appât du gain facile que sont les Fake News a suscité des vocations.
En Macédoine, une partie de la jeunesse de Vélès s’est ainsi spécialisée
dans la création de Fake News, attirée par de juteux revenus
publicitaires. La ville s’est transformée en fabrique à Fake News
pendant l’élection américaine[^5]. Mais aussi des sites comme
[InfoWars](https://www.infowars.com/) voient naître des Fake News.

![image](../../img/rumeur_4chan/macron.jpg) \[macron\]

Des organisations qui travaillent dans l’ombre des plus grands forums
sont à la base de la conception des Fake News. En effet, l’étude de
[Savvas Zannettou et al, 2017](https://arxiv.org/abs/1705.06947) montre
comment les forums leaders mondiaux que sont 4chan et reddit sont en
partie responsable dans la création de rumeurs.

### La propagation des Fake News.

#### Les réseaux sociaux : médiations des Fakes News

Selon [Maksym Gabielkov et al, 2016](https://hal.inria.fr/hal-01281190),
59% des liens partagés sur Twitter n’ont jamais été cliqués. En d’autres
termes, la plupart des gens semblent retweeter des nouvelles sans jamais
les lire. Les personnes qui partagent sans lire des articles propagent
certainement des Fake News sans le savoir.

Pour évaluer une Fake News nous n’avons pas besoin de dîplome. En effet
des études ont montré que les déterminismes sociaux n’étaient pas
suffisants pour prévoir le partage de Fake News. L’éducation, le sexe,
l’âge, etc. ne sont pas des critères distinctifs. Nous voyons alors que
personne est à l’abri des Fake News. Seuls la pensée critique et le
recul nous permettraient d’être protégés des Fake News.

#### Le biais de confirmation.

Les biais de confirmation sont un aspect déroutant de la pensée humaine.
Nous pourrions penser que l’homme ait acquis une pensée analytique
développée pour arriver à ce niveau d’intelligence. Et pourtant il est
soumis au biais de confirmation. Ce biais cognitif consiste à
privilégier les informations confirmant nos idées préconçues ou nos
hypothèses. De plus il nous fait aussi négliger les informations jouant
en défaveur de nos conceptions.

Ainsi les personnes tenantes de la thèse des extraterrestres gouvernent
le payssont plus enclin à croire la thèse des reptiliens au pouvoir que
la thèse Barack Obama est un être humain .

Les Fake News relayant souvent des informations conspirationnistes, il
est facile pour un tenant de croire celle-ci plutôt que de croire des
versions officielles. Le biais de confirmation agit dans tous les sujets
confondus. Il n’est pas uniquement cantonné au conspirationnisme. Les
Fake News utilisent ce biais de manière idéologique pour renforcer nos
croyances et nous rendre son information plausible.

#### Tri de l’information selon Kahneman.

La thèse centrale de Daniel Kahneman, dans son livre Système 1 / Système
2 : Les deux vitesses , est qu’il y a une dichotomie entre deux modes de
pensée. Le système 1 est rapide, instinctif et émotionnel, alors que le
système 2 est plus lent, plus réfléchi et plus logique. Il définit les
biais cognitifs associés à chacun de ces modes de pensée. Il montre que
l’on donne une trop grande importance au jugement humain.

Selon Kahneman nous nous reposons plus souvent sur le système 1. Ce qui
expliquerait notre partage de Fake News quand nous sommes
émotionnellement impliqués.

### Les risques des Fake News.

#### Les risques politiques.

L’institutionnalisation des Fake News est l’un des plus gros risques
politiques. En effet rien de pire qu’une Fake News qui a pour
pseudo-autorité un état. Un état niant les faits devient répressifs.

[.5]{} ![Deux photos d’événements du National Mall à
Washington[]{data-label="fig:test"}](../../img/trumpvswomen/trump.png "fig:")

[.5]{} ![Deux photos d’événements du National Mall à
Washington[]{data-label="fig:test"}](../../img/trumpvswomen/women.png "fig:")

L’inauguration de Trump et la Women’s March avaient fait beaucoup de
bruit. Les partisans pro-Trump seraient soi-disant en plus grand nombre
que les partisans de la Women’s March. Nous pourrions croire la version
officielle. Mais apparemment sans comptage, il y avait plus de
participants à la Women’s March. L’État américain avaient tenté de faire
passer cela pour des faits alternatifs. Ce qui n’a pas beaucoup de sens.
Certes, nous observons tous le réel de manière différente, mais ce n’est
pas une raison pour faire du relativisme et conclure à des faits
alternatifs. De plus comment définir des faits alternatifs ? Prendre des
faits et les dénaturer à des fins idéologiques ne nous donne pas raison
sur la réalité. En somme, les Fake News peuvent servir à cacher des
scandales politiques.

D’autres Fake News institutionnalisées peuvent servir à des particuliers
pour qu’ils puissent s’enrichir, ou à ne pas payer d’amende. Par
exemple, nier le réchauffement climatique est très pratique quand on est
l’un des pays les plus polluant au monde.

#### Les risques sanitaires.

Beaucoup de Fake News portent sur les domaines sanitaires. Comme nous
l’avons vu précédemment avec les vaccins, les Fake News développent une
méfiance pour la médecine conventionnelle. Pour reprendre l’exemple des
vaccins, il faut savoir que des cas de rougeole mortels sont réapparus
ces dernières années. Ne pas se vacciner entraîne un baisse de la
couverture vaccinale. Le rapport bénéfice/risque est plus que positif
pour la vaccination. Aucun des effets indésirables notoires suspectés
n’a trouvé un protocole testable positif. Nous n’avons que des
affirmations pseudo-scientifiques et des hypothèses contre. En somme, la
désinformation, autour de la médecine notamment, peut couter la vie.

#### Détournement des news vers des sujets clivants.

Les Fake News peuvent être colportées par des personnes convaincues de
leur véracité. Le but ultime d’une Fake News est d’être considéré comme
une vraie information. Les Fake News détournent l’attention de la
population vers des problèmes factices et souvent résolus depuis des
années. En somme les Fake News sont une perte de temps. Elles nous
empêchent de nous focaliser sur de vrais problèmes ; car l’on doit
démystifier des faits irréels.

### Légitimité du projet et motivations.

Comme nous avons pu le voir dans les sous-sections précédentes. Les Fake
News sont de fausses nouvelles qui cherchent à tromper volontairement.
Elles participent pour la majorité à une pollution du web dûe au système
monétaire de la publicité en ligne. Elles servent parfois un propos
idéologique avec de mauvais argument. Ceci les rend moins crédibles pour
ceux qui découvrent le pot aux roses. Elles sont produites par des
militants anonymes anti-intellectuels prônant la désinformation sur de
sombres forums. Elles inondent les réseaux sociaux d’inepties et sont
partagées en masse sans être lues. Elles véhiculent des titres avec de
fausses idées alors qu’un simple coup d’oeil au corps de l’article rend
le propos infondé. De plus,Elles coutent la vie à certains. Et pour
finir elles peuvent devenir un instrument politique redoutable et
autoritaire.

Pour toutes ces raisons il est légitime de vouloir combattre le
phénomène des Fake News.

### Comment détecter une Fake News?

#### Comment vérifier des informations ?

Il y a deux moyens de détecter une Fake News. Par soi-même en cherchant
les indices du canular. Ou en utilisant un moteur de recherche de
canular sur un domaine internet.

Premièrement voyons de manière non-exhaustive quelques techniques pour
détecter une Fake News:

Avant de partager

:   il faut se questionner sur ce qu’il est raconté dans l’article et
    vérifier les sources. On est responsable de ce que l’on partage.

Est-ce une information ?

:   Il faut se poser différentes questions: Est-ce cela à un intérêt
    public ? Est-ce factuel ? Est-ce vérifié ? Cela permet de distinguer
    les avis et les rumeurs des informations.

Ce site est-il fiable ?

:   A-t-il une page À propos ? Est-il parodique ? Quelles sont les
    sources de ce site ?

Beaucoup de techniques spécifiques pour chaque média existent ! Nous ne
pouvons pas être exhaustif ici.

Les Fake News ont fait apparaître de nouveaux sites spécialisés dans la
détection de canulars. Par exemple, en français, il existe le
[Décodex](http://www.lemonde.fr/verification/) propulsé par le journal
le Monde. Ce site répertorie les autres sites selon leurs fiabilités. En
anglais il existe le site internet Polifacts de vérification des faits,
qui vérifie la véracité des promesses et engagements pris par les
politiques américains

#### Méthode informatique: Stance detection.

Cette tâche peut aussi être résolue avec un succès modeste par
l’apprentissage automatique. En effet une des réponses au phénomène des
Fake News est l’apparition de réseaux neuronaux complexes qui permettent
de manière partielle de repérer les Fake News. Ce repérage passe par une
détection des partis pris (stance detection).

Ainsi dans la deuxième partie de ce mémoire, nous allons voir plus en
détail ce qu’est la stance detection. Au travers de tâches partagées,
nous allons découvrir les techniques pour l’utiliser.

Dans la troisième partie nous nous essayerons à la Stance detection
aussi. Et donnerons une analyse comparative de nos résultats par rapport
à l’état de l’art.

Un problème; une méthode.
=========================

Vers une définition.
--------------------

### Formalisation de la *Stance Detection*.

La *Stance Detection* ou en français la détection de parti pris [^6] est
la méthode qui permet de déterminer si un énoncé **E** par rapport à une
cible **C** donnée est en accord ou en désaccord avec la cible. On
l’utilise aussi parfois pour déterminer si l’énoncé discute sans parti
pris de la cible. C’est-à-dire que **E** parle de **C** mais on ne
trouve aucun indice soit en faveur, soit en défaveur la cible. Par
extension, si on arrive à déterminer la cible, on peut connaître les
énoncés qui n’y correspondent pas. Ce type d’énoncé indépendant ne donne
aucun indice de prise de parti et surtout aucun indice de la cible en
général. La cible et l’énoncé ne partagent aucun lien direct ou
indirect. Ainsi la détection de parti pris nous permet de repérer ces
quatre cas de figure:

E est pour C

:   quand l’énoncé montre un ou des indices en faveur de la cible.

E est contre C

:   quand l’énoncé montre un ou des indices en contradiction avec la
    cible.

E discute C

:   quand l’énoncé donne une ou des informations sur la cible sans
    donner d’indices de parti pris comme dans les deux cas pécédents.

E est non-lié à C

:   quand l’énoncé ne donne aucune information par rapport à la cible en
    général.

Les deux derniers cas ne détectent aucun parti pris. Mais ils restent
pertinents pour la détection de parti pris doit intégrer une limitation
à un sujet donné. Une telle détection implémente donc un module de
détection des relations. Appellons **R** la relation entre **E** et
**C**.

### Domaine de la détection de parti.

Nous avons beaucoup parlé d’indices dans la partie précédente.
Questionnons leur nature. La détection de parti pris se base sur la
relation entre la cible et l’énoncé. La nature de cette relation est
sémantique. Les traits qui permettent d’unir l’énoncé et la cible pour
déterminer le parti pris doivent alors aussi entretenir une relation
sémantique. On verra plus tard que certaines relations syntaxiques
peuvent être utiles de manière localisées dans certaines tâches.

Il apparait un problème dû à la sémantique: il faut s’accorder au
préalable sur le sens des mots et sur ce que désignent nos cibles et
leurs rapports avec l’énoncé. En effet, pour constituer un corpus de
prise de position par rapport à un énoncé, il faudra trouver la manière
la plus objective de qualifier la relation entre l’énoncé et la cible.

### La genèse de la détection de parti pris.

Une des premières publications sur la déctection de prise de parti était
*Cats Rule and Dogs Drool!\[...\]* (voir [Pranav Anand et al,
2011](http://www.aclweb.org/anthology/W11-1701)) qui cherchait à classer
la prise de position dans des débats en ligne sur des sujets variés.
Leur but était de montrer que les débats idéologiques comportent une
plus grande part de messages de réfutation. La publication montrait
aussi qu’il est beaucoup plus difficile de classer les posts de
réfutation, aussi bien pour les humains que pour les classificateurs
automatiques formés à la détection de prise de parti.

Les chercheurs ont créé leur corpus à partir de 1113 débats bi-partiaux
(soit 4873 posts) dans 14 sujets différents du site
[ConvinceMe.net](http://www.convinceme.net/). Pour annoter le corpus,
les chercheurs ont demandé à neuf participants de mettre une étiquette
sur différentes parties de débat sur le site. Il est intéressant de
notifier que les annotateurs n’ont eu que 0.73 d’exactitude croisée dans
la classification des réfutations (tous sujets confondus). Ainsi le
problème sémantique est réel. Les annotateurs ne tombent pas d’accord
sur la relation sémantique de certains énoncés par rapport à leurs
cibles. Le but d’un système automatique de classification des
réfutations sera donc de s’approcher au plus de ce pourcentage
d’exactitude pour représenter au mieux le classement humain général.

L’équipe d’Anand a fait plusieurs modèles de système utilisant des
traits différents (n-grams, la ponctuation répétée, LIWC, dépendance
syntaxique,...). Ces modèles utilisaient soit une implémentation de
Naive Bayes, soit une implémentation de JRip[^7] en fonction des traits
choisis.

Les résultats des modèles varient en fonction des sujets entre 0.59 et
0.69 d’exactitude pour la détection de réfutation. De plus, aucun modèle
ne se départage des autres. Tous ont plus ou moins réussi selon un sujet
différent. La moyenne est 0.63 pour la détection de réfutation. C’est
dix points de moins que l’exactitude humaine (qui varie entre 0.66 et
0.94).

Premièrement, cette publication nous montre combien il est ardu de se
confronter à la sémantique. En droit, le sens d’un énoncé devrait être
univoque et susciter une seule relation universelle entre la cible et
l’énoncé. En fait, nous -les annotateurs humains- sommes tous soumis à
des biais, des opinions, des préjugés qui ne permettent qu’un
recouvrement subjectif de la relation entre cible et énoncé.

Deuxièmement, ce papier montre la difficulté de la tâche. Aucun modèle
possédant des traits particuliers n’a eu de meilleur résultat dans tous
les sujets confondus.

Nous avons présenté un des premiers travaux sur la détection de parti
pris. Par la suite, nous nous limiterons à des travaux plus récents.
Ceux-ci s’intéressent à notre sujet: les *Fake News*.

### Application générale et relative au *Fake News*.

Nous allons voir dans les sections suivantes les différentes
utilisations de la détection de parti pris à travers deux tâches
partagées. Premièrement dans la section 2, nous verrons l’utilisation de
la détection de parti pris à l’intérieur de *tweets* sur des sujets
polémiques; grâce à la ***SemEval-2016 Task 6***. Puis deuxièmement dans
la section 3, nous verrons l’utilisation de la détection de parti pris
pour la détection de *Fake News* ; grâce au ***Fake News Challenge***.
Nous proposerons dans la troisième partie de ce mémoire une contribution
originale de la tâche que nous discutons dans la section 3.

*SemEval-2016 Task 6*.
----------------------

### Description générale de la tâche.

Cette tâche porte le nom de *Detecting Stance in Tweets* ([Saif M.
Mohammad et al,
2016](https://www.aclweb.org/anthology/S/S16/S16-1003.pdf)). Le but de
la tâche est de déterminer la relation **R** entre un tweet **E** et une
cible **C**.

Ici, nous avons trois classes possibles pour déterminer le parti du
tweeter par rapport à son tweet:

favor

:   s’il est en faveur la cible.

against

:   s’il est contre la cible

neither

:   si il n’est ni en faveur la cible, ni il n’est contre la cible.

Exemple direct:

C

:   Hillary Clinton

E

:   Hillary Clinton has some strengths and some weaknesses.

R

:   neither

Exemple indirect:

C

:   legalization of abortion

E

:   A foetus has rights too! Make your voice heard.

R

:   against

La tâche se divise en deux sous-tâches:

#### Sous-tâche A.

La sous-tache A est supervisée. Elle porte sur cinq différents sujets
(*‘Atheism’*, *‘Climate Change is a Real Concern’*,*‘Feminist
Movement’*, *‘Hillary Clinton’*,*‘Legalization of Abortion’*). Elle
contient 4163 couples **C/E** labélisés **R**. On réserve 30% pour
l’ensemble de test et le reste pour l’ensemble d’entraînement.

#### Sous-tâche B.

La sous-tache B est non-supervisée. Elle porte sur un seul thème
(*‘Donald Trump’*). L’ensemble test est constitué de 707 tweets **E**.
Aucun ensemble d’entraînement n’a été donné. Mais un ensemble de 78 000
tweets non-labélisés à propos de Donald Trump était disponible.

#### Évaluation.

Pour l’évaluation des systèmes on utilise le F1-score moyen; calculé
ainsi: $$F_{avg} = \frac{F_{favor}+F_{against}}{2}$$ Avec F$_{favor}$ et
F$_{against}$ ainsi calculés:

$$F_{favor} = \frac{2P_{favor}R_{favor}}{P_{favor}+R_{favor}}$$

$$F_{against} = \frac{2P_{against}R_{against}}{P_{against}+R_{against}}$$

### Les participants.

Il y a eu 19 dépots pour la sous-tâche A et 9 dépots pour la sous-tâche
B. Premièrement, nous parlerons de la réussite à la tâche en général.
Deuxièment, nous discuterons seulement de quelques dépots intéressantes.
Et troisièment, nous comparerons les différents protocoles vus.

#### Dépots en général.

Parmi les 19 dépots de la sous-tâche A aucun système n’a dépassé les
baselines. En effet, Saif M. Mohammad et al ont fourni 4 baselines pour
la sous-tâche A. La première baseline naïve donnait le label majoritaire
à toutes les entrées (*Majority class*). Les trois suivantes utilisent
un ou plusieurs classificateurs linéaires (SVM) pour labéliser les
entrées. La deuxième utilisent 5 classificateurs SVM (un pour chaque
différent sujet) sur les vecteurs d’unigrams de la combinaison de **C**
et **E** (*SVM-unigrams*). De la même manière la troisième a aussi 5 SVM
mais utilise comme dimensions de vecteur : les 1-2-3-grams pour les mots
et les 2-3-4-5-grams pour les caractères (*SVM-ngrams*). Et pour finir,
la quatrième baseline utilise un seul SVM sur les mêmes dimensions de
vecteur que la troisième baseline (*SVM-ngrams-comb*).

En revanche, 7 des 9 équipes ont réussit à battre les baselines de la
sous-tâche sur B. Ces baselines reprennent certaines baselines de la
sous-tâche A à savoir la première *Majority class* et la quatrième
*SVM-ngrams-comb*.

Pour la sous-tâche A, la plupart des équipes ont utilisé des fonctions
de classification de texte standard tels que n-gram et vecteurs de mots,
des lexiques de sentiments. Certaines équipes ont interrogé Twitter sur
des hashtags, pour marquer des prises de parti plus déterminantes.
Certaines ont entrainé leurs systèmes à partir de vecteurs de Google
Actualitée ou directement des corpus Twitter.

Et pour la sous-tâche B, certaines équipes ont très bien détecté les
tweets en faveur de Trump. Grâce aux tweets qui se trouvaient dans le
corpus de Clinton en inversant leur valeur.

#### Dépots particuliers.

Ici, de manière succinte, nous allons décrire les différents modèles des
meilleurs systèmes pour les différentes tâches.

##### MITRE 1er pour la tâche A.

![image](../../img/model/mitre/model.png) \[mitre\_model\]

L’approche de détection de prise de parti de MITRE utilise un réseau de
neurones récurrent organisé en quatre couches de poids. Chaque mots est
projeté comme une entrée dans une couche d’*embbeding* de 256 dimensions
(créé avec word2vec), qui alimente en une couche récurrente contenant
128 LSTM. La sortie du terminal de cette couche récurrente est densément
connecté à un 128 classifieurs linéaires Cette même couche est
entièrement connectée à un softmax tri-dimentionnel dans laquelle chaque
unité représente l’une des classes de sortie: FAVOR, AGAINST ou NONE.

##### pkudblab 2ème pour la tâche A.

![image](../../img/model/pkudblab/model.png) \[pkudblab\_model\]

L’Architecture principale de pkudblab est un réseau de neurones
convolutionnels. On peut en décrire 5 composant majeurs:

Une table de correspondance

:   est une énorme matrice d’embbeding de mots. Chaque colonne de la
    table, correspond à un mot. Chaque mot incorporé dans cette table a
    été pré-formé par des vecteurs de word2vec (Mikolov et al., 2013).
    Ces vecteurs sont formés sur une partie de l’ensemble de données
    Google News.

Une matrice d’entrée

:   représente d’une phrase d’entrée et la longueur de la phrase.

La couche convolution

:   a pour but d’extraire des paternes, de sorte que certaines
    formulations abstraites communnes soient représentées.

Le Pooling layer

:   a pour but est de simplifier l’information dans le sortie de la
    couche convolutionnelle.

La Couche de sortie softmax

:   est entièrement connectée et est destinée à la classification.

Pour la sous-tâche A, ils ont séparées les ensembles de données en cinq
sous-ensembles. Ils ont donc entrainé de manière séparé les modèles sur
les différents sujets.

##### pkudblab 1er pour la tâche B.

Pour la sous-tâche B, ils ont utilisé le même modèle que pour A. Pour
entraîner leur modèle ils établissent un ensemble de données de
formation à deux classes (favor, against) à partir du corpus du domaine
officiel en fonction de plusieurs expressions spéciales.

#### Discussions comparatives.

    **Baseline**     **F$_{favor}$**   **F$_{against}$**   **F$_{avg}$**
  ----------------- ----------------- ------------------- ---------------
   Majority class         52.01              78.44             65.22
    SVM-unigrams          54.49              72.13             63.31
     SVM-ngrams           62.98              74.98             68.98
   SVM-ngrams-comb        54.11              70.01             62.06
     **Équipe**                                           
        MITRE             59.32              76.33             67.82
      pkudblab            61.98              72.67             67.33
       TakeLab            60.93              72.67             66.83

On voit qu’il est difficile de faire décoller les scores mêmes avec les
meilleurs systèmes. Ceci nous donne une bonne idée de l’état de l’art en
2016. Une implémentation simple avec des n-grams bien choisis et une
catégorisation aident beaucoup à avoir de bons résultats. Mais est-ce
toujours possible de contextualiser les données ? Il y a un biais
notoire du fait de travailler avec une micro vocabulaire en plus souvent
réduit sémantiquement par l’algorithme.

    **Baseline**     **F$_{favor}$**   **F$_{against}$**   **F$_{avg}$**
  ----------------- ----------------- ------------------- ---------------
   Majority class         0.00               59.44             29.72
   SVM-ngrams-comb        18.42              38.45             28.43
     **Équipe**                                           
      pkudblab            57.39              55.17             56.28
      LitisMind           30.04              59.28             44.66
      INF-UFRGS           32.56              52.09             42.32

La tâche dîte non-supervisée a fini par l’être. Au final les équipes ont
utilisé le corpus d’Hillary Clinton pour former celui de Trump. Ils ont
juste ajouté quelques expressions clichés trouvé la faveur ou la
défaveur du tweet. Le sujet de cette sous-tâche est particuliérement
clivant. Cela ne permet pas de retirer une méthode d’apprentissage non
supervisé objective.

*Fake News Challenge*.
----------------------

### Description générale de la tâche

Nous présentons dans cette section la tâche partagée qu’est le *Fake
News Challenge* et les différentes solutions proposées par ses
participants. Pour détecter des *Fake News* il nous faut résoudre
plusieurs défis à savoir:

1.  Déterminer si les faits présents dans l’article de presse sont
    corrects; c’est-à-dire déterminer la véracité des faits par rapport
    au monde réel.

2.  Analyser les relations entre le titre de l’article et le corps de
    l’article.

3.  Quantifier le biais inhérent d’un texte.

On voit clairement une application de la détection de parti pris dans le
défi 2. En effet ce défi correspond parfaitement à sa définition.

Évaluer la véracité d’un article est une tâche complexe et lourde, même
pour des experts formés. La première étape du Fake News Challenge se
concentre sur la tâche de détection de parti pris.

#### But.

L’objectif du Fake News Challenge est d’explorer comment les
technologies d’intelligence artificielle pourraient être utilisées pour
lutter contre les fake news.

#### Organisation générale.

Vous pouvez retouver toutes les infomations du [Fake News
Challenge](http://www.fakenewschallenge.org/) sur leur site officiel. Et
vous pouvez retrouver les codes de leur
[baseline](https://github.com/FakeNewsChallenge/fnc-1-baseline) et [les
données](https://github.com/FakeNewsChallenge/fnc-1) sur github.

#### Données et origines des données.

Le FNC est une tâche partagée supervisée. Les donneés sont pourvues par
les organisateurs. Ils définissent les données en termes d’entrées et de
sorties.Une entrée est le couple formé par une affirmation **C** et un
corps de texte **E**; soit à partir du même article de nouvelles ou de
deux articles différents. Une sortie est la relation **R** corps du
texte par rapport à la revendication faite dans l’affirmation définie
par l’une de ces quatre catégories:

related:

:   Le corps du texte **E** et l’affirmation **C** traitent d’un sujet
    en commun[^8].

    agree:

    :   Le corps du texte **E** est en accord avec l’affirmation **C**.

    disagree:

    :   Le corps du texte **E** n’est pas d’accord avec l’affirmation
        **C**.

    discuss:

    :   Le corps du texte discute **E** le même sujet que l’affirmation
        **C**, mais ne prend pas de parti pris.

unrelated:

:   Le corps du texte **E** traite d’un sujet différent de l’affirmation
    **C**.

[Ferreira & Vlachos
(2016)](http://aclweb.org/anthology/N/N16/N16-1138.pdf) ont au préalable
testé et créé un ensemble de donneés à partir du [site du projet
Emergent](http://www.emergent.info/) de Craig Silverman. Le projet
Emergent fut aussi utile pour la création du corpus de la FNC.

Les données de ce projet ont été collectées par des journalistes du
[*Tow Center for Digital Journalism*](https://towcenter.org/). Pour
ajouter une entrée au site, le journaliste doit trouver deux choses: une
affirmation qui semble être une rumeur et un ensemble d’articles qui
parlent de cette soi-disant rumeur. Les sujets de chaque affirmation
varient, cela va des dixits politiques de Donald Trump aux comparaisons
de prix de la prochaine Apple Watch. Les sources de celles-ci sont les
comptes twitter polémiques, traitant les rumeurs et les sites tel que
Snopes.com[^9].À partir de certaines affirmations, le journaliste
constitue donc un corpus d’articles pour établir la véracité de
celles-ci. Donc chaque affirmation peut être Vraie, Fausseou
Non-vérifié. Cette valeur de vérité peut être établie grâce au corpus
d’articles; où chaque article peut soit être Pour, Contreou Neutre. Le
journaliste résume l’article en un gros titre (*headline* à ne pas
confondre avec notre affirmations de rumeurs). Ce n’est pas le nombre
d’articles Pourou Contrela véracité des affirmations; mais bien sur la
vraissemblance des preuves qui sont rapportées dans les articles jugées
par le journaliste.

Le corpus de Ferreira & Vlachos est composé alors de 300 affirmations de
rumeurs dont 2595 articles sont associés à un ratio de 8,75 articles
pour une affirmation. La distribution hétérogène est de 47.7% Pour,
15.2% Contreet 37.1% Neutre. Pour tester si les données d’Emergent
étaient assez discriminatives et robustes pour une tâche d’apprentissage
automatique, Ferreira & Vlachos ont testé l’accord entre les gros titre
des journalistes et les affirmations de rumeurs. Nous ne détaillerons
pas plus leur protocole ici. Mais leur 73% d’exactitude (par rapport aux
47% de leur baseline naïve) donne une bonne estimation de la consistance
des données.

La répartitions des donneés de la FNC est faite avec le même procédé
mais cette fois-ci on est extrait l’affirmation de rumeurs et le corps
des articles. De plus les organisateurs ajoutent une dimension de
classification; la classe **unrelated** est formée à partir des couples
affirmation et de valeurs qui n’ont pas de liens sur la plateforme
Emergent. Les sujets sont alors non-liés. La répartition des données au
niveau des relations **R** se fait donc ainsi pour l’entrainement:
73.13% sont **unrelated**, 17.82% sont **discuss**, 7.36% sont **agree**
et 1.68% sont **disagree**. En chiffre cela donne 37727 corps d’articles
**E** pour 1648 affirmations de rumeurs **C**. Ce qui a donné 49973
couples **C/E**. L’ensemble de test est composé de 20019 corps
d’articles **E**, 894 affirmations de rumeurs **C** et donc de 25419
couples **C/E**. Bien sûr, les données **E** ou **C** entre le test et
l’entrainement ne se recoupent pas et les relations **R** ne sont pas
données dans le test.

Voici un exemple de données pour l’affirmation **C** suivante *Robert
Plant Ripped up \$800M Led Zeppelin Reunion Contract* :

R: Agree

:   **E**: *… Led Zeppelin’s Robert Plant turned down £500 MILLION to
    reform supergroup. …*

R: Disagree

:   **E**: *… No, Robert Plant did not rip up an \$800 million deal to
    get Led Zeppelin back together. …*

R: Discusses

:   **E**: *… Robert Plant reportedly tore up an \$800 million Led
    Zeppelin reunion deal. …*

R: Unrelated

:   **E**: *… Richard Branson’s Virgin Galactic is set to launch
    SpaceShipTwo today. …*

#### L’évaluation.

![image](../../img/fnc-eval/fnc-eval.png) \[fig\_eval\]

Les équipes seront évaluées selon un système de score relatif pondéré à
deux niveaux; pour le premier niveau il faut classer **E** et **C**
comme étant liés ou non (25% de la pondération). Puis pour le deuxième
niveau il faut classer les couples liés comme étant d’accord, en
désaccord ou discuté (75% de la pondération), trouver le bon **R** du
couple. Le score relatif est le score brut normalisé par le score
maximum possible sur l’ensemble de test [^10]. En effet, il est très
facile d’avoir une très bonne exactitude avec une classe sur-représentée
comme les **unrelated** (73.13% du corpus d’entrainement). Il y a donc
deux règles qui régissent ce score:

unrelated/related :

:   si la classe Gold et la classe attiribué ont la même méta-classe
    alors on ajoute 0.25 au score.

same related :

:   si entre deux classe **related** la classe Gold et la classe
    attiribuée sont les mêmes, alors on ajoute 0.75 au score.

Exemples de scores en fonction de l’attribution de classe:

   **Classe Gold**   **Classe attribuée**  **Score**
  ----------------- ---------------------- -----------
      unrelated           unrelated        +0.25
        agree             unrelated        +0
        agree              disagree        +0.25
        agree               agree          +0.75

#### Baseline.

Une simple baseline utilisant un classificateur de boosteur de gradient
est fourni par les organisateurs. Cette baseline inclut également le
code pour le pré-traitement du texte, la division des données pour
éviter des pertes entre l’entraînement et le test, la validation croisée
avec k-fold. Cette baseline permet les overlap entre les mots et les
n-grams et des fonctions d’indicateurs pour la polarité et la
réfutation. Avec ces caractéristiques et un classificateur boosté, la
baseline atteint un score d’exactitude pondérée de 79,53% avec dix
validations croisées.

#### Les participants.

Il y a eu 71 équipes participantes à cette tâche. Les trois premières
équipes avaient pour obligations d’écrire un article sur leur système et
d’en publier une version Opensource. Dans les sous-sections qui suivent,
nous allons justement vous présentez les systèmes des trois gagnant de
FNC.

### Solat in the swen.

#### Méthodologie.

![image](../../img/model/solat_in_the_swen/final_prediction_light.png)
\[fig0\]

L’équipe de Solat in the swen a implémenté plusieurs modèles
performants. Ils ont ensuite décidé de faire un modèle utilisant des
systèmes concurants. Les traits entre la solutions de Talos et la
baseline de la FNC ne changent pas. Ils utilisent le même preprocessing
et la même vectorisation. Le modèle est composé de plusieurs systèmes
concurents: le premier est un *deep convolutional neural network* et le
second est un *gradient-boosted decision trees*. Détaillons ici les
algorithmes du modèles:

![image](../../img/model/solat_in_the_swen/deep_model_light.png)
\[fig1\]

Le premier modèle utilisé par l’équipe a plusieurs réseaux de neurones
différents utilisés dans l’apprentissage en profondeur. Ce modèle
s’applique à la convolution numérique nette unidimensionnelle (CNN) sur
le titre et le corps du texte, en utilisant les vecteurs préchargés de
Google News. Les CNN permettent un calcul parallèle efficace lors de
l’exécution. La sortie de ce CNN est ensuite envoyée à MLP avec une
sortie 4 classes:agree, disagree, discusset unrelated , formés de bout
en bout. Cette architecture de ce modèle fut choisie en raison de sa
facilité de mise en œuvre et de son calcul rapide puisque l’on peut
compter sur des convolutions au lieu de récurrence. Il est par contre
limité par le fait qu’il ne peut observer le texte qu’une seule fois.

![image](../../img/model/solat_in_the_swen/tree_model_light.png)
\[fig2\]

L’autre modèle utilisé dans l’ensemble est un modèle d’arbres de
décision à gradient d’intensité (GBDT). Ce modèle introduit peu de
caractéristiques textuelles de l’affirmation de rumeurs et du corps de
l’article, qui sont ensuite introduites dans le sujet d’un gradient dans
la relation entre **C** et **E**. Ce modèle basé sur le texte entrainé
avec XGBoost utilise plusieurs modules de décision à savoir:

Un compteur de trait

:   pour compter le nombre de trait commun entre le titre et le corps de
    l’article.

La méthode de pondération TF-IDF

:   pour comparer de manière inversé la fréquence relative des mots.

Le procédé algebrique linéaire SVD Features

:   pour mesurer la similarité entre différents n-grams.

L’espace vectoriel word2vec

:   pour comparer le cosinus de similarité entre deux représentation
    vectorielle.

Un module Sentiment

:   utilisant un corpus de mots connotés sentimentalement.

Un **compteur de trait**, pour compter le nombre de trait commun entre
le titre et le corps de l’article, la méthode de pondération **TF-IDF**;
pour comparer de manière inversé la fréquence relative des mots, le
procédé algebrique linéaire **SVD Features** pour mesurer la similarité
entre différents n-grams, l’espace vectoriel **word2vec**; pour comparer
le cosinus de similarité entre deux représentation vectorielle et un
**module Sentiment** utilisant un corpus de mots connotés
sentimentalement.

Les arbres de décision à gradient ont été choisis en raison de la
robustesse du modèle par rapport aux différentes échelles des vecteurs
caractéristiques.

#### Résultats.

Talos in the swen gagne le FNC avec une score de 9556.50 points donc un
score relatif de 82.02%.

### Athene (UKP Lab).

#### Méthodologie.

![image](../../img/model/athene/athene_model.png) \[fig3\]

Le MLP proposé par Richard Davis et Chris Proctor (organisateurs de FNC)
a été le point de départ pour le développement du système final
d’Athene. La structure du système a été optimisée pour les
caractéristiques par une recherche aléatoire par laquelle les
hyper-paramètres ont été ajusté. La structure du modèle qui en résulte
est illustrée ci-dessus en résumé, car 5 des 7 couches cachées sont
ignorées.

Le preprocessing d’Athene utilise différents traits, à savoir: les Bag
of Words sur les uni-grams, les matrices de factorisations
non-négatives, l’indexation et l’analyses latente sémantique (LSA, LSI)
et la détection de paraphrase basé sur le recouvrement de mots (avec
word2vec).

La vectorisation des informations se passe en trois étape la
vectorisation des données préprocessées de **C** puis de **E** et la
création d’un vecteur joint des dimension se recoupant dans les deux
précédents vecteurs. Ces trois vecteurs sont alors concaténés en un seul
pour former une entrée.

Le modèle final rassemble cinq MLP initialisés de manière aléatoire, qui
donnent leurs sorties à un seul MLP qui va faire le vote de la classes à
attribuer à partir des autres MLP.

#### Résultats

Athene arrive deuxième au classement du FNC avec une score de 9550.75
points donc un score relatif de 81.97%.

### UCL Machine reading.

#### Méthodologie.

![image](../../img/model/uclmr/uclmr_model.png) \[fig4\]

UCL-MR est juste un MLP (plutot simple par rapport aux autres solutions)
entrainé sur les unigrams et une utilisation astucieuse du TF-IDF.

UCL utilise deux représentations simples des mots avec BoW pour les
entrées de texte: fréquence de terme (TF) pour représenter l’affirmation
**C** et le corps de l’article **E** et l’inverse de la fréquence de la
fréquence du document (TF-IDF) pour calculer le cosinus de similarité
entre **E** et **C**.

Ainsi les vecteurs d’entrée contiennent ces trois vecteurs composites.
Les vecteurs passent dans une seule couche d’entrée de 100 perceptrons
avec une activation ReLU. Puis une couche linear pour donner une valeur
à chacune des classes. Puis un softmax pour sortir la classe dominante.

UCL-MR utilise juste un MLP mais avec des paramètres très optimisés.
Nous ne détaillerons pas ici les paramètres d’implémentation qui se
retrouvent dans leur publication.

#### Résultats.

UCL-MR arrive troisième au classement du FNC avec une score de 9521.50
points donc un score relatif de 81.72%.

### Discussion comparative des modèles et des résultats.

      **Équipes**      **Scores bruts**   **Scores relatifs**
  ------------------- ------------------ ---------------------
   Talos in the Swen       9556.50              82.02%
        Athene             9550.75              81.97%
         UCLMR             9521.50              81.72%

Comme l’a dit Dean Domerleau (organisateur) en parlant de ce tableau de
résultats: Ce que tout cela signifie, c’est que les meilleures équipes
se sont très bien débrouillées, mais il y a certainement encore place
pour l’amélioration!. En effet on pourrait pousser plus loin les sytèmes
pour que ceux-ci nous donnent de meilleurs résultats. Mais qu’il n’y ait
pas de percée d’une équipe dans le tableau des scores, et le fait que
très peu d’équipes on fait mieux que la baseline, montrent que cette
tâche est difficile.

De plus un système complexe comme celui de Talos sensé être explicatif
sur les traits pertinents ne se démarque que de 0,3 points du système
d’UCLMR très peu explicatif mais bien otpimisé, qui reste une boîte
noire au niveau de la sélection des paramètres. On revient à un modèle
régréssif qui est simple et qui explique beaucoup avec peu. Mais cela
donne une compréhension minime du phènomène. Ou peut être le système
d’UCLMR est surévalué pour cette ensemble de données. En ce qui concerne
Athene les résultats sont sensiblement les mêmes que Talos. La
complexité de leur modèle est aussi fait à partir d’apprentissages
automatisés, certes moins complexe que Talos mais qui reste quand même
un modèle avec des systèmes concurents.

Ce qu’il faudrait faire, c’est de comparer les outputs de chaque système
et voir comment ils trient les classes **related**. Ainsi on pourait
faire des recoupements sur les données. Cela permettrait de constater ce
que les différents systèmes font à l’identique et ce qu’ils font
différemments. On en déterminerait les traits et les architectures de
modèle relatifs aux classes de données.

C’est ce que je me propose de faire dans la première section de la
partie 3 de ce mémoire. Dans le but ensuite d’apporter une contribution
originale à ce problème en partant des systèmes déjà réalisés.

Un challenge; des tentatives!
=============================

Analyse des résultats des participants et création d’hypothèses.
----------------------------------------------------------------

Dans cette troisième partie nous tentons de faire une analyse d’erreurs
comparative des participants de la FNC. Nous avons reproduit les
résultats de tous les participants[^11].

### Un aperçu de l’ensemble de test.

         Stance  unrelated   agree   disagree   discuss    Somme
  ------------- ----------- ------- ---------- --------- ----------
         Nombre    18349     1903      697       4464      25413
    Pourcentage   72.20%     7.48%    2.74%     17.56%      100%
      Score FNC   4587.25    1903      697       4464     11651.25

Il y a 7064 points à marquer avec les *Related* et seulement 4587.25
points avec les *Unrelated*. Ainsi comme nous l’avions vu précédement
trouvé un *Related* rapporte 4 fois plus de points que trouvé un
*Unrelated*.

Afin de produire des hypothèses non-biaisées [^12], nous allons faire
des observations des résultats des différents modèles sur 80% des
entrées de l’ensemble de test.

         Stance  unrelated   agree   disagree   discuss   Somme
  ------------- ----------- ------- ---------- --------- --------
         Nombre    14662     1568      550       3550     20330
    Pourcentage   72.12%     7.71%    2.70%     17.46%     100%
      Score FNC   3665.5     1568      550       3550     9333.5

Le corpus de test étant partiellement ordonné nous avons retiré les 20%
de manière ordonnée[^13] aussi.

Les résultats et les scores des participants.
---------------------------------------------

Ici nous présentons les différents résultats des modèles de chaque
participant sur notre ensemble de test à 80%. Notez que les tables de
confusions ont horizontalement les labels de vérité et verticalement les
prédictions. Nous présentons les participants du premiers au derniers
selon le score FNC.

### Talos in the Swen.

[ r | c c c c | c ]{}\
& agree & disagree & discuss & unrelated & Somme\
agree & 927 & 11 & 478 & 152 & 1568\
disagree & 217 & 8 & 235 & 90 & 550\
discuss & 661 & 5 & 2700 & 184 & 3550\
unrelated & 26 & 0 & 172 & 14464 & 14662\
Somme & 1831 & 24 & 3585 & 14890 & 20330\

On remarque que la classe **disagree** est largement sous-représentée.
Cette classe est aussi sous-représentée dans l’ensemble d’entrainement.
Ce qui explique potentiellement pourquoi nous ne détectons pas ces
traits distinctifs.

[ r | c c c c ]{}\
Mesure & agree & disagree & discuss & unrelated\
Précision & 0.59 & 0.01 & 0.76 & 0.99\
Rappel & 0.51 & 0.33 & 0.75 & 0.97\
F1score & 0.55 & 0.03 & 0.76 & 0.98\
Exactitude &\
Score FNC &\
Pourcentage FNC &\

Bien que Talos in the Swen ait remporté la 1er place de la FNC,
l’exactitudes et les scores ci-dessus ne sont pas les maximaux.

#### Les sous-modèles de Talos in the Swen.

##### Sous-modèle arborescent de Talos in the Swen

Les sous-modèles de Talos n’ont pas eu de soumission à la FNC mais ils
sont quand même intéressants à étudier car ils expliquent les résultats
et les biais du modèles.

[ r | c c c c | c ]{}\
& agree & disagree & discuss & unrelated & Somme\
agree & 807 & 0 & 690 & 71 & 1568\
disagree & 147 & 1 & 334 & 68 & 550\
discuss & 500 & 1 & 2902 & 147 & 3550\
unrelated & 16 & 0 & 160 & 14486 & 14662\
Somme & 1470 & 2 & 4086 & 14772 & 20330\

On voit d’où le modèle principal tient son aversion du label
**disagree**.

[ r | c c c c ]{}\
Mesure & agree & disagree & discuss & unrelated\
Précision & 0.51 & 0.0 & 0.82 & 0.99\
Rappel & 0.55 & 0.5 & 0.71 & 0.98\
F1score & 0.53 & 0.0 & 0.76 & 0.98\
Exactitude &\
Score FNC &\
Pourcentage FNC &\

Ce sous-modèles ne tient pas vraiment compte de la classe **disagree**
mais il a paradoxalement tout de même les plus hauts scores du
challenge. En effet si Talos avait proposé uniquement ce modèle il
aurait pris encore plus d’avance par rapport aux autres participants.

##### Sous-modèle de Deep Learning de Talos in the Swen

[ r | c c c c | c ]{}\
& agree & disagree & discuss & unrelated & Somme\
agree & 911 & 115 & 143 & 399 & 1568\
disagree & 271 & 62 & 41 & 176 & 550\
discuss & 1396 & 137 & 1397 & 620 & 3550\
unrelated & 2321 & 449 & 766 & 11126 & 14662\
Somme & 4899 & 763 & 2347 & 12321 & 20330\

Nous voyons clairement que ce sous-modèle vient équilibrer le
sous-modèle arborescent. Sa table de confusion montre une tentative
d’uniformisation de la classe **disagree**.

[ r | c c c c ]{}\
Mesure & agree & disagree & discuss & unrelated\
Précision & 0.58 & 0.11 & 0.39 & 0.76\
Rappel & 0.19 & 0.08 & 0.6 & 0.9\
F1score & 0.28 & 0.09 & 0.47 & 0.82\
Exactitude &\
Score FNC &\
Pourcentage FNC &\

Cette uniformisation a pour conséquence que ce sous-modèle est le pire
de tous les modèles. Combiné avec le sous-modèle arborescent, il permet
d’avoir une augmentation minime de la classe **disagree** au détriment
des autres classes.

### Le système Athene

[ r | c c c c | c ]{}\
& agree & disagree & discuss & unrelated & Somme\
agree & 709 & 57 & 669 & 133 & 1568\
disagree & 193 & 56 & 193 & 108 & 550\
discuss & 388 & 30 & 2853 & 279 & 3550\
unrelated & 16 & 3 & 86 & 14557 & 14662\
Somme & 1306 & 146 & 3801 & 15077 & 20330\

La table de confusion d’Athene ressembe beaucoup à celle de Talos. Ce
modèle tente beaucoup plus de labéliser des titres d’articles comme
**diagree**. Mais il a beaucoup plus de mal à distinguer la classe
**discuss** de la classe **agree**.

[ r | c c c c ]{}\
Mesure & agree & disagree & discuss & unrelated\
Précision & 0.45 & 0.1 & 0.8 & 0.99\
Rappel & 0.54 & 0.38 & 0.75 & 0.97\
F1score & 0.49 & 0.16 & 0.78 & 0.98\
Exactitude &\
Score FNC &\
Pourcentage FNC &\

Athene a la meilleure exactitude de toute la FNC car elle classe très
bien les **unrelated** (qui ne valent pas beaucoup de points dans le
score FNC).

### UCL Machine Reader

[ r | c c c c | c ]{}\
& agree & disagree & discuss & unrelated & Somme\
agree & 697 & 7 & 770 & 94 & 1568\
disagree & 144 & 37 & 277 & 92 & 550\
discuss & 424 & 35 & 2882 & 209 & 3550\
unrelated & 44 & 2 & 261 & 14355 & 14662\
Somme & 1309 & 81 & 4190 & 14750 & 20330\

Nous observons une tentative d’uniformisation proportionnelle de la
table de confusion. UCLMR sait très bien classé les **unrelated**.
Néanmoins, il manque apparemment de traits pour distinguer les **agree**
des **discuss**.

[ r | c c c c ]{}\
Mesure & agree & disagree & discuss & unrelated\
Précision & 0.44 & 0.07 & 0.81 & 0.98\
Rappel & 0.53 & 0.46 & 0.69 & 0.97\
F1score & 0.48 & 0.12 & 0.74 & 0.98\
Exactitude &\
Score FNC &\
Pourcentage FNC &\

### Analyses et Hypothèses

Voici un liste d’hypothéses basée sur nos constatations que nous
testerons de vérifier par la suite avec les différents modèles. Nous
voyons clairement une confusion entre la **agree** et la classe
**discuss**. Mieux distinguer ces deux classe rapporterait gros Et
pourrait faire un différence significative. La classe **disagree** est
sous-représentée donc quantitativement elle ne rapporte que peu de
points. Le modèls de Talos semble plus robuste que les autres en
utilisant l’apprentissage par ensemble (*ensemble learning*). Utiliser
ce type d’apprentissage entre les modèles des participants augmenterait
certainement les performances.

Modèles par combinaison:\
Le vote de majorité
-------------------------

### Explication du modèle.

Comme nous l’avons vu précédement les combinaisons entre les modèles
déjà présentés à la FNC peuvent atteindre de hauts résultats. Notre
premier modèle sera un jet naif de combinaisons de deux modèles. Le vote
de majorité se base sur les classes prédites par les modèles des
participants pour l’ensemble de test complet. Ce vote de majorité marche
avec un modèle dominant départageant en cas de conflict entre les deux
autres modèles assujettis. La classe la plus voté sera la classe
prédite. Si jamais les trois classes sont toutes différentes alors est
choisie la classe donné par le modèle dominant.

[ c c c || c ]{}\
Modèle Dominant & Modèle assujetti 1 & Modèle assujetti 2 & Classe
prédite\
**agree** & **agree** & unrelated & **agree**\
disagree & **discuss** & **discuss** & **discuss**\
**discuss** & disagree & agree & **discuss**\

Ainsi chaque modèle à tour de rôle peut devenir le modèle dominant. Ce
qui donne les résultats dans la sous-sections suivantes.

### Les résultats des votes de majorité

#### Dominant: Talos in the swen

[ r | c c c c | c ]{}\
& agree & disagree & discuss & unrelated & Somme\
agree & 923 & 13 & 815 & 152 & 1903\
disagree & 228 & 20 & 321 & 128 & 697\
discuss & 483 & 4 & 3729 & 248 & 4464\
unrelated & 27 & 0 & 149 & 18173 & 18349\
Somme & 1661 & 37 & 5014 & 18701 & 25413\

[ r | c c c c ]{}\
Mesure & agree & disagree & discuss & unrelated\
Précision & 0.49 & 0.03 & 0.84 & 0.99\
Rappel & 0.56 & 0.54 & 0.74 & 0.97\
F1score & 0.52 & 0.05 & 0.79 & 0.98\
Exactitude &\
Score FNC &\
Pourcentage FNC &\

#### Dominant: Athene

[ r | c c c c | c ]{}\
& agree & disagree & discuss & unrelated & Somme\
agree & 914 & 42 & 809 & 138 & 1903\
disagree & 213 & 46 & 308 & 130 & 697\
discuss & 453 & 21 & 3735 & 255 & 4464\
unrelated & 14 & 2 & 148 & 18185 & 18349\
Somme & 1594 & 111 & 5000 & 18708 & 25413\

[ r | c c c c ]{}\
Mesure & agree & disagree & discuss & unrelated\
Précision & 0.48 & 0.07 & 0.84 & 0.99\
Rappel & 0.57 & 0.41 & 0.75 & 0.97\
F1score & 0.52 & 0.11 & 0.79 & 0.98\
Exactitude &\
Score FNC &\
Pourcentage FNC &\

#### Dominant: UCL Machine Reader

[ r | c c c c | c ]{}\
& agree & disagree & discuss & unrelated & Somme\
agree & 920 & 13 & 844 & 126 & 1903\
disagree & 202 & 35 & 339 & 121 & 697\
discuss & 467 & 26 & 3728 & 243 & 4464\
unrelated & 19 & 1 & 157 & 18172 & 18349\
Somme & 1608 & 75 & 5068 & 18662 & 25413\

[ r | c c c c ]{}\
Mesure & agree & disagree & discuss & unrelated\
Précision & 0.48 & 0.05 & 0.84 & 0.99\
Rappel & 0.57 & 0.47 & 0.74 & 0.97\
F1score & 0.52 & 0.09 & 0.78 & 0.98\
Exactitude &\
Score FNC &\
Pourcentage FNC &\

#### Commentaires sur les résultats du vote de majorité

Bien que ce modèle d’apprentissage par ensemble semble être le plus
naïf; ces résultats sont les plus haut que l’on obtiendra. On remarque
que Athene est le meilleur des modèles dominants. C’est le modèle qui se
trompe le moins en cas de conflit.

Modèles par combinaison:\
Par moyenne
-------------------------

### Modèles utiliseant *50/50 weighted average*

Pour ce modèle, deux sous-modèles génèreront des probalités de label
pour chaque entrée. Nous nous s’inspirerons de la méthode d’unification
de Talos. Nous utiliserons donc aussi un *50/50 weighted average* pour
combiner les résultats. Ainsi chaque sous-modèles produira un vecteurs
de dimension 4 pour chaque labels. Chaque couple de même dimensions
passera par un *50/50 weighted average*. Le maximum des 4 résultats des
moyennes indiquera la classe prédite pour l’entrée.

Notre première architecture utilisera le sous-modèle arborescent de
Talos et le modèle de UCL Machine Reader. Nous appelerons ce modèles
mixte UCLMR/Talos TF-Idf.

Notre deuxième architecture utilisera aussi le sous-modèle arborescent
de Talos et le modèle de UCL Machine Reader mais dans cette version le
sous modèle arborescent de Talos n’utiliseras pas son de TF-Idf. La
raison est que le système de UCL utilise déjà et uniquement ces
traits-là. Ainsi pour augmenter la différence entre les résultats des
deux sous-modèles, nous décidons de retirer ce module. De plus il sera
entrainé seleument sur les données d’entraînement pour créer son espace
sémantique[^14]. Nous appelerons ce modèles mixte UCLMR/Talos sans
TF-Idf.

### Résultats

#### Modèles mixte UCLMR/Talos TF-Idf

[ r | c c c c | c ]{}\
& agree & disagree & discuss & unrelated & Somme\
agree & 963 & 0 & 819 & 121 & 1903\
disagree & 198 & 1 & 377 & 121 & 697\
discuss & 606 & 3 & 3612 & 243 & 4464\
unrelated & 21 & 0 & 166 & 18162 & 18349\
Somme & 1788 & 4 & 4974 & 18647 & 25413\

Cette table de confusion ressemble beaucoup à celle de Talos dans
l’analyse sur 80% du corpus. Sans surprise, la classe disagree n’est pas
améliorée. Par contre, les classes agree, discuss et unrelated sont
légèrement augmentées.

[ r | c c c c ]{}\
Mesure & agree & disagree & discuss & unrelated\
Précision & 0.51 & 0.0 & 0.81 & 0.99\
Rappel & 0.54 & 0.25 & 0.73 & 0.97\
F1score & 0.52 & 0.0 & 0.77 & 0.98\
Exactitude &\
Score FNC &\
Pourcentage FNC &\

Nous constatons un gain de 0.52% par rapport au meilleur des systèmes de
la FNC. Ceci est peu mais montre une amélioration minime de la précision
de la classe agree et de la classe discuss. La classe disagree est
encore négligée par le modèle arborescent de Talos. En conséquence, le
modèle UCLMR biaisé par Talos ne permet pas d’améliorer la précision de
la classe disagree.

#### Modéles mixte UCLMR/Talos sans TF-Idf

[ r | c c c c | c ]{}\
& agree & disagree & discuss & unrelated & Somme\
agree & 1002 & 0 & 776 & 125 & 1903\
disagree & 216 & 1 & 357 & 123 & 697\
discuss & 602 & 2 & 3596 & 264 & 4464\
unrelated & 16 & 0 & 149 & 18184 & 18349\
Somme & 1836 & 3 & 4878 & 18696 & 25413\

Par rapport au modèle mixte UCLMR/Talos TF-Idf, ce modèle améliore la
classe des **agree** d’une quarantaine d’entrée. C’est certes un
avantage minime, qui n’en reste pas moins surprenant. En effet le modèle
avec TF-Idf a un espace sémantique plus exhaustif et plus proche de
l’ensemble de test.

[ r | c c c c ]{}\
Mesure & agree & disagree & discuss & unrelated\
Précision & 0.53 & 0.0 & 0.81 & 0.99\
Rappel & 0.55 & 0.33 & 0.74 & 0.97\
F1score & 0.54 & 0.0 & 0.77 & 0.98\
Exactitude &\
Score FNC &\
Pourcentage FNC &\

Certes l’avantagesur le modèle précédent n’est que de 0.16% pour les
pourcentage FNC. Peut-être montrons-nous qu’un espace sémantique
simplement formé avec l’ensemble d’entrainement est suffisant.

Apprentissage par ensemble:\
Avec *Single Layer Learner*
----------------------------

### Explication du modèle

Une des meilleurs manière *a priori* de déterminer une classe à partir
d’une liste de probabilité est certainement d’utiliser un couche
neuronale. Ainsi nous avons créer avec le framework Keras un *Single
Layer Learner*. Celui-ci dispose d’un couche d’entrée de la longueur de
nos vecteurs d’entrainement, d’un couche de 32 unités d’apprentissage et
d’une couche de sortie de 4 unités, une par label. Afin de produire les
vecteurs d’entrainement nous avons utiliser l’intégralité du corpus
d’entrainement. Chaque dixième des vecteurs on était produits par les
90% restant du corpus. Les données qui ont servi à produire les vecteurs
d’entraînement sont les vecteurs concaténé du modèle Mixte UCLMR/Talos
sans TF-Idf. Nous nommerons ce modèle Mixte UCLMR/Talos sans TF-Idf SLL.

#### Code du modèle

``` {.python language="Python"}

  import numpy as np
  import keras
  from keras.models import Sequential
  from keras.layers import Dense, Activation
  import tensorflow as tf


  def create_trained_nn(vecs_train, labels_train, epochs=50):
      """Create a trained neural network model."""
      input_dim = vecs_train.shape[1]
      model = Sequential()
      model.add(Dense(units=32, input_dim=input_dim))
      model.add(Activation('relu'))
      model.add(Dense(units=4))
      model.add(Activation('softmax'))
      model.compile(loss='sparse_categorical_crossentropy',
                    optimizer='sgd',
                    metrics=['accuracy'])
      model.fit(vecs_train, labels_train, epochs=epochs,
                batch_size=32)

      return model
```

### Résultats

[ r | c c c c | c ]{}\
& agree & disagree & discuss & unrelated & Somme\
agree & 1059 & 3 & 729 & 112 & 1903\
disagree & 253 & 14 & 323 & 107 & 697\
discuss & 684 & 7 & 3530 & 243 & 4464\
unrelated & 45 & 0 & 288 & 18016 & 18349\
Somme & 2041 & 24 & 4870 & 18478 & 25413\

[ r | c c c c ]{}\
Mesure & agree & disagree & discuss & unrelated\
Précision & 0.56 & 0.02 & 0.79 & 0.98\
Rappel & 0.52 & 0.58 & 0.72 & 0.97\
F1score & 0.54 & 0.04 & 0.76 & 0.98\
Exactitude &\
Score FNC &\
Pourcentage FNC &\

Etonnamment ce modèle a de moins bons résultats que le modèle précédent.
Même en changeant les paramètres d’apprentissage (nombre d’unités
d’apprentissage ou nombre de récusrion) le modèle n’excéde pas le
précédents.

Discussions
-----------

Notre objectif dans ce troisième chapitre était de proposer des
améliorations aux systèmes présentés à la fake news challenge. Sur la
diversité des hypothèses et des tests effectués nous observons qu’il n’y
a très peu de systèmes qui dépassent la baseline que l’on s’était fixé
(à savoir les résultats de Solat in the swen).

Rappelons que nous avons utilisé trois méthodes combinaison : le vote de
majorité, la moyenne pondérée à 50/50 et finalement une méthode d’
apprentissage d’ensemble avec une couche neuronalle apprenante.

Nous avons bien vérifié une de nos hypothèses celle qui disait qu’en
combinant les résultats de plusieurs systèmes gagnant de la fnc on
obtiendrait de meilleurs résultats. Par contre les résultats nous
donnent une bonne leçon d’humilité en ce que nos modèles les plus
complexes n’ont pas eu les meilleurs résultats. En effet le vote de
majorité ressort grand gagnant de nos améliorations alors que c’est le
système le plus simple et naïf. A posteriori nous expliquons son succès
du fait que c’est le modèle qui dispose le plus de ressources par
rapport aux autres. En effet, nos autres modèles de combinaison ou notre
modèle d’apprentissage par ensemble ne se base que sur les résultats de
deux sous-modèles gagnants, alors que le vote de majorité dispose des
résultats de tous les participants gagnants.

Ainsi le modèle de vote de majorité où le système Athene est dominant
dépasse notre baseline de 1.26 avec le score de 83,28 au pourcentage
fnc. Nous regrettons, en revanche, la difficulté d’accessibilité du code
du système d’Athene au profane. Pour cette raison nous n’avons pas pu
produire des probabilités de labels que nos autres modèles utilisent.
Ceci est l’explication de l’absence deux moyennes ou d’apprentissage
d’ensemble entre Athene et les autres participants.

Nous regrettons aussi de ne pas avoir réussi à utiliser correctement le
module TF-IDF du modèle Solat in the swen. Cela a créé plus de variable
indépendante pour nos modèles de moyenne et notre modèle d’apprentissage
d’ensemble. C’est donc moins partique pour la comparaison de modèle.

Notre autre hypothèse : mieux distinguer les labels agree et discuss
améliore les résultatsne fut pas vérifiée de manière indidrecte. En
effet nous regrettons aussi de ne pas avoir utilisé plus de technologie
du traitement du langage afin de mieux faire cette distinction. Mais à
vrai dire nous n’étions pas sur de quelle voie emprunter. Les systèmes
gagnants ont explorer de manière assez exhaustive les technologies
pertinentes. Ils ont montré ce qui valait la peine de ce qui était
délétère. Prétendre à proposer des traits non significatif n’était pas
notre but. C’est pourquoi nous nous sommes concentrés sur des
combinaisons de système. Mais si par le futur il venait à y avoir une
découverte de très plus significative que les présents, ces systèmes ne
demanderaient qu’à être amélioré.

Nous sommes aussi rendu compte que entraîner les systèmes sur les
headlines de test ne changez pas beaucoup l’espace sémantique des
classifieurs. Les résultats étant assez proche entraîner avec ou sans.

Conclusions
===========

Dans ce mémoire nous avons vu ce qu’était donc une fake news ce
phénomène nouveau d’informations volontièrement trompeuses qui pullulent
et se reproduisent sur le web. Nous avons décrit les origines leur mode
de fonctionnement et leur utilisation. Entre autres nous avons vu à quel
point elles peuvent être dangereuses utilisé à des fins autoritaire.
Nous avons donc proposé une méthode manuelle pour s’en protéger de
manière individuelle et éducative. Ensuite nous sommes allés voir les
systèmes informatiques préliminaires de détection de fake news.
Labelliser comme vrai/faux est pour le moment impossible, du fait du
manques cruel de corpus d’entrainement pour ce type de tâches. Nous nous
sommes donc rabattu sur les technologies de traitement de langage qui
pourrait potentiellement aider à créer un classifieur fake news/true
news par le futur. Ainsi nous avons présenté la détection de position.
Nous sommes familiarisé avec le concept avec la tâche 6 semeval 2016
puis nous nous sommes rapprochés de notre but en expliquant la fake news
challenge. Nous avons discuté les différents résultats obtenus des
participants gagnants au challenge et nous avons décrit leurs modèles.
Et dans notre dernière partie nous avons proposé nos propre modèle
combinatoire pour répondre à la fake news challenge. De manière minime
nous avons dépasser l’état de l’art.

En conclusion, nous avons donc atteint nos 3 objectifs à savoir définir
exhaustivement ce qu’est une fake news, expliquer comment detection de
position peut aider à leurs détections et dépasser l’état de l’art en la
matière.

Appendice
=========

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
commodo consequat. Duis aute irure dolor in reprehenderit in voluptate
velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint
occaecat cupidatat non proident, sunt in culpa qui officia deserunt
mollit anim id est laborum.

[^1]: En français, nouvelle truquée mais le terme Fake News est devenu
    tellement commun en français qu’il sera utilisé dans ce mémoire.

[^2]: Andrew Wakefield est un ancien chirurgien britannique et chercheur
    médical connu pour ses prétentions frauduleuses entre le vacin ROR
    et l’autisme. Il fut radié de l’ordre des médecins en mai 2010 pour
    défaut à son devoir de consultant responsable.

[^3]: Partisans de la controverse sur la vaccination qui remet en cause
    son efficacité et la sécurité de certains vaccins.

[^4]: Citation : *Knowing more and understanding less in the age of big
    data* sous-titre du livre *The internet of us*, de Michael Lynch
    ISBN-10:
    [0871406616](https://www.kirkusreviews.com/book-reviews/michael-patrick-lynch/the-internet-of-us/)

[^5]: D’après le
    [Figaro](http://www.lefigaro.fr/actualite-france/2017/03/06/01016-20170306ARTFIG00187-fake-news-un-meme-terme-pour-plusieurs-realites.php)
    20/12/2017

[^6]: Vous remarquerez que pour la cohérence et pour la consistance de
    ce document nous n’emploierons plus que la formulation détection de
    parti prisau lieu de *Stance Detection*.

[^7]: JRip est un classificateur basé sur des règles qui produisent un
    modèle compact adapté à la conception d’application rapide.

[^8]: Cette méta-relation ne labélisera jamais les données elle est là
    pour mieux comprendre le but de la détection de prise de parti.

[^9]: [Snopes.com](https://www.snopes.com/) est un site Web anglophone
    créé dans le but de limiter la propagation des canulars
    informatiques et des rumeurs infondées circulant sur Internet.

[^10]: Nous donnerons à chaque fois le score brut et le score normalisé
    en pourcent.

[^11]: À l’exeption de Talos in the Swen qui ont laissé une copie de
    leur CSV de leurs résultats, pour leurs deux modèles sur leur
    répertoire Github.

[^12]: Du moins des hypothèses qui ne soient pas ajustées totalement à
    l’ensemble de test final.

[^13]: En effet, nous avons retiré toutes les entrées dont l’indice été
    divisible par 5 ou 10

[^14]: En effet dans la version originale du modèle lors de la création
    de l’espace sémantique les données de test viennent augmentées les
    données d’entrainement. Cela a pour conséquence que le modèle ait
    déjà vu les données de test lors de son entrainement. Mais ne nous
    méprenons pas cela est autorisé dans le réglement de la FNC même si
    cela est assez questionnable.
