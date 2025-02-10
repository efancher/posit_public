# Instructions for Automated Test Cases

## Assumptions

* Assumes you have python 3.10 or above, or can install it.
* Assumes you have Chrome installed.
* Assumes you have a posit cloud user created.

## Steps

* Create and activate a python venv

```
pushd ~
python3 -m venv env_posit_challenge
source ~/env_posit_challenge/bin/activate
```

* Clone the project.
```
git clone git@github.com:efancher/posit_public.git
```

* Enter the project directory.

```
cd posit_public
```

* Install dependencies.

```
 python3 -m pip install -r requirements.txt
```

* Run Tests.

```
  pytest --username "[your user name]" --password 'your password'
```
