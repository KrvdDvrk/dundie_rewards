# How to use

## Load data

Having a file `people.csv` with the following format:

```csv
Jim Halpert, Sales, Salesman, jim@dundlermifflin.com
Dwight Scrute, Sales, Manager, schrute@dundlermifflin.com
Gabe Lewis, Director, Manager, glewis@dundlermifflin.com
```

Run `dundie load` command

```py
dundie load people.csv
```

## Viewing data

### Viewing all information

```bash
$ dundie show

┏━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━┓
┃ Email             ┃ Balance ┃ Last_Movement     ┃ Name          ┃ Dept    ┃ Role     ┃
┡━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━┩
│ jim@dundlermiffl… │ 810     │ 2023-12-12T18:21… │ Jim Halpert   │ Sales   │ Salesman │
│ schrute@dundlerm… │ 410     │ 2023-12-12T18:21… │ Dwight Scrute │ Sales   │ Manager  │
│ glewis@dundlermi… │ 100     │ 2023-12-11T12:59… │ Gabe Lewis    │ C-Level │ CEO      │
└───────────────────┴─────────┴───────────────────┴───────────────┴─────────┴──────────┘
```

### Filtering

Avaliable filters are `--dept` and `--email`

```bash
dundie show --dept=Sales

┏━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━┓
┃ Email              ┃ Balance ┃ Last_Movement      ┃ Name          ┃ Dept  ┃ Role     ┃
┡━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━┩
│ jim@dundlermiffli… │ 810     │ 2023-12-12T18:21:… │ Jim Halpert   │ Sales │ Salesman │
│ schrute@dundlermi… │ 410     │ 2023-12-12T18:21:… │ Dwight Scrute │ Sales │ Manager  │
└────────────────────┴─────────┴────────────────────┴───────────────┴───────┴──────────┘
```

> **NOTE** passing `--output=file.json` will save a json file with the results.

## Adding points

An admin user can easily add points to any user or dept.

```bash
dundie add 100 --email=jim@dundlermifflin.com

┏━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━┓
┃ Email               ┃ Balance ┃ Last_Movement       ┃ Name        ┃ Dept  ┃ Role     ┃
┡━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━┩
│ jim@dundlermifflin… │ 910     │ 2023-12-13T17:05:4… │ Jim Halpert │ Sales │ Salesman │
└─────────────────────┴─────────┴─────────────────────┴─────────────┴───────┴──────────┘
```

Avaliable selectors are `--email` and `--dept`
