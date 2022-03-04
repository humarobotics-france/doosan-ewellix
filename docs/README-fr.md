<a href="https://www.humarobotics.com/">
    <img src="../images/Logo_HR_bleu.png" alt="HumaRobotics logo" title="HumaRobotics" align="right" height="80" />
</a>

# Doosan Ewellix

<p align="left">
  <a href="../README.md">English</a> •
  <a href="./README-fr.md">Français</a>
</p>

--------------

Interface TCP/IP permettant d'utiliser une colonne téléscopique Ewellix avec un robot Doosan.

Ce projet est développé par [HumaRobotics](https://www.humarobotics.com/).

## Conditions requises

- Un **robot Doosan**
- Une colonne **Ewellix**

## Mode d'emploi

- Configurer l'adresse IP du robot pour être sous le même sous réseau que la colonne (par défaut: "192.168.1.X")

- Créez un `Custom Code` et importez le fichier [ewellix.py](../ewellix.py) (il faut remplacer le .py par .txt pour importer le fichier dans un Doosan). N'oubliez pas d'enlever les premières lignes du code (ces lignes sont utilisées pour tester le code sans robot).

- Ensuite, regardez les exemples dans le dossier "examples" pour voir comment utiliser la classe Ewellix. Vous pouvez commencer avec le programme [ex_basic.py](../examples/ex_basic.py) (n'oubliez pas de changer l'extension '.py' en '.txt' pour importer le fichier dans le Doosan).

## Exemples

- [ex_basic.py](../examples/ex_basic.py): Exemple basique de communication entre une colonne Ewellix et un robot Doosan.
- [ex_move_ewellix.tw](./examples/ex_move_ewellix.tw): Un "TaskWriter" pour déplacer la colonne Ewellix avec un "User Input" (H2017-v2.8.2).

## Tests

- [test_fake_ewellix.py](../tests/test_fake_ewellix.py): Code simulant une Ewellix depuis un ordinateur. Vous pouvez lancer ce script, puis le programme  [ewellix.py](../Ewellix.py) depuis un même ordinateur pour simuler la communication.

<div align = "center" >
<img src="../images/Logo_HR_bleu.png" alt="HumaRobotics logo" title="HumaRobotics" height="200" />
</div>
