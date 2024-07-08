# SharedArticle

**Properties**

| Name           | Type        | Required | Description                                                         |
| :------------- | :---------- | :------- | :------------------------------------------------------------------ |
| url            | str         | ❌       | Article's URL.                                                      |
| adx_keywords   | str         | ❌       | Semicolon separated list of keywords.                               |
| subsection     | str         | ❌       | Article's subsection (e.g. Politics). Can be empty string.          |
| column         | str         | ❌       | Deprecated. Set to null.                                            |
| eta_id         | int         | ❌       | Deprecated. Set to 0.                                               |
| section        | str         | ❌       | Article's section (e.g. Sports).                                    |
| id\_           | int         | ❌       | Asset ID number (e.g. 100000007772696).                             |
| asset_id       | int         | ❌       | Asset ID number (e.g. 100000007772696).                             |
| nytdsection    | str         | ❌       | Article's section (e.g. sports).                                    |
| byline         | str         | ❌       | Article's byline (e.g. By Thomas L. Friedman).                      |
| type\_         | str         | ❌       | Asset type (e.g. Article, Interactive, ...).                        |
| title          | str         | ❌       | Article's headline (e.g. When the Cellos Play, the Cows Come Home). |
| abstract       | str         | ❌       | Brief summary of the article.                                       |
| published_date | str         | ❌       | When the article was published on the web (e.g. 2021-04-19).        |
| source         | str         | ❌       | Publisher (e.g. New York Times).                                    |
| updated        | str         | ❌       | When the article was last updated (e.g. 2021-05-12 06:32:03).       |
| des_facet      | List[str]   | ❌       | Array of description facets (e.g. Quarantine (Life and Culture)).   |
| org_facet      | List[str]   | ❌       | Array of organization facets (e.g. Sullivan Street Bakery).         |
| per_facet      | List[str]   | ❌       | Array of person facets (e.g. Bittman, Mark).                        |
| geo_facet      | List[str]   | ❌       | Array of geographic facets (e.g. Canada).                           |
| media          | List[Media] | ❌       | Array of images.                                                    |
| uri            | str         | ❌       | An article's globally unique identifier.                            |
