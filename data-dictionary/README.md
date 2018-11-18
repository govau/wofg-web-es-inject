Data dictionary for WofG Web Reporting service - tracking post-filtering field names injected into ElasticSearch.

Naming convention is as follows:

| Elastic search variable | Source variable name | ES variable type | Category | Description |
|-------------------------|----------------------|------------------|----------|-------------|
| m_* | <meta name=""*""> |(varies)|Metadata (name type)|Fields prefixed with m_ are standard metadata tags|
|mh_*|"<meta http-equiv=""*"">"|(varies)|Metadata (http-equiv type)|Fields prefixed with mh_ are http-equiv style metadata tags|
|mp_*|"<meta property=""*"">"|(varies)|Metadata (property type)|Fields prefixed with mp_ are property style metadata tags|
|aa_*|(Added via filters)|(varies)|Accessibility check|Fields prefixed with aa_ contain Funnelback accessibility auditor check information|
|ca_*|(Added via filters)|(varies)|Content auditor check|Fields prefixed with ca_ contain Funnelback content auditor check information|
|h_*|*:|(varies)|HTTP header|Fields prefixed with h_ are HTTP headers|
|fb_*|(Added via filters)|(varies)|Funnelback-generated Header metadata|Fields prefixed with fb_ are Funnelback inserted HTTP headers|
