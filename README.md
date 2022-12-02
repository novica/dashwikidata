# Dash app to access Wikidata

This is a simple demo in Streamlit I did to see the diffrence between building an app with stramlit vs. shiny for python.

The app can be run with:

```
python app.py
```

Install locally with:

```
pip install .
```

And run with:

```
gunicorn dashwikidata.app:server -b :8000
```