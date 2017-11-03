#Codage de l'information et Numération
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

Synthèse AP1
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
