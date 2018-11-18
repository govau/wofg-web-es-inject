Data dictionary for WofG Web Reporting service - tracking post-filtering field names injected into ElasticSearch.

Naming convention is as follows:

| Prefix | Source | Category | Description | Example |
|--------|--------|----------|-------------|---------|
| `m_*` | `<meta name="*">` |Metadata (name type)|Standard metadata tags|`<meta name="title" content="DTA Home page" />`|
| `mh_*` | `<meta http-equiv="*">`|Metadata (http-equiv type)|http-equiv style metadata tags| |
| `mp_*` | `<meta property="*">`|Metadata (property type)|Property style metadata tags| |
| `aa_*` | (Added via filters) |Accessibility check| Accessibility auditor check information| |
| `ca_*` | (Added via filters) |Content auditor check| Content auditor check information| |
| `h_*`  | `*:` |HTTP header| HTTP headers| |
| `fb_*` | (Added via filters)|Funnelback-generated Header metadata| Funnelback-inserted HTTP headers| |
| `ga_*` | Google Analytics 360 Data API|Metadata (name type)|GA Data API for sites using [DTA GA360 account](https://beta.dta.gov.au/our-projects/google-analytics-government)| |
