"""
call_schema.py - contains the CALL_SCHEMA lookup for the qualysdk package.

The CALL_SCHEMA dictionary contains the schema for each Qualys API call. 
This schema is used to determine what parameters are required for each call and where/how
they should be sent to the API.
"""

from frozendict import frozendict

# frozen schema for all calls:
CALL_SCHEMA = frozendict(
    {
        "gav": {
            "url_type": "gateway",
            "count_assets": {
                "endpoint": "/am/v1/assets/host/count",
                "method": ["POST"],
                "valid_params": ["filter", "lastSeenAssetId", "lastModifiedDate"],
                "valid_POST_data": [],
                "use_requests_json_data": False,
                "return_type": "json",
                "pagination": False,
                "auth_type": "token",
            },
            "get_all_assets": {
                "endpoint": "/am/v1/assets/host/list",
                "method": ["POST"],
                "valid_params": [
                    "excludeFields",
                    "includeFields",
                    "lastModifiedDate",
                    "lastSeenAssetId",
                    "pageSize",
                ],
                "valid_POST_data": [],
                "use_requests_json_data": False,
                "return_type": "json",
                "pagination": True,
                "auth_type": "token",
            },
            "get_asset": {
                "endpoint": "/am/v1/asset/host/id",
                "method": ["POST"],
                "valid_params": ["excludeFields", "includeFields", "assetId"],
                "valid_POST_data": [],
                "use_requests_json_data": False,
                "return_type": "json",
                "pagination": False,
                "auth_type": "token",
            },
            "query_assets": {
                "endpoint": "/am/v1/assets/host/filter/list",
                "method": ["POST"],
                "valid_params": [
                    "filter",
                    "excludeFields",
                    "includeFields",
                    "lastModifiedDate",
                    "lastSeenAssetId",
                    "pageSize",
                ],
                "valid_POST_data": [],
                "use_requests_json_data": False,
                "return_type": "json",
                "pagination": True,
                "auth_type": "token",
            },
        },
        "vmdr": {
            "url_type": "api",
            "query_kb": {
                "endpoint": "/api/2.0/fo/knowledge_base/vuln/",
                "method": ["GET", "POST"],
                "valid_params": [
                    "action",
                    "code_modified_after",
                    "code_modified_before",
                    "echo_request",
                    "details",
                    "ids",
                    "id_min",
                    "id_max",
                    "is_patchable",
                    "last_modified_after",
                    "last_modified_before",
                    "last_modified_by_user_after",
                    "last_modified_by_user_before",
                    "last_modified_by_service_after",
                    "last_modified_by_service_before",
                    "published_after",
                    "published_before",
                    "discovery_method",
                    "discovery_auth_types",
                    "show_pci_reasons",
                    "show_supported_modules_info",
                    "show_disabled_flag",
                    "show_qid_change_log",
                ],
                "valid_POST_data": [],
                "use_requests_json_data": False,
                "return_type": "xml",
                "pagination": False,
                "auth_type": "basic",
            },
            "get_host_list": {
                "endpoint": "/api/2.0/fo/asset/host/",
                "method": ["GET", "POST"],
                "valid_params": [
                    "action",
                    "echo_request",
                    "show_asset_id",
                    "details",
                    "os_pattern",
                    "truncation_limit",
                    "ips",
                    "ipv6",
                    "ag_ids",
                    "ag_titles",
                    "ids",
                    "id_min",
                    "id_max",
                    "network_ids",
                    "compliance_enabled",
                    "no_vm_scan_since",
                    "no_compliance_scan_since",
                    "vm_scan_since",
                    "compliance_scan_since",
                    "vm_processed_before",
                    "vm_processed_after",
                    "vm_scan_date_before",
                    "vm_scan_date_after",
                    "vm_auth_scan_date_before",
                    "vm_auth_scan_date_after",
                    "scap_scan_since",
                    "no_scap_scan_since",
                    "use_tags",
                    "show_tags",
                    "tag_set_by",
                    "tag_include_selector",
                    "tag_exclude_selector",
                    "tag_set_include",
                    "tag_set_exclude",
                    "show_ars",
                    "ars_min",
                    "ars_max",
                    "show_ars_factors",
                    "show_trurisk",
                    "trurisk_min",
                    "trurisk_max",
                    "show_trurisk_factors",
                    "host_metadata",
                    "host_metadata_fields",
                    "show_cloud_tags",
                    "cloud_tag_fields",
                ],
                "valid_POST_data": [],
                "use_requests_json_data": False,
                "return_type": "xml",
                "pagination": True,
                "auth_type": "basic",
            },
            "get_hld": {
                "endpoint": "/api/2.0/fo/asset/host/vm/detection/",
                "method": ["GET", "POST"],
                "valid_params": [
                    "action",
                    "echo_request",
                    "show_asset_id",
                    "show_results",
                    "include_vuln_type",
                    "arf_kernel_filter",
                    "arf_service_filter",
                    "arf_config_filter",
                    "active_kernels_only",
                    "output_format",
                    "suppress_duplicated_data_from_csv",
                    "truncation_limit",
                    "max_days_since_detection_updated",
                    "detection_updated_since",
                    "detection_updated_before",
                    "detection_processed_before",
                    "detection_processed_after",
                    "detection_last_tested_since",
                    "detection_last_tested_since_days",
                    "detection_last_tested_before",
                    "detection_last_tested_before_days",
                    "include_ignored",
                    "include_disabled",
                    "ids",
                    "id_min",
                    "id_max",
                    "ips",
                    "ipv6",
                    "ag_ids",
                    "ag_titles",
                    "network_ids",
                    "network_name",
                    "vm_scan_since",
                    "no_vm_scan_since",
                    "max_days_since_last_vm_scan",
                    "vm_processed_before",
                    "vm_processed_after",
                    "vm_scan_date_before",
                    "vm_scan_date_after",
                    "vm_auth_scan_date_before",
                    "vm_auth_scan_date_after",
                    "status",
                    "compliance_enabled",
                    "os_pattern",
                    "qids",
                    "severities",
                    "filter_superseded_qids",
                    "include_search_list_titles",
                    "exclude_search_list_titles",
                    "include_search_list_ids",
                    "exclude_search_list_ids",
                    "use_tags",
                    "tag_set_by",
                    "tag_include_selector",
                    "tag_exclude_selector",
                    "tag_set_include",
                    "tag_set_exclude",
                    "show_tags",
                    "show_qds",
                    "qds_min",
                    "qds_max",
                    "show_qds_factors",
                    "host_metadata",
                    "host_metadata_fields",
                    "show_cloud_tags",
                    "cloud_tag_fields",
                ],
                "valid_POST_data": [],
                "use_requests_json_data": False,
                "return_type": "xml",
                "pagination": True,
                "auth_type": "basic",
            },
            "get_ip_list": {
                "endpoint": "/api/2.0/fo/asset/ip/",
                "method": ["GET", "POST"],
                "valid_params": [
                    "action",
                    "echo_request",
                    "ips",
                    "network_id",
                    "tracking_method",
                    "compliance_enabled",
                    "certview_enabled",
                ],
                "valid_POST_data": [],
                "use_requests_json_data": False,
                "return_type": "xml",
                "pagination": False,
                "auth_type": "basic",
            },
            "add_ips": {
                "endpoint": "/api/2.0/fo/asset/ip/",
                "method": ["POST"],
                "valid_params": [],
                "valid_POST_data": [
                    "action",
                    "echo_request",
                    "ips",
                    "tracking_method",
                    "enable_vm",
                    "enable_pc",
                    "owner",
                    "ud1",
                    "ud2",
                    "ud3",
                    "comment",
                    "ag_title",
                    "enable_certview",
                    "enable_sca",
                ],
                "use_requests_json_data": False,
                "return_type": "xml",
                "pagination": False,
                "auth_type": "basic",
            },
            "update_ips": {
                "endpoint": "/api/2.0/fo/asset/ip/",
                "method": ["POST"],
                "valid_params": [],
                "valid_POST_data": [
                    "action",
                    "echo_request",
                    "ips",
                    "network_id",
                    "tracking_method",
                    "host_dns",
                    "host_netbios",
                    "owner",
                    "ud1",
                    "ud2",
                    "ud3",
                    "comment",
                ],
                "use_requests_json_data": False,
                "return_type": "xml",
                "pagination": False,
                "auth_type": "basic",
            },
            "get_ag_list": {
                "endpoint": "/api/2.0/fo/asset/group/",
                "method": ["GET", "POST"],
                "valid_params": [
                    "action",
                    "echo_request",
                    "output_format",
                    "ids",
                    "id_min",
                    "id_max",
                    "truncation_limit",
                    "network_ids",
                    "unit_id",
                    "user_id",
                    "title",
                    "show_attributes",
                ],
                "valid_POST_data": [],
                "use_requests_json_data": False,
                "return_type": "xml",
                "pagination": True,
                "auth_type": "basic",
            },
            "manage_ag": {  # called by add_ag, update_ag, delete_ag
                "endpoint": "/api/2.0/fo/asset/group/",
                "method": ["POST"],
                "valid_params": [],
                "valid_POST_data": [
                    "action",
                    "id",
                    "echo_request",
                    "title",
                    "comments",
                    "division",
                    "function",
                    "location",
                    "business_impact",
                    "ips",
                    "appliance_ids",
                    "default_appliance_id",
                    "domains",
                    "dns_names",
                    "netbios_names",
                    "cvss_enviro_cdp",
                    "cvss_enviro_td",
                    "cvss_enviro_cr",
                    "cvss_enviro_ir",
                    "cvss_enviro_ar",
                    "set_comments",
                    "set_division",
                    "set_function",
                    "set_location",
                    "set_business_impact",
                    "add_ips",
                    "remove_ips",
                    "set_ips",
                    "add_appliance_ids",
                    "remove_appliance_ids",
                    "set_appliance_ids",
                    "set_default_appliance_id",
                    "add_domains",
                    "remove_domains",
                    "set_domains",
                    "add_dns_names",
                    "remove_dns_names",
                    "set_dns_names",
                    "add_netbios_names",
                    "remove_netbios_names",
                    "set_netbios_names",
                    "set_title",
                    "set_cvss_enviro_cdp",
                    "set_cvss_enviro_td",
                    "set_cvss_enviro_cr",
                    "set_cvss_enviro_ir",
                    "set_cvss_enviro_ar",
                ],
                "use_requests_json_data": False,
                "return_type": "xml",
                "pagination": False,
                "auth_type": "basic",
            },
            "list_scans": {
                "endpoint": "/api/2.0/fo/scan/",
                "method": ["GET", "POST"],
                "valid_params": [
                    "action",
                    "echo_request",
                    "scan_ref",
                    "state",
                    "processed",
                    "type",
                    "target",
                    "user_login",
                    "launched_after_datetime",
                    "launched_before_datetime",
                    "scan_type",
                    "client_id",
                    "client_name",
                    "show_ags",
                    "show_op",
                    "show_status",
                    "ignore_target",
                    "show_last",
                ],
                "valid_POST_data": [],
                "use_requests_json_data": False,
                "return_type": "xml",
                "pagination": False,
                "auth_type": "basic",
            },
            "launch_scan": {
                "endpoint": "/api/2.0/fo/scan/",
                "method": ["POST"],
                "valid_params": [],
                "valid_POST_data": [
                    "action",
                    "echo_request",
                    "runtime_http_header",
                    "scan_title",
                    "option_id",
                    "option_title",
                    "iscanner_id",
                    "iscanner_name",
                    "ec2_instance_ids",
                    "ip",
                    "asset_group_ids",
                    "asset_groups",
                    "exclude_ip_per_scan",
                    "default_scanner",
                    "scanners_in_ag",
                    "scanners_in_network",  # set to 1 to use all scanners
                    "target_from"  # must be tags
                    "use_ip_nt_range_tags_include",
                    "use_ip_nt_range_tags_exclude",
                    "use_ip_nt_range_tags",
                    "tag_include_selector",
                    "tag_exclude_selector",
                    "tag_set_by",
                    "tag_set_exclude",
                    "tag_set_include",
                    "ip_network_id",  # must be enabled in subscription
                    "client_id",  # only for consultant subscriptions
                    "client_name",  # only for consultant subscriptions
                    "fqdn",
                    "connector_name",
                    "ec2_endpoint",
                ],
                "use_requests_json_data": False,
                "return_type": "xml",
                "pagination": False,
                "auth_type": "basic",
            },
            "pause_scan": {
                "endpoint": "/api/2.0/fo/scan/",
                "method": ["POST"],
                "valid_params": [],
                "valid_POST_data": ["action", "echo_request", "scan_ref"],
                "use_requests_json_data": False,
                "return_type": "xml",
                "pagination": False,
                "auth_type": "basic",
            },
            "resume_scan": {
                "endpoint": "/api/2.0/fo/scan/",
                "method": ["POST"],
                "valid_params": [],
                "valid_POST_data": ["action", "echo_request", "scan_ref"],
                "use_requests_json_data": False,
                "return_type": "xml",
                "pagination": False,
                "auth_type": "basic",
            },
            "cancel_scan": {
                "endpoint": "/api/2.0/fo/scan/",
                "method": ["POST"],
                "valid_params": [],
                "valid_POST_data": ["action", "echo_request", "scan_ref"],
                "use_requests_json_data": False,
                "return_type": "xml",
                "pagination": False,
                "auth_type": "basic",
            },
            "delete_scan": {
                "endpoint": "/api/2.0/fo/scan/",
                "method": ["POST"],
                "valid_params": [],
                "valid_POST_data": ["action", "echo_request", "scan_ref"],
                "use_requests_json_data": False,
                "return_type": "xml",
                "pagination": False,
                "auth_type": "basic",
            },
            "fetch_scan": {
                "endpoint": "/api/2.0/fo/scan/",
                "method": ["POST"],
                "valid_params": [],
                "valid_POST_data": [
                    "action",
                    "echo_request",
                    "scan_ref",
                    "ips",
                    "mode",
                    "client_id",
                    "client_name",
                    "output_format",
                ],
                "use_requests_json_data": False,
                "return_type": "json",
                "pagination": False,
                "auth_type": "basic",
            },
            "get_scanner_list": {
                "endpoint": "/api/2.0/fo/appliance/",
                "method": ["GET", "POST"],
                "valid_params": [
                    "action",  # set to "list"
                    "echo_request",  # set to False
                    "output_mode",
                    "scan_detail",
                    "show_tags",
                    "include_cloud_info",
                    "busy",
                    "scan_ref",
                    "name",
                    "ids",
                    "include_license_info",  # set to False
                    "type",
                    "platform_provider",
                ],
                "valid_POST_data": [],
                "use_requests_json_data": False,
                "return_type": "xml",
                "pagination": False,
                "auth_type": "basic",
            },
            "get_static_searchlists": {
                "endpoint": "/api/2.0/fo/qid/search_list/static/",
                "method": ["GET"],
                "valid_params": ["action", "echo_request", "ids"],
                "valid_POST_data": [],
                "use_requests_json_data": False,
                "return_type": "xml",
                "pagination": False,
                "auth_type": "basic",
            },
            "get_dynamic_searchlists": {
                "endpoint": "/api/2.0/fo/qid/search_list/dynamic/",
                "method": ["GET"],
                "valid_params": [
                    "action",
                    "echo_request",
                    "ids",
                    "show_qids",
                    "show_option_profiles",
                    "show_distribution_groups",
                    "show_report_templates",
                    "show_remediation_policies",
                ],
                "valid_POST_data": [],
                "use_requests_json_data": False,
                "return_type": "xml",
                "pagination": False,
                "auth_type": "basic",
            },
            "get_report_list": {
                "endpoint": "/api/2.0/fo/report/",
                "method": ["GET", "POST"],
                "valid_params": [
                    "action",
                    "echo_request",
                    "id",
                    "state",
                    "user_login",
                    "expires_before_datetime",
                    "client_id",
                    "client_name",
                ],
                "valid_POST_data": [],
                "use_requests_json_data": False,
                "return_type": "xml",
                "pagination": False,
                "auth_type": "basic",
            },
            "launch_report": {
                "endpoint": "/api/2.0/fo/report/",
                "method": ["POST"],
                "valid_params": [],
                "valid_POST_data": [
                    "action",  # set to "launch"
                    "echo_request",  # set to False
                    "template_id",
                    "report_title",
                    "output_format",
                    "hide_header",  # Set to True to hide header!!!
                    "pdf_password",
                    "recipient_group",
                    "recipient_group_id",
                    "recipient_group_id",
                    "report_type",  # Important! map, scan, etc.
                    # MAP REPORT:
                    "domain",
                    "ip_restriction",
                    "report_refs",
                    # SCAN REPORT:
                    "ips",
                    "asset_group_ids",
                    "ips_network_id",
                    # PATCH REPORT:
                    # "ips",
                    # "asset_group_ids",
                    # REMEDITION REPORT:
                    # "ips",
                    # "asset_group_ids",
                    "assignee_type",  # User,All
                    # COMPLIANCE REPORT:
                    "policy_id",
                    # asset_group_ids,
                    # "ips",
                    "host_id",
                    "instance_string",
                    # FOR USING ASSET TAGS:
                    "use_tags",
                    "tag_include_selector",
                    "tag_exclude_selector",
                    "tag_set_by",
                    "tag_set_include",
                    "tag_set_exclude",
                ],
                "use_requests_json_data": False,
                "return_type": "xml",
                "pagination": False,
                "auth_type": "basic",
            },
            "get_template_list": {
                "endpoint": "/msp/report_template_list.php",
                "method": ["GET", "POST"],
                "valid_params": [],
                "valid_POST_data": [],
                "use_requests_json_data": False,
                "return_type": "xml",
                "pagination": False,
                "auth_type": "basic",
            },
            "cancel_report": {
                "endpoint": "/api/2.0/fo/report/",
                "method": ["POST"],
                "valid_params": [],
                "valid_POST_data": ["action", "echo_request", "id"],
                "use_requests_json_data": False,
                "return_type": "xml",
                "pagination": False,
                "auth_type": "basic",
            },
            "fetch_report": {
                "endpoint": "/api/2.0/fo/report/",
                "method": ["GET", "POST"],
                "valid_params": ["action", "echo_request", "id"],
                "valid_POST_data": [],
                "use_requests_json_data": False,
                "return_type": "xml",
                "pagination": False,
                "auth_type": "basic",
            },
            "delete_report": {
                "endpoint": "/api/2.0/fo/report/",
                "method": ["POST"],
                "valid_params": [],
                "valid_POST_data": ["action", "echo_request", "id"],
                "use_requests_json_data": False,
                "return_type": "xml",
                "pagination": False,
                "auth_type": "basic",
            },
            "get_scheduled_report_list": {
                "endpoint": "/api/2.0/fo/schedule/report/",
                "method": ["GET", "POST"],
                "valid_params": ["action", "id", "echo_request", "is_active"],
                "valid_POST_data": [],
                "use_requests_json_data": False,
                "return_type": "xml",
                "pagination": False,
                "auth_type": "basic",
            },
            "launch_scheduled_report": {
                "endpoint": "/api/2.0/fo/schedule/report/",
                "method": ["POST"],
                "valid_params": [],
                "valid_POST_data": ["action", "echo_request", "id"],
                "use_requests_json_data": False,
                "return_type": "xml",
                "pagination": False,
                "auth_type": "basic",
            },
            "get_user_list": {
                "endpoint": "/msp/user_list.php",
                "method": ["GET", "POST"],
                "valid_params": ["external_id_contains", "external_id_assigned"],
                "valid_POST_data": [],
                "use_requests_json_data": False,
                "return_type": "xml",
                "pagination": False,
                "auth_type": "basic",
            },
            "add_user": {
                "endpoint": "/msp/user.php",
                "method": ["GET", "POST"],
                "valid_params": [
                    "action",
                    "user_role",
                    "business_unit",
                    "first_name",
                    "last_name",
                    "title",
                    "phone",
                    "email",
                    "address1",
                    "city",
                    "country",
                    "state",
                    "send_email",
                    "asset_groups",
                    "fax",
                    "address2",
                    "zip_code",
                    "external_id",
                ],
                "valid_POST_data": [],
                "use_requests_json_data": False,
                "return_type": "xml",
                "pagination": False,
                "auth_type": "basic",
            },
            "edit_user": {
                "endpoint": "/msp/user.php",
                "method": ["GET", "POST"],
                "valid_params": [
                    "action",
                    "login",
                    "asset_groups",
                    "first_name",
                    "last_name",
                    "title",
                    "phone",
                    "email",
                    "address1",
                    "address2",
                    "city",
                    "country",
                    "state",
                    "fax",
                    "zip_code",
                    "external_id",
                ],
                "valid_POST_data": [],
                "use_requests_json_data": False,
                "return_type": "xml",
                "pagination": False,
                "auth_type": "basic",
            },
            "get_kb_qvs": {
                "endpoint": "/api/2.0/fo/knowledge_base/qvs/",
                "method": ["GET", "POST"],
                "valid_params": [
                    "action",
                    "details",
                    "cve",
                    "qvs_last_modified_before",
                    "qvs_last_modified_after",
                    "qvs_min",
                    "qvs_max",
                    "nvd_published_before",
                    "nvd_published_after",
                ],
                "valid_POST_data": [],
                "use_requests_json_data": False,
                "return_type": "json",
                "pagination": False,
                "auth_type": "basic",
            },
            "get_activity_log": {
                "endpoint": "/api/2.0/fo/activity_log",
                "method": ["GET", "POST"],
                "valid_params": [
                    "action",
                    "user_action",
                    "action_details",
                    "username",
                    "since_datetime",
                    "until_datetime",
                    "user_role",
                    "id_max",
                    "truncation_limit",
                    "output_format",
                ],
                "valid_POST_data": [],
                "use_requests_json_data": False,
                "return_type": "xml",
                "pagination": True,
                "auth_type": "basic",
            },
            "purge_hosts": {
                "endpoint": "/api/2.0/fo/asset/host/",
                "method": ["POST"],
                "valid_params": [
                    "action",
                    "echo_request",
                    "ids",
                    "ips",
                    "ag_ids",
                    "ag_titles",
                    "network_ids",
                    "no_vm_scan_since",
                    "no_compliance_scan_since",
                    "data_scope",
                    "compliance_enabled",
                    "os_pattern",
                ],
                "valid_POST_data": [],
                "use_requests_json_data": False,
                "return_type": "xml",
                "pagination": False,
                "auth_type": "basic",
            },
        },
        "cloud_agent": {
            "url_type": "api",
            "purge_agent": {
                "endpoint": "/qps/rest/2.0/uninstall/am/asset/{placeholder}",  # assetId
                "method": ["POST"],
                "valid_params": [],
                "valid_POST_data": ["placeholder", "_xml_data"],
                "use_requests_json_data": False,
                "return_type": "xml",
                "pagination": False,
                "auth_type": "basic",
                "_xml_data": True,
            },
            "bulk_purge_agent": {
                "endpoint": "/qps/rest/2.0/uninstall/am/asset",
                "method": ["POST"],
                "valid_params": [],
                "valid_POST_data": ["_xml_data"],
                "use_requests_json_data": False,
                "return_type": "xml",
                "pagination": False,
                "auth_type": "basic",
                "_xml_data": True,
            },
            "list_agents": {
                "endpoint": "/qps/rest/2.0/search/am/hostasset",
                "method": ["POST"],
                "valid_params": [],
                "valid_POST_data": ["_xml_data"],
                "use_requests_json_data": False,
                "return_type": "xml",
                "pagination": True,
                "auth_type": "basic",
                "_xml_data": True,
            },
            "launch_ods": {
                "endpoint": "/qps/rest/1.0/ods/ca/agentasset/{placeholder}",
                "method": ["POST"],
                "valid_params": ["scan", "overrideConfigCpu"],
                "valid_POST_data": ["placeholder", "_xml_data"],
                "use_requests_json_data": False,
                "return_type": "xml",
                "pagination": False,
                "auth_type": "basic",
                "_xml_data": True,
            },
            "bulk_launch_ods": {
                "endpoint": "/qps/rest/1.0/ods/ca/agentasset",
                "method": ["POST"],
                "valid_params": ["scan", "overrideConfigCpu"],
                "valid_POST_data": ["_xml_data"],
                "use_requests_json_data": False,
                "return_type": "xml",
                "pagination": False,
                "auth_type": "basic",
                "_xml_data": True,
            },
        },
    }
)
