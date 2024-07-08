# GetSharedPeriodJsonOkResponse

**Properties**

| Name        | Type                | Required | Description                                  |
| :---------- | :------------------ | :------- | :------------------------------------------- |
| status      | str                 | ❌       | API response status (e.g. OK).               |
| copyright   | str                 | ❌       | Copyright message.                           |
| num_results | int                 | ❌       | Number of articles in the results (e.g. 20). |
| results     | List[SharedArticle] | ❌       | Array of articles.                           |
