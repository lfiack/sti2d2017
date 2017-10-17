#Ariane 5 Vol 501
Ceci n'est pas une histoire inventée, j'ai un petit peu simplifié quelques détails, mais grosso modo, c'est bien ça qui s'est passé en vrai.

Notre histoire se déroule le 4 juin 1996.
L'agence spatiale européenne, l'ESA (European Space Agency) réalise le vol inaugural de la fusée Ariane 5.
Comme le modèle précédent, la fusée Ariane 4 était particulièrement fiable, l'Ariane 5 était composée de beaucoup de composants issus de l'Ariane 4.
Du coup, l'ESA était particulièrement confiante, et, pour économiser un ou plusieurs vols d'essais, 
le vol inaugural contenait 4 satellites pour un coût total de 370 millions de dollars.

Au final, la fusée à explosé au bout de 36,7 secondes, à 4000m d'altitude. Dommage.

Alors, qu'est-ce qui s'est passé?

Pour expliquer le problème, je vais devoir vous expliquer *de manière simplifiée* comment on envoie un satellite en orbite.
Alors, si on envoie la fusée tout droit, et bien elle va finir par retomber sur Terre.
Pour aller en orbite, il faut faire un "virage" ("gravity turn" en anglais).
On accélère donc verticalement ET horizontalement.

Les fusées sont bourrées de capteurs dont un qui permet de mesurer l'accélération horizontale.
Pour la fusée Ariane 4, la grandeur maximale correspondant à cette accélération tourne autour de 60 (j'ai pas d'unité, c'est vraiment la valeur brute sortant du capteur).
60, c'est pas mal, ça rentre sur un octet.

Sur la fusée Ariane 5, qui est beaucoup plus puissante, mais surtout qui fait un "gravity turn" plus "aggressif", cette valeur peut atteindre la valeur 300.
Alors 300, ça rentre sur un octet ?
-> Non
On peut rentrer des valeurs jusqu'à combien ?
-> 255
Donc lorsque la valeur à dépassé 256, le calculateur de bord à cru à une accélération horizontale de 0: la fusée va tout droit vers l'espace, et à cherché à corriger.
Du coup, les tuyères se sont braqués au max.
La fusée, elle est pas conçue pour pouvoir supporter de tels efforts et le système qui maintient les boosters au reste de la fusée se sont détachés.
Le contrôleur de la fusée a fini par détecter un problème grave et à lancé le processus d'autodestruction de la fusée.

Au final, cette boulette a couté 370 millions de dollars, plus le prix du lanceur, 
plus la perte de confiance envers les clients de l'ESA (ce qui a probablement couté beaucoup plus cher au final).

Évidemment, cette boulette aurait pu être évitée par une simple simulation ou un vol d'essai.
Mais par cet exemple un peu extrème, on voit concrètement l'intérêt de se poser des questions du codage et de la représentation de l'information
