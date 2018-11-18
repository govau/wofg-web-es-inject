Data dictionary for WofG Web Reporting service - tracking post-filtering field names injected into ElasticSearch.

Naming convention is as follows:

| Prefix | Source | Category | Description | Detail |
|--------|--------|----------|-------------|---------|
| `m_*` | `<meta name="*">` |Metadata (name type)|Standard metadata tags| [metadata-standard.csv](metadata-standard.csv), [metadata-non-standard.csv](metadata-non-standard.csv), [custom-fields.csv](custom-fields.csv)|
| `mh_*` | `<meta http-equiv="*">`|Metadata (http-equiv type)|http-equiv style metadata tags| [http-headers-standard.csv](http-headers-standard.csv), [http-headers-non-standard.csv](http=-headers-non-standard.csv)|
| `mp_*` | `<meta property="*">`|Metadata (property type)|Property style metadata tags| [metadata-standard.csv](metadata-standard.csv) |
| `aa_*` | (Added via filters) |Accessibility check| Accessibility auditor check information| [funnelback-standard.csv](funnelback-standard.csv)|
| `ca_*` | (Added via filters) |Content auditor check| Content auditor check information| [funnelback-standard.csv](funnelback-standard.csv)|
| `h_*`  | `*:` |HTTP header| HTTP headers|  [http-headers-standard.csv](http-headers-standard.csv), [http-headers-non-standard.csv](http=-headers-non-standard.csv) |
| `fb_*` | (Added via filters)|Funnelback-generated Header metadata| Funnelback-inserted HTTP headers| [funnelback-standard.csv](funnelback-standard.csv) |
| `ga_*` | Google Analytics 360 Data API|Metadata (name type)|GA Data API for sites using [DTA GA360 account](https://beta.dta.gov.au/our-projects/google-analytics-government)|[ga360-fields.csv](ga360-fields.csv) |
