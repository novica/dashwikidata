# Dash app to access Wikidata

This is a simple demo in dash I did to see the diffrence between building an app with stramlit vs. shiny for python vs dash.

The app is packaged as a python package and can be installed locally with:

```
pip install .
```

And run with:

```
gunicorn dashwikidata.app:server -b :8000
```

