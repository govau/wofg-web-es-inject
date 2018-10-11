try:
    import ujson as json
except:
    import json

std_meta_wl = (
    'm_agls_audience','m_agls_availability','m_agls_creator',
    'm_agls_date','m_agls_function','m_agls_mandate',
    'm_agls_mandate_act','m_aglsterms_accessibility',
    'm_aglsterms_aggregationlevel','m_aglsterms_audience',
    'm_aglsterms_availability','m_aglsterms_category',
    'm_aglsterms_creator','m_aglsterms_date',
    'm_aglsterms_datelicensed','m_aglsterms_description',
    'm_aglsterms_documenttype','m_aglsterms_function',
    'm_aglsterms_identifier','m_aglsterms_isbasedon',
    'm_aglsterms_jurisdiction','m_aglsterms_language',
    'm_aglsterms_mandate','m_aglsterms_protectivemarking',
    'm_aglsterms_publisher','m_aglsterms_rights',
    'm_aglsterms_servicetype','m_aglsterms_subject',
    'm_aglsterms_title','m_author','m_dc_contributors',
    'm_dc_coverage','m_dc_creator','m_dc_date','m_dc_description',
    'm_dc_format','m_dc_identifier','m_dc_language','m_dc_publisher',
    'm_dc_relation','m_dc_rights','m_dc_source','m_dc_subject',
    'm_dc_title','m_dc_type','m_dcterms_abstract',
    'm_dcterms_accessRights','m_dcterms_accrualMethod',
    'm_dcterms_accrualPeriodicity','m_dcterms_accrualPolicy',
    'm_dcterms_alternative','m_dcterms_audience','m_dcterms_available',
    'm_dcterms_bibliographicCitation','m_dcterms_conformsTo',
    'm_dcterms_contributor','m_dcterms_coverage',
    'm_dcterms_created','m_dcterms_creator','m_dcterms_date',
    'm_dcterms_dateAccepted','m_dcterms_dateCopyrighted',
    'm_dcterms_dateSubmitted','m_dcterms_description',
    'm_dcterms_educationLevel','m_dcterms_extent',
    'm_dcterms_format','m_dcterms_hasFormat','m_dcterms_hasPart',
    'm_dcterms_hasVersion','m_dcterms_identifier',
    'm_dcterms_instructionalMethod','m_dcterms_isFormatOf',
    'm_dcterms_isPartOf','m_dcterms_isReferencedBy',
    'm_dcterms_isReplacedBy','m_dcterms_isRequiredBy',
    'm_dcterms_issued','m_dcterms_isVersionOf','m_dcterms_language',
    'm_dcterms_language','m_dcterms_license','m_dcterms_mediator',
    'm_dcterms_medium','m_dcterms_modified','m_dcterms_provenance',
    'm_dcterms_publisher','m_dcterms_references',
    'm_dcterms_relation','m_dcterms_replaces','m_dcterms_requires',
    'm_dcterms_rights','m_dcterms_rightsHolder','m_dcterms_source',
    'm_dcterms_spatial','m_dcterms_subject',
    'm_dcterms_tableOfContents','m_dcterms_temporal',
    'm_dcterms_title','m_dcterms_type','m_dcterms_valid',
    'm_description','m_fb_page_id','m_keywords','m_language',
    'm_og_country-name','m_og_description','m_og_email',
    'm_og_fax_number','m_og_image','m_og_latitude','m_og_locality',
    'm_og_longitude','m_og_phone_number','m_og_postal-code',
    'm_og_region','m_og_site_name','m_og_street-address',
    'm_og_title','m_og_type','m_og_url','m_robots',
    'm_twitter_card','m_twitter_creator','m_twitter_creator_id',
    'm_twitter_description','m_twitter_image','m_twitter_image_alt',
    'm_twitter_image_height','m_twitter_image_width','m_twitter_name',
    'm_twitter_player','m_twitter_player_height',
    'm_twitter_player_width','m_twitter_site','m_twitter_site_id',
    'm_twitter_text_title','m_twitter_title','m_twitter_url',
    'mh_cache-control','mh_content-language','mh_expires',
    'mh_pragma','mp_og_country_name','mp_og_description',
    'mp_og_image','mp_og_image_height','mp_og_image_secure_url',
    'mp_og_image_type','mp_og_image_url','mp_og_image_width',
    'mp_og_locale','mp_og_site_name','mp_og_title','mp_og_type',
    'mp_og_updated_time','mp_og_url','mp_og_video',
    'mp_og_video_secure_url','mp_og_video_type','mp_og_video_url',
)
non_std_meta_wl = (
    'm_generator','m_handheldfriendly','m_mobileoptimized',
    'm_viewport','mh_cleartype','m_rating','m_format-detection',
    'm_langid-exists','m_apple-mobile-web-app-capable',
    'm_apple-mobile-web-app-status-bar-style',
    'm_msapplication-tooltip,m_application-name',
)
non_std_http_wl = (
    'h_cache-control','h_transfer-encoding','h_connection',
    'h_accept-ranges','h_etag','h_link','h_p3p',
    'h_strict-transport-security','h_vary','h_x-age',
    'h_x-ah-environment','h_x-content-type-options',
    'h_x-drupal-cache','h_x-frame-options','h_x-generator',
    'h_x-request-id','h_x-ui-compatible','h_x-varnish',
    'h_x-powered-by','h_x-ua-compatible',
)
std_http_wl = (
    'h_age','h_content-language','h_content-length',
    'h_content-type','h_date','h_expires','h_last-modified',
    'h_server','h_set-cookie',
)

