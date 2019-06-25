# LE DOSSIER SOTA EST DANS LE REPO : Recommendation-System-Q 
https://github.com/PNS-PS7-1819/Recommendation-System-Q

# pns-innov1819-new-pns-innov1819-q-eatrack
pns-innov1819-new-pns-innov1819-q-eatrack created by GitHub Classroom
_Soufiane AOURINMOUCHE - _Hugo Croenne - _Alix Humbert - _Mohamed Younnes


### Repository 
This project is about recipes recommendation application.
It will be used by everyone in order to help him to decide recipes to prepare.
It is based on a recommendation system designed for an individual person or a group of persons.
It is a configurable recommendation system, by users numbers: individual/groups, also by context : family, friends group ... 


# Tests and benchmarks

## Benchmarking
In the file unit_test_CF_rec_test.py, we have a benchmark that for given inputs, it execute several algorithms and checks that our system recommendation's failure score is the lowest.


# Server roots
/getRecommendation : root to get recommendation, it is a POST request and takes list of users_id as arguments
/hey : test root, it returns a simple string
/helloWorld : test root, it tests JSON object use

# Server information
host : host='127.0.0.1'
port : port=81


### Sub-modules
##### Add submodule
```git submodule add <url> fileName```

##### Define branch to be used by the submodule
```
cd /path/to/parent/repo
git config -f .gitmodules submodule.<path>.branch <branch>
```
(Pour avoir le path : ```cat .gitmodules```)

##### Update all submodules 
```git submodule update --init --recursive --remote```

#### Delete a submodule 
```
git submodule deinit <path_to_submodule>
git rm <path_to_submodule>
git commit-m "Removed submodule "
rm -rf .git/modules/<path_to_submodule>
```
