#Codage de l'information et Numération
* O4 - Décoder l’organisation fonctionnelle, structurelle et logicielle d’un système
	* CO4.2. Identifier et caractériser l’agencement matériel et/ou logiciel d’un système
	* CO4.4. Identifier et caractériser des solutions techniques relatives aux matériaux, à la structure, 
		à l’énergie et aux informations (acquisition, traitement, transmission) d’un système
	* CO4.4. Identifier et caractériser des solutions techniques relatives aux matériaux, à la structure, 
		à l’énergie et aux **informations** (acquisition, traitement, transmission) d’un système
* O6 - Communiquer une idée, un principe ou une solution technique, un projet, y compris en langue étrangère
	* CO6.1. Décrire une idée, un principe, une solution, un projet en utilisant des outils de représentation adaptés
	* CO6.2. Décrire le fonctionnement et/ou l’exploitation d’un système en utilisant l'outil de description le plus pertinent

* 2.1.2 Organisation fonctionnelle d’une chaîne d’information
	* Caractérisation des fonctions relatives à l'information : acquisition et restitution, codage et traitement, transmission
* 2.3.6 Comportements informationnels des systèmes
	* Caractérisation de l’information : expression, visualisation, interprétation, caractérisations temporelle et fréquentielle
	* Modèles de description en statique et en dynamique
* 3.1.4 Traitement de l’information
	* Codage (binaire, hexadécimal, ASCII) et transcodage de l’information, compression, correction

##09/11/17
Première séance avec les SIN

