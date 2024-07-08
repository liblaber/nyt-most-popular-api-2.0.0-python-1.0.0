# Media

**Properties**

| Name                     | Type                | Required | Description                                |
| :----------------------- | :------------------ | :------- | :----------------------------------------- |
| type\_                   | str                 | ❌       | Asset type (e.g. image).                   |
| subtype                  | str                 | ❌       | Asset subtype (e.g. photo).                |
| caption                  | str                 | ❌       | Media caption.                             |
| copyright                | str                 | ❌       | Media credit.                              |
| approved_for_syndication | int                 | ❌       | Whether media is approved for syndication. |
| media_metadata           | List[MediaMetadata] | ❌       | Media metadata (url, width, height, ...).  |
