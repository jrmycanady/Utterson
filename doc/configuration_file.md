# Configuration File
Utterson contains a single core configuration file. The file may be generated
three ways. With the --generate_config switch, the --build_utterson
switch, and manually.

## Raw File
```yaml
site:
  url: <string>
  deployment_root: <string>
  jekyll_root: <string>
  site_title: <string>

tags:
  - default

categories:
  - default

users:
```

## Configuration Parameter Definitions
- site
-- **url**: The full url for the site when published.
-- **
*   Red