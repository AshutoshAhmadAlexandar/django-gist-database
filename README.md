Gist Database
===============


This project will combine our work with the [requests library](http://docs.python-requests.org/en/master/) (HTTP) and databases. We will use requests to interface with Github's API to retrieve [gists](https://help.github.com/articles/about-gists/) and store them in a database that we will then be able to perform searches on.

Example:
* Guido's HTML Gists: [https://gist.github.com/gvanrossum](https://gist.github.com/gvanrossum)
* Guido's API Gists: [https://api.github.com/users/gvanrossum/gists](https://api.github.com/users/gvanrossum/gists)

## Tests

Tests are all under `tests/`. We some fixtures and mocking to make testing fast and remove side effects. Don't worry if you don't understand it now. You can just focus on reading the actual test functions. If you feel lost and need to print something out in the screen, you can use the `main.py` script. It's using the testing database. The same one used for `test_search.py`.

## The Importer
Your `import_gists_to_database` function will take three parameters:

 - `db`: The database object to connect to
 - `username`: The GitHub user whose gists we are going to retrieve
 - `commit` *(Optional, defaults to `True`)*: If `True`, automatically commit changes to database

You are going to use the [GitHub gists API](https://developer.github.com/v3/gists/) to retrieve the gists of a given user, insert those gists into a database (schema may be found in the `schema.sql` file), and if `commit` is True, commit those changes to the database.

## The Searcher

Your `search_gists` method should take a `db_connection` parameter (the database connection), as well as two **optional** arguments:
- `github_id`
- `created_at`

If no parameter is provided, all the gists in the database should be returned. If `public_id` or `created_at` parameters are provided, you should filter your SELECT query based on them.

## Optional activities

This project contains optional tests that you can just uncomment if you want an extra challenge. Your task will be to extend the `search_gists` function to accept the following **optional** parameters:

 - `created_at__gt`
 - `created_at__gte`
 - `created_at__lt`
 - `created_at__lte`
 - `updated_at__gt`
 - `updated_at__gte`
 - `updated_at__lt`
 - `updated_at__lte`

These parameters will be operating against the `created_at` and `updated_at` fields using the corresponding comparison: `gt` means greater than, `gte` greater than or equal to, `lt` less than, `lte` less than or equal to.

That is, `created_at__gt=datetime(2018, 1, 1)` are all the Gists that were created AFTER January 1st 2018. If we use `created_at__gt`, that'd also include the corresponding day.

## Important Note for datetime parameters

When comparing dates in your sql statements use the format `datetime(attribute) operator datetime(comparing_date)`.

For example, to search by date, you need to use the following query:

```python
params = {
  'created_at': datetime(2014, 5, 3, 20, 26, 8)
}
cursor = db.execute("""
  SELECT *
  FROM
    gists
  WHERE
    datetime(created_at) == datetime(:created_at)
""", params)
```

**Remember, the search should return a list of `Gist` objects (see `Gist` definition is in `models.py`). Not just the tuples**