* Vidéo en début de séance: 
	* [Vidéo Dr. Nozman Vrai ou Faux Informatique](https://youtu.be/Itcvi5joPaw)
	* Téléchargé avec [ce site](https://telecharger-videos-youtube.com/)
* Débriefing vidéo:
	* Qu'est-ce que l'informatique?
= Traitement automatique d'information (par le biais de programmes informatiques et de machines)

	* Stockage de l'information
-> retrouver l'historique

	* Algèbre booléenne (Georges Boole)
-> exprimer la logique sous forme de variable, d'opérateurs et de fonctions
-> Algèbre binaire n'acceptant que deux valeurs numériques, 0 ou 1, soit vrai, soit faux

	* Transposition sur circuit électrique (Claude Shannon)
-> Transposition de l'algèbre booléenne sur circuits électriques : 1 relais fermé, 0 relais ouvert. Remplacé maintenant par des transistors.
-> Calcul informatique = suite d'opérations sur des paquets de 0 et des 1 généralement regroupés par multiples de 8.

Beaucoup d'autres grands noms non cités.

	* Représentation des nombres
Bug en 2038 -> représentation des dates en 32 bits
-> Évolution de représentation des nombres est passé de 8 à 16 puis 32 bits et enfin 64 bits aujourd'hui, pour représenter des nombres jusqu'à 255, 65k, 4G, 1.8E19

* Démarrage AP
	* Objectif: Comment l'ordinateur fait-il pour coder une image ?
	* PDF avec formulaire -> Comme ça pas de problèmes avec libreoffice
	* Régulièrement "Faire valider par l'enseignant"
	* Pensez à enregistrer régulièrement et à vérifier que ça ait bien sauvegardé (c'est la première fois qu'on teste ça)

* Pendant l'AP, je note régulièrement où les élèves en sont arrivés.

##11/10/17
Idem avec groupe ITEC
-> Plus compliqué parce que le groupe est plus nombreux
	-> Penser à homogénéiser les groupes
Explications sur l'en-tête en groupe (1 à 2 îlots)
* Démonstration en modifiant le niveau de gris max
	* Les pixels > 254 deviennent noirs -> Explication rebouclage (lien avec la vidéo)
* Démonstration en modifiant la taille de l'image 
	* le logiciel n'affiche que les N premières lignes.

##12/10/17
Fiche de connaissance = synthèse + exos dans le même dossier
- Codage binaire
* Tentative travail en groupes de 4
	* Je ne donne pas la solution au tableau

##16/10/17
Activité 2 pour les plus rapide, fin activité 1 pour les autres.

Synthèse AP1 : "Comment l'ordinateur fait-il pour coder une image ?"
* Fichier image composé de pixels
* Logiciel de visualisation + éditeur hexadécimal -> État "brut" de la mémoire = Succession de bit, organisé en octets dans le logiciel
	* Interprété comme un nombre (= Vue décimale, binaire ou hexa)
	* Interprété comme un niveau de gris
	* Interprété comme un caractère
* Comment un fichier image est organisé (header+"payload") -> On peut extrapoler ça à tous types de fichiers.
	* Le header sert à un logiciel (ou un humain) à décoder le fichier
	* Le payload est le partie intéressante du fichier (ici l'image)
* Conversion binaire vers décimal et inversement

Lancement AP2: Codages binaires, hexa, BCD et ASCII. Conversion entre les différents codages.
Utilisation du logiciel "Guide Des Automates"
* Vocabulaire
* Différentes bases utilisées en informatique et conversion
* Différents codages
* Faites les calculs sur feuille

Les élèves qui vont plus vite: écrire programme python permettant de passer d'une base à une autre

##19/10/17
Travail en groupes de 4 : suite de la synthèse et des exercices sur le binaire.

Début du cours sur l'hexadécimal.

##06/11/17
J'ai commencé à corriger les activités sur SysML, il me manque les rapports de certains d'entre vous:
Activité 1:
Antoine
Killian (excusé)
Corentin (vide)

Activité 3:
Guillaume
Barclay

J'ai quelques remarques générales : Commencez à prendre des bonnes habitudes :
Lisez les questions jusqu'au bout ! Apprenez à survoler le sujet jusqu'au bout avant de commencer
Rédigez vos réponses (attention à la grammaire et à l'orthographe, SVP)
Faites attention à la tournure de vos phrases : « elle redescend direct »

Il y aura encore une séance, peut-être deux.
Qui a fini les deux activités?

##08/11/17
J'ai commencé à corriger les activités sur SysML, il me manque les rapports de certains d'entre vous:
Activité 1:
Marwane RACHDI

Activité 2:
Ethan
William

Activité 3:
Ethan
Mathys
Illyas

J'ai quelques remarques générales : Commencez à prendre des bonnes habitudes :
Lisez les questions jusqu'au bout ! Apprenez à survoler le sujet jusqu'au bout avant de commencer
Rédigez vos réponses (attention à la grammaire et à l'orthographe, SVP)
Faites attention à la tournure de vos phrases : « elle redescend direct »

Il y aura encore une séance, peut-être deux.
Qui a fini les deux activités?

##09/11/17
Évaluation synthèse SysML

##13/11/17
###Demander à Nathalie
Comment qu'on met des notes sur pronote
Qu'est-ce qu'on fait avec les élèves absents au contrôle?
Guyard Nathan ne m'a pas rendu les compte-rendus. Qu'est qu'on fait?

###Avec mon groupe
Envoyez-moi le compte-rendu d'activité 1.

Évaluation orale individuelle:
* Qu'est-ce qu'un pixel
* Qu'est-ce qu'une en-tête
* Qu'est-ce qu'un bit ?
* Qu'est-ce qu'un octet ? Combien peut-il prendre de valeurs différentes ? Valeur min, max ?
* Qu'elle est la différence entre la base binaire, décimale, hexadécimale ? Qu'elles sont leurs utilités ?

Ensuite, je fais quelques conversions au tableau (sur 6 bits):
* 10 1101(2) = 1+4+8+32 = 45(10) = 2D(16)
* 39(10) = 10 0111(2) = 27(16)
 	(39 -> 19(1) -> 9(1) -> 4(1) -> 2(0) -> 1(0) -> 0(1))
* 3A(16) = 11 1010(2) = 32+16+8+2 = 58(10)

Continuer activité 2. Certains sont en retard, c'est la dernière séance d'activité. Il faut avoir fini la partie sur l'hexa.
Distribuer exercices

##15/11/17
Même que lundi avec l'autre groupe

##16/11/17
Fin fiche de connaissances : Exercices Hexa
Exercices supplémentaires