fb_wl = (
    'fb_x-funnelback-charset','fb_x-funnelback-content-length',
    'fb_x-funnelback-filtered-content-type','fb_x-funnelback-total-request-time-band-ms',
    'fb_x-funnelback-total-request-time-ms','aa_x-funnelback-aa-checked',
    'aa_x-funnelback-aa-domain','aa_x-funnelback-aa-explicit-failedlevels',
    'aa_x-funnelback-aa-failed-occurrences-on-techniques','aa_x-funnelback-aa-format',
    'aa_x-funnelback-aa-is-affected','aa_x-funnelback-aa-occurrences-of-failing-success-criteria',
    'aa_x-funnelback-aa-occurrences-of-failing-success-criteria-by-level-a',
    'aa_x-funnelback-aa-occurrences-of-failing-success-criteria-by-level-aa',
    'aa_x-funnelback-aa-occurrences-of-failing-success-criteria-by-level-aaa',
    'aa_x-funnelback-aa-occurrences-of-failing-success-criterion-1_1_1',
    'aa_x-funnelback-aa-occurrences-of-failing-success-criterion-1_2_1',
    'aa_x-funnelback-aa-occurrences-of-failing-success-criterion-1_2_2',
    'aa_x-funnelback-aa-occurrences-of-failing-success-criterion-1_2_3',
    'aa_x-funnelback-aa-occurrences-of-failing-success-criterion-1_2_4',
    'aa_x-funnelback-aa-occurrences-of-failing-success-criterion-1_2_5',
    'aa_x-funnelback-aa-occurrences-of-failing-success-criterion-1_2_6',
    'aa_x-funnelback-aa-occurrences-of-failing-success-criterion-1_2_7',
    'aa_x-funnelback-aa-occurrences-of-failing-success-criterion-1_2_8',
    'aa_x-funnelback-aa-occurrences-of-failing-success-criterion-1_2_9',
    'aa_x-funnelback-aa-occurrences-of-failing-success-criterion-1_3_1',
    'aa_x-funnelback-aa-occurrences-of-failing-success-criterion-1_4_2',
    'aa_x-funnelback-aa-occurrences-of-failing-success-criterion-1_4_3',
    'aa_x-funnelback-aa-occurrences-of-failing-success-criterion-1_4_5',
    'aa_x-funnelback-aa-occurrences-of-failing-success-criterion-1_4_6',
    'aa_x-funnelback-aa-occurrences-of-failing-success-criterion-1_4_7',
    'aa_x-funnelback-aa-occurrences-of-failing-success-criterion-1_4_8',
    'aa_x-funnelback-aa-occurrences-of-failing-success-criterion-1_4_9',
    'aa_x-funnelback-aa-occurrences-of-failing-success-criterion-2_1_1',
    'aa_x-funnelback-aa-occurrences-of-failing-success-criterion-2_1_3',
    'aa_x-funnelback-aa-occurrences-of-failing-success-criterion-2_2_1',
    'aa_x-funnelback-aa-occurrences-of-failing-success-criterion-2_4_1',
    'aa_x-funnelback-aa-occurrences-of-failing-success-criterion-2_4_10',
    'aa_x-funnelback-aa-occurrences-of-failing-success-criterion-2_4_2',
    'aa_x-funnelback-aa-occurrences-of-failing-success-criterion-2_4_4',
    'aa_x-funnelback-aa-occurrences-of-failing-success-criterion-2_4_5',
    'aa_x-funnelback-aa-occurrences-of-failing-success-criterion-2_4_6',
    'aa_x-funnelback-aa-occurrences-of-failing-success-criterion-2_4_9',
    'aa_x-funnelback-aa-occurrences-of-failing-success-criterion-3_1_1',
    'aa_x-funnelback-aa-occurrences-of-failing-success-criterion-3_1_2',
    'aa_x-funnelback-aa-occurrences-of-failing-success-criterion-3_2_2',
    'aa_x-funnelback-aa-occurrences-of-failing-success-criterion-3_3_1',
    'aa_x-funnelback-aa-occurrences-of-failing-success-criterion-3_3_2',
    'aa_x-funnelback-aa-occurrences-of-failing-success-criterion-4_1_1',
    'aa_x-funnelback-aa-occurrences-of-failing-success-criterion-4_1_2',
    'aa_x-funnelback-aa-occurrences-of-technique-aria1','aa_x-funnelback-aa-occurrences-of-technique-aria10',
    'aa_x-funnelback-aa-occurrences-of-technique-aria11','aa_x-funnelback-aa-occurrences-of-technique-aria12',
    'aa_x-funnelback-aa-occurrences-of-technique-aria16','aa_x-funnelback-aa-occurrences-of-technique-aria17',
    'aa_x-funnelback-aa-occurrences-of-technique-aria19','aa_x-funnelback-aa-occurrences-of-technique-aria4',
    'aa_x-funnelback-aa-occurrences-of-technique-aria5','aa_x-funnelback-aa-occurrences-of-technique-f23',
    'aa_x-funnelback-aa-occurrences-of-technique-f25','aa_x-funnelback-aa-occurrences-of-technique-f54',
    'aa_x-funnelback-aa-occurrences-of-technique-f68','aa_x-funnelback-aa-occurrences-of-technique-f74',
    'aa_x-funnelback-aa-occurrences-of-technique-f75','aa_x-funnelback-aa-occurrences-of-technique-f77',
    'aa_x-funnelback-aa-occurrences-of-technique-f8','aa_x-funnelback-aa-occurrences-of-technique-f84',
    'aa_x-funnelback-aa-occurrences-of-technique-f89','aa_x-funnelback-aa-occurrences-of-technique-flash18',
    'aa_x-funnelback-aa-occurrences-of-technique-flash26','aa_x-funnelback-aa-occurrences-of-technique-flash9',
    'aa_x-funnelback-aa-occurrences-of-technique-g1','aa_x-funnelback-aa-occurrences-of-technique-g115',
    'aa_x-funnelback-aa-occurrences-of-technique-g130','aa_x-funnelback-aa-occurrences-of-technique-g133',
    'aa_x-funnelback-aa-occurrences-of-technique-g140','aa_x-funnelback-aa-occurrences-of-technique-g141',
    'aa_x-funnelback-aa-occurrences-of-technique-g148','aa_x-funnelback-aa-occurrences-of-technique-g151',
    'aa_x-funnelback-aa-occurrences-of-technique-g157','aa_x-funnelback-aa-occurrences-of-technique-g158',
    'aa_x-funnelback-aa-occurrences-of-technique-g159','aa_x-funnelback-aa-occurrences-of-technique-g166',
    'aa_x-funnelback-aa-occurrences-of-technique-g170','aa_x-funnelback-aa-occurrences-of-technique-g171',
    'aa_x-funnelback-aa-occurrences-of-technique-g173','aa_x-funnelback-aa-occurrences-of-technique-g54',
    'aa_x-funnelback-aa-occurrences-of-technique-g56','aa_x-funnelback-aa-occurrences-of-technique-g58',
    'aa_x-funnelback-aa-occurrences-of-technique-g60','aa_x-funnelback-aa-occurrences-of-technique-g69',
    'aa_x-funnelback-aa-occurrences-of-technique-g78','aa_x-funnelback-aa-occurrences-of-technique-g8',
    'aa_x-funnelback-aa-occurrences-of-technique-g81','aa_x-funnelback-aa-occurrences-of-technique-g87',
    'aa_x-funnelback-aa-occurrences-of-technique-g88','aa_x-funnelback-aa-occurrences-of-technique-g9',
    'aa_x-funnelback-aa-occurrences-of-technique-g91','aa_x-funnelback-aa-occurrences-of-technique-g93',
    'aa_x-funnelback-aa-occurrences-of-technique-h2','aa_x-funnelback-aa-occurrences-of-technique-h24',
    'aa_x-funnelback-aa-occurrences-of-technique-h25','aa_x-funnelback-aa-occurrences-of-technique-h30',
    'aa_x-funnelback-aa-occurrences-of-technique-h32','aa_x-funnelback-aa-occurrences-of-technique-h33',
    'aa_x-funnelback-aa-occurrences-of-technique-h37','aa_x-funnelback-aa-occurrences-of-technique-h39',
    'aa_x-funnelback-aa-occurrences-of-technique-h42','aa_x-funnelback-aa-occurrences-of-technique-h43',
    'aa_x-funnelback-aa-occurrences-of-technique-h44','aa_x-funnelback-aa-occurrences-of-technique-h49',
    'aa_x-funnelback-aa-occurrences-of-technique-h53','aa_x-funnelback-aa-occurrences-of-technique-h57',
    'aa_x-funnelback-aa-occurrences-of-technique-h58','aa_x-funnelback-aa-occurrences-of-technique-h63',
    'aa_x-funnelback-aa-occurrences-of-technique-h64','aa_x-funnelback-aa-occurrences-of-technique-h65',
    'aa_x-funnelback-aa-occurrences-of-technique-h67','aa_x-funnelback-aa-occurrences-of-technique-h71',
    'aa_x-funnelback-aa-occurrences-of-technique-h73','aa_x-funnelback-aa-occurrences-of-technique-h85',
    'aa_x-funnelback-aa-occurrences-of-technique-h91','aa_x-funnelback-aa-occurrences-of-technique-h93',
    'aa_x-funnelback-aa-occurrences-of-technique-pdf1','aa_x-funnelback-aa-occurrences-of-technique-pdf16',
    'aa_x-funnelback-aa-occurrences-of-technique-pdf18','aa_x-funnelback-aa-occurrences-of-technique-pdf2',
    'aa_x-funnelback-aa-occurrences-of-technique-sm1','aa_x-funnelback-aa-occurrences-of-technique-sm11',
    'aa_x-funnelback-aa-occurrences-of-technique-sm12','aa_x-funnelback-aa-occurrences-of-technique-sm13',
    'aa_x-funnelback-aa-occurrences-of-technique-sm14','aa_x-funnelback-aa-occurrences-of-technique-sm2',
    'aa_x-funnelback-aa-occurrences-of-technique-sm6','aa_x-funnelback-aa-occurrences-of-technique-sm7',
    'aa_x-funnelback-aa-occurrences-of-unique-failing-success-criterions',
    'aa_x-funnelback-aa-occurrencesoffailingtechniques',
    'aa_x-funnelback-aa-possibility_of_failure-occurrences-on-techniques',
    'aa_x-funnelback-aa-passedlevel-a','aa_x-funnelback-aa-passedlevel-aa',
    'aa_x-funnelback-aa-passedlevel-aaa','aa_x-funnelback-aa-passedlevels',
    'aa_x-funnelback-aa-suspected_failure-occurrences-on-techniques',
    'aa_x-funnelback-aa-set-of-failing-principles','aa_x-funnelback-aa-set-of-failing-success-criterions',
    'aa_x-funnelback-aa-set-of-failing-techniques','aa_x-funnelback-aa-techniquesareaffectedby',
    'aa_x-funnelback-aa-unaffected','ca_x-funnelback-raw-flesch-kincaid-readability-grade',
    'ca_x-funnelback-rounded-flesch-kincaid-readability-grade',
    'ca_x-funnelback-title-for-duplicate-detection','ca_x-funnelback-undesirable-text',
)
dta_wl = (
    'DOCURL','HOST','PORTFOLIO','REPORT_ID','3LD','m_x-dta-agds','m_x-dta-agds-count','m_x-dta-uikit',
    'm_x-dta-uikit-count','m_x-dta-captcha','m_x-dta-captcha-count','m_x-dta-twitter',
    'm_x-dta-twitter-count','m_x-dta-facebook','m_x-dta-facebook-count','m_x-dta-canonical',
    'm_x-dta-canonical-count','m_x-dta-ga-id','m_x-dta-ga-360-id','m_x-dta-reported-lang',
    'm_x-dta-detected-lang','m_x-funnelback-twitter-hash-tags','m_x-funnelback-twitter-user-tags',
    'm_x-dta-links-clickhere','m_x-dta-links-clickhere-value','m_x-dta-links-clickhere-count',
    'm_x-dta-h1-count','m_x-dta-title-length','m_x-dta-title-length-size','m_x-dta-weasel-words',
    'm_x-dta-weasel-words-count','m_x-dta-plain-english','m_x-dta-plain-english-count',
)

white_keys = std_meta_wl + non_std_meta_wl + non_std_http_wl + std_http_wl + fb_wl + dta_wl


def json_lines_bk_iter(fle):
    for line in fle:
        if isinstance(line, str):
            j = json.loads(line)
        else:
            j = json.loads(line.decode('utf-8'))
        wanted = { k: v for k, v in j.items() if k in white_keys }
        yield wanted


def dump_lines(lines, file_path):
    for line in lines:
        if line == {}:
            continue
        with open(file_path, 'a+') as f:
            f.write(json.dumps(line) + '\n')
            

if __name__=='__main__':
    fp = '/Users/jgriffithshawking/dtadata/refilter-10-10/metadata-report01-01.json'
    lines = json_lines_bk_iter(open(fp))

    file_path = '/Users/jgriffithshawking/dtadata/testbatch/refilter-10-10.json'
    dump_lines(lines, file_path)
