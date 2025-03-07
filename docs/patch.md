# Patch Management APIs

PM APIs return data on patches, asset patch status/compliance, and patch jobs.

>**Head's Up!:** Qualys does not support MacOS for the patch management API.

After running:
```py
from qualysdk.pm import *
```

You can use any of the endpoints currently supported:

## PM Endpoints

|API Call| Description |
|--|--|
| ```get_version``` | Returns the version of the PM API. |
| ```list_jobs``` | Returns jobs that match given kwargs. |
| ```get_job_results``` | Returns a summary of a job. |
| ```get_job_runs``` | Returns a list of runs of a job. |
| ```create_job```| Creates a new job. |
| ```delete_job``` | Deletes a job or a list of jobs. |
| ```change_job_status``` | Enable/disable a job or a list of jobs. |
| ```lookup_cves``` | Returns a list of CVEs and other details associated with a QID. |
| ```get_patches``` | Returns a list of patches. |
| ```get_assets``` | Returns a list of assets. |
| ```get_patch_count``` | Returns the number of patches for a given platform that match ```query``` and ```havingQuery```. |
| ```get_asset_count``` | Returns the number of assets for a given platform that match ```query``` and ```havingQuery```. |
| ```lookup_host_uuids``` | Returns a list of tuples, containing host UUIDs for a given list of asset IDs. |
| ```get_patch_catalog``` | Returns the patch catalog for a given platform according to ```patchId```. |
| ```get_packages_in_linux_patch``` | Returns the packages associated with a Linux patch. |
| ```get_products_in_windows_patch``` | Returns the products associated with a Windows patch. |
| ```count_product_vulns``` | Return the number of vulns (active and fixed) from products in your environment. |

## Get PM Version API

```get_version``` returns the version of the PM API.

|Parameter| Possible Values |Description| Required|
|--|--|--|--|
|```auth```|```qualysdk.auth.TokenAuth``` | Authentication object | ✅ |

```py
from qualysdk.auth import TokenAuth
from qualysdk.pm import get_version

auth = TokenAuth(<username>, <password>, platform='qg1')
get_version(auth)
>>>"3.1.0.0-29"
```

## List Jobs API

```list_jobs``` returns a ```BaseList``` of patch management jobs in the user's account that match the given kwargs. if ```platform='all'```, it uses threading to speed up the process.

>**Head's Up!:** For the ```filter``` kwarg, see the linked documentation for the possible values: [Windows Jobs](https://docs.qualys.com/en/pm/3.1.0.0/search_tips/ui_jobs_list.htm), [Linux Jobs](https://docs.qualys.com/en/pm/3.1.0.0/search_tips/search_linux_jobs.htm)

|Parameter| Possible Values |Description| Required|
|--|--|--|--|
|```auth```|```qualysdk.auth.TokenAuth``` | Authentication object | ✅ |
| ```platform``` | ```Literal['all', 'windows', 'linux']='all'``` | The platform of the job | ❌ |
| ```page_count``` | ```Union[int, "all"] = "all"``` | The number of pages to return | ❌ |
| ```filter``` | ```str``` | The QQL filter to search for jobs | ❌ |
| ```attributes``` | ```str``` | The attributes to return in the response as a comma-separated string | ❌ |
| ```coauthorJob``` | ```bool=False``` | Only include jobs where the user is a coauthor | ❌ |
| ```ownedJob``` | ```bool=False``` | Only include jobs where the user is the sole owner | ❌ |
| ```pageSize``` | ```int=10``` | The number of jobs to return per page | ❌ |

```py
from qualysdk.auth import TokenAuth
from qualysdk.pm import list_jobs

auth = TokenAuth(<username>, <password>, platform='qg1')

# Get all Windows jobs:
win_jobs = list_jobs(auth, 'windows')
>>>[
    PMJob(
        name="My Job", 
        id="<job_guid>", 
        platform="Windows", 
        ...
    ), 
    ...
]
```

## Get Job Results API

```get_job_results``` returns the results of a patch management job.

|Parameter| Possible Values |Description| Required|
|--|--|--|--|
|```auth```|```qualysdk.auth.TokenAuth``` | Authentication object | ✅ |
| ```jobId``` | ```Union[str, BaseList[PMJob, str]]``` | The ID(s) of the job to get results for. If a ```BaseList``` of ```PMJob``` objects is passed, the function will use threading. | ✅ |
| ```jobInstanceId``` | ```str``` | The ID of the job instance to get results for. Should not be used with threading. | ❌ |
| ```pageSize``` | ```int=10``` | The number of results to return per page | ❌ |
| ```sort``` | ```str``` | The field to sort the results by | ❌ |

```py
from qualysdk.auth import TokenAuth
from qualysdk.pm import get_job_results, list_jobs

auth = TokenAuth(<username>, <password>, platform='qg1')

# Get some job:
job = list_jobs(auth, 'linux')[0]

# Get the results summary for the job:
results = get_job_results(auth, job.id)
>>>JobResultSummary(
    id='11111111-2222-3333-4444-555555555555', 
    name='My Job', 
    assetCount=1, 
    patchCount=1, 
    createdBy=<username>, 
    createdOn=datetime.datetime(2020, 1, 2, 3, 12, 30, 777000), 
    assets=[
        PMAssetJobView(
            id='aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee',
            name='Patch Asset', 
            operatingSystem='Red Hat Enterprise Linux 9.5',
            ...
        )
    ]
)

# Threading example:
jobs = list_jobs(auth)
results = get_job_results(auth, jobs)
```

## Get Job Runs API

```get_job_runs``` returns a list of runs of a patch management job.

|Parameter| Possible Values |Description| Required|
|--|--|--|--|
|```auth```|```qualysdk.auth.TokenAuth``` | Authentication object | ✅ |
| ```jobId``` | ```str``` | The ID(s) of the job to get runs for | ✅ |

```py

from qualysdk.auth import TokenAuth
from qualysdk.pm import get_job_runs, list_jobs

auth = TokenAuth(<username>, <password>, platform='qg1')

# Get some job:
job = list_jobs(auth, 'linux')[0]

# Get the runs for the job:
runs = get_job_runs(auth, job.id)
>>>[
    PMRun(
        jobInstanceId=1, 
        jobId='11111111-2222-3333-4444-555555555555',
        scheduledDateTime=datetime.datetime(2020, 1, 1, 15, 32, 18, tzinfo=datetime.timezone.utc), 
        timezoneType='SPECIFIC_TZ'
    )
]
```

## Create Job API

```create_job``` creates a new patch management job.

|Parameter| Possible Values |Description| Required|
|--|--|--|--|
|```auth```|```qualysdk.auth.TokenAuth``` | Authentication object | ✅ |
| ```name``` | ```str``` | The name of the job | ✅ |
| ```platform``` | ```Literal["Windows", "Linux"]``` | The platform of the job | ✅ |
| ```jobType``` | ```Literal["Install", "Rollback"]``` | The type of job to create. ```Rollback``` is Windows-only. | ✅ |
| ```scheduleType``` | ```Literal["On-demand", "Once", "Daily", "Weekly", "Monthly"]``` | The type of schedule to use | ✅ |
|```approvedPatches```|```List[str]```|An explicit list of patche GUIDs to add to the job|❌|
| ```assetIds``` | ```List[str]``` | The IDs of the assets to target | ❌ |
| ```assetTagIds``` | ```List[str]``` | The IDs of the asset tags to target | ❌ |
| ```filterType``` | ```Literal["all", "any"] = "any"``` | The type of filter to use | ❌ |
| ```exclusionTagIds``` | ```List[str]``` | The IDs of the asset tags to exclude | ❌ |
| ```exclusionAssetIds``` | ```List[str]``` | The IDs of the assets to exclude | ❌ |
| ```description``` | ```str``` | The description of the job | ❌ |
| ```coAuthorUserIds``` | ```List[str]``` | The IDs of the co-authors to add to the job | ❌ |
| ```exclusionFilterType``` | ```Literal["all", "any"] = "any"``` | The type of exclusion filter to use | ❌ |
| ```startDateTime``` | ```str``` | The start date and time of the job | ❌ for ```On-demand```, ✅ for others |
| ```recurring``` | ```bool=False``` | Whether the job is recurring | ❌ |
| ```dayOfMonth``` | ```int, 0 <= x <= 31``` | The day of the month to run the job | ❌ |
| ```matchAllTagIds``` | ```list[str]``` | The IDs of the asset tags to match | ❌ |
| ```recurringLastDayOfMonth``` | ```bool=False``` | Whether the job runs on the last day of the month | ❌ |
| ```monthlyRecurringType``` | ```Literal[0, 1, "0", "1"]``` | If 1, run on Patch Tuesday | ❌ |
| ```patchTuesdayPlusXDays``` | ```int, -27 <= x <= 27``` | The number of days before or after Patch Tuesday to run the job | ❌ |
| ```recurringDayOfMonth``` | ```int, 1 <= x <= 5``` | Run the job on a specific weekday of the month | ❌ |
| ```recurringWeekDayOfMonth``` | ```int, 0 <= x <= 6``` | The day of the week to run the job | ❌ |
| ```recurringWeekDays``` | ```str``` like ```"0,0,0,0,0,0,0"```| Similar to cron. Replace a 0 with a 1 to run on that day. str[0] = Sunday | ❌ |
| ```dynamicQQLType``` | ```Literal[0,1,2]``` | 0 = Do not use QQL, 1 = use patch QQL, 2 = use vulnerability QQL | ❌ |
| ```isDynamicPatchesQQL``` | ```bool=False``` | Whether to use dynamic patches QQL | ❌ |
| ```dynamicPatchesQQL``` | ```str``` | The QQL to use for dynamic patches | ❌ |
| ```continueOnPatchFailure``` | ```bool=True``` | (Linux only) Whether to continue the job if a patch fails | ❌ |
| ```preDeployment``` | ```str``` | Specify a message to display before deployment starts | ❌ |
| ```duringDeployment``` | ```str``` | Specify a message to display during deployment | ❌ |
| ```postDeployment``` | ```str``` | Specify a message to display after deployment | ❌ |
| ```onComplete``` | ```str``` | Specify a message to display when the job completes | ❌ |
| ```rebootCountdown``` | ```str``` | Specify a message to display before a reboot | ❌ |
| ```rebootOption``` | ```str``` | Specify a message for after a reboot | ❌ |
| ```suppressReboots``` | ```bool=False``` | Allow users to suppress reboots | ❌ |
| ```minimizeWindow``` | ```bool=False``` | Allow users to minimize the deployment window | ❌ |
| ```status``` | ```Literal["Disabled", "Enabled"] = "Disabled"``` | The status of the job | ❌ |
| ```timeout``` | ```int 1 <= x <= 168``` for hours, ```int 1 <= x <= 10080``` for minutes | The timeout for the job in hours or minutes (specified by timeoutUnit) | ❌ |
| ```timeoutUnit``` | Literal["HOURS", "MINUTES"] | The unit of the timeout | ❌ |
| ```timezoneType``` | ```Literal["AGENT_TZ", "SPECIFIC_TZ"]``` | The timezone type to use | ❌ |
| ```timezone``` | ```str``` | The (timezone)[https://docs.qualys.com/en/pm/api/deployment_job_resource/time_zones.htm] to use. For example: ```"America/New_York"``` | ❌ |
| ```opportunisticDownloads``` | ```bool=False``` | Whether to use opportunistic downloads. Only available for Windows | ❌ |
| ```linkedJobId``` | ```str``` | The ID of the job to link to | ❌ |
| ```notificationType``` | ```bool``` | If true, email notifications are sent | ❌ |
| ```notificationConfigRecipientEmail``` | ```str``` | The email to send notifications to | ❌ |
| ```notificationConfigCompletedPercentage``` | ```int 1 <= x <= 100``` | The percentage of completion to send notifications at | ❌ |
| ```notificationEvents``` | ```bool``` | If true, send notifications when ```onJobStart``` or ```onJobComplete``` are triggered | ❌ |
| ```downloadRandomizeTime``` | ```str``` | Provide the job randomize time in hours or minutes. Max is 2 hours or 120 minutes and must be less than the timeout/timeoutUnit | ❌ |
| ```downloadRandomizeTimeUnit``` | ```Literal["HOURS", "MINUTES"]``` | The unit of the randomize time | ❌ |
| ```additionalDynamicQQLType``` | ```Literal[1,2]``` | 1 = Use patch QQL, 2 = Use vulnerability QQL | ❌ |


There are a few ways to pass in certain assets. If you have very particular assets in mind, you can make a GAV API call to get the agentIds of the assets you want to target:

### Example 1 with GAV Query


```py
from qualysdk.auth import TokenAuth
from qualysdk.pm import create_job
from qualysdk.gav import query_assets

auth = TokenAuth(<username>, <password>, platform='qg1')

windows_assets = query_assets(
  auth, 
  filter="operatingSystem.category: `Windows / Server`",
  includeFields="agentId",  
)

# PM uses GUIDs for almost everything, so we need 
# to extract the GUIDs from the assets:
windows_assets_ids = [asset.agentId for asset in windows_assets]

# Create a new job for Windows servers. Let's
# focus on critical patches only:
job = create_job(
    auth, 
    platform='Windows', 
    jobType='Install', 
    scheduleType='On-demand', 
    assetIds=windows_assets_ids,
    name='My Job',
    dynamicPatchesQQL="vendorSeverity:`Critical`",
    dynamicQQLType=1,
    isDynamicPatchesQQL=True,
    status="Enabled", # Immediately enable the job. By default, the job is disabled!
)
>>>"11111111-2222-3333-4444-555555555555"
```

Or you can use asset tags to dynamically target assets. 

Using PM tag GUIDs is a bit more cumbersome since Qualys does not provide an easy way to look up tag GUIDs, but this method is much more flexible since new assets are picked up automatically by the job:

### Example 2 with Tag GUIDs

```py
from qualysdk.auth import TokenAuth
from qualysdk.pm import create_job

auth = TokenAuth(<username>, <password>, platform='qg1')

# Create a new job for Windows servers. Let's
# assume we have a tag for all Windows servers
# with GUID 22222222-3333-4444-5555-666666666666:

job = create_job(
    auth, 
    platform='Windows', 
    jobType='Install', 
    scheduleType='On-demand', 
    assetTagIds=['22222222-3333-4444-5555-666666666666'],
    name='My Job',
    dynamicPatchesQQL="vendorSeverity:`Critical`",
    dynamicQQLType=1,
    isDynamicPatchesQQL=True,
    status="Enabled", # Immediately enable the job. By default, the job is disabled!
)
>>>"11111111-2222-3333-4444-555555555555"
```

## Delete Job API

```delete_job``` deletes a patch management job or a list of jobs.

|Parameter| Possible Values |Description| Required|
|--|--|--|--|
|```auth```|```qualysdk.auth.TokenAuth``` | Authentication object | ✅ |
| ```jobId``` | ```Union[str, BaseList[str]]``` | The ID(s) of the job to delete | ✅ |

```py
from qualysdk.auth import TokenAuth
from qualysdk.pm import delete_job, list_jobs

auth = TokenAuth(<username>, <password>, platform='qg1')

# Delete a single job:
job = list_jobs(auth, 'linux')[0]
delete_job(auth, job.id)
>>>[
  {
    "id":"11111111-2222-3333-4444-555555555555",
    "name":"My job",
    "status":"success"
  }
]

# Delete multiple jobs:
jobs = list_jobs(auth)
delete_job(auth, [job.id for job in jobs])
>>>[
  {
    "id":"11111111-2222-3333-4444-555555555555",
    "name":"My job",
    "status":"success"
  },
  {
    "id":"22222222-3333-4444-5555-666666666666",
    "name":"My other job",
    "status":"success"
  },
  ...
]
```

## Change Job Status API

```change_job_status``` enables or disables a patch management job or a list of jobs.

|Parameter| Possible Values |Description| Required|
|--|--|--|--|
|```auth```|```qualysdk.auth.TokenAuth``` | Authentication object | ✅ |
| ```action``` | ```Literal["enable", "disable"]``` | The action to perform | ✅ |
| ```jobId``` | ```Union[str, BaseList[str]]``` | The ID(s) of the job to change the status of | ✅ |

```py
from qualysdk.auth import TokenAuth
from qualysdk.pm import change_job_status, list_jobs

auth = TokenAuth(<username>, <password>, platform='qg1')

# Disable a single job:
job = list_jobs(auth, 'linux')[0]
change_job_status(auth, 'disable', job.id)
>>>[
  {
    "id":"11111111-2222-3333-4444-555555555555",
    "name":"My job",
    "status":"success"
  }
]

# Disable multiple jobs:
jobs = list_jobs(auth)
change_job_status(auth, 'disable', [job.id for job in jobs])
>>>[
  {
    "id":"11111111-2222-3333-4444-555555555555",
    "name":"My job",
    "status":"success"
  },
  {
    "id":"22222222-3333-4444-5555-666666666666",
    "name":"My other job",
    "status":"success"
  },
  ...
]
```

## Lookup CVEs for QIDs API

```lookup_cves``` returns a list of CVEs and other details associated with specified QIDs as a ```BaseList``` of ```PMVulnerability``` objects.

This function accepts either a single QID as a string or integer, a list/BaseList of strings/integers, or a comma-separated string of QIDs.

|Parameter| Possible Values |Description| Required|
|--|--|--|--|
|```auth```|```qualysdk.auth.TokenAuth``` | Authentication object | ✅ |
| ```qids``` | ```Union[str, int, BaseList/list[str, int]]``` | The QID(s) to look up. Can be a list of strings/ints, a single int/string, or a comma-separated string | ✅ |
| ```threads``` | ```int=5``` | The number of threads to use for the lookup. ⚠️ Thread mode is only used if 1K+ ```qids``` are passed | ❌ |

```py
from qualysdk.auth import TokenAuth, BasicAuth
from qualysdk.vmdr import query_kb
from qualysdk.pm import lookup_cves

token = TokenAuth(<username>, <password>, platform='qg1')
basic = BasicAuth(<username>, <password>, platform='qg1')

# Get some QIDs:
qids = query_kb(basic, page_count=1, ids='10000-11000')

# Get the PM details/CVEs:
cves = lookup_cves(token, [qid.QID for qid in qids])
>>>[
  PMVulnerability(
    id=10230, 
    title='Viralator CGI Input Validation Remote Shell Command Vulnerability', 
    cves=['CVE-2001-0849'], 
    detectedDate=datetime.datetime(2001, 11, 7, 16, 15, 57), 
    severity=5, 
    vulnType='VULNERABILITY'
  ), 
  PMVulnerability(
    id=10310, 
    title='Suspicious file register.idc', 
    cves=None, # Sometimes there are no CVEs!
    detectedDate=datetime.datetime(2001, 4, 3, 4, 12, 9), 
    severity=1, 
    vulnType='POTENTIAL'
  ),
  ...
]

# Or you can pass in a single QID:
cve = lookup_cves(token, 10230)
>>>PMVulnerability(
  id=10230, 
  title='Viralator CGI Input Validation Remote Shell Command Vulnerability', 
  cves=['CVE-2001-0849'], 
  detectedDate=datetime.datetime(2001, 11, 7, 16, 15, 57), 
  severity=5, 
  vulnType='VULNERABILITY'
)
```

## Get Patches API

```get_patches``` returns a ```BaseList``` of ```Patch``` objects that match the given kwargs.

|Parameter| Possible Values |Description| Required|
|--|--|--|--|
|```auth```|```qualysdk.auth.TokenAuth``` | Authentication object | ✅ |
| ```page_count``` | ```Union[int, "all"] = "all"``` | The number of pages to return | ❌ |
| ```pageSize``` | ```int=1000``` | The number of patches to return per page | ❌ |
| ```platform``` | ```Literal["all", "windows", "linux"] = "all"``` | The platform of the patches to return | ❌ |
| ```query``` | ```str="patchStatus:[Missing,Installed] and isSuperseded:false``` FOR WINDOWS | A patch QQL query to filter with. By default returns all of the latest patches if ```platform=windows``` | ❌ |
| ```havingQuery``` | ```str``` | A PM host QQL query to filter with | ❌ |
| ```attributes``` | ```str``` | The attributes to return in the response as a comma-separated string | ❌ |

```py
from qualysdk.auth import TokenAuth
from qualysdk.pm import get_patches

auth = TokenAuth(<username>, <password>, platform='qg1')

# Get all patches that are severity 5
# and only return their titles & IDs:
patches = get_patches(auth, query="vendorSeverity:5", attributes="id,title")
>>>[
  Patch(
    id='11111111-2222-3333-4444-555555555555', 
    title='My Patch',
    ...
  ),
  Patch(
    id='22222222-3333-4444-5555-666666666666', 
    title='My Other Patch',
    ...
  ),
  ...
]

# Just get windows patches:
windows_patches = get_patches(auth, platform='windows')
>>>[
  Patch(
    id='11111111-2222-3333-4444-555555555555', 
    title='My Patch',
    platform='Windows',
    ...
  ),
  Patch(
    id='22222222-3333-4444-5555-666666666666', 
    title='My Other Patch',
    ...
  ),
  ...
]
```

## Get Assets API

```get_assets``` returns a ```BaseList``` of ```Asset``` objects that match the given kwargs.

|Parameter| Possible Values |Description| Required|
|--|--|--|--|
|```auth```|```qualysdk.auth.TokenAuth``` | Authentication object | ✅ |
| ```page_count``` | ```Union[int, "all"] = "all"``` | The number of pages to return | ❌ |
| ```pageSize``` | ```int=400``` | The number of assets to return per page | ❌ |
| ```platform``` | ```Literal["all", "windows", "linux"] = "all"``` | The platform of the assets to return | ❌ |
| ```query``` | ```str``` | A patch QQL query to filter with | ❌ |
| ```havingQuery``` | ```str``` | A PM host QQL query to filter with | ❌ |
| ```attributes``` | ```str``` | The attributes to return in the response as a comma-separated string | ❌ |

```py
from qualysdk.auth import TokenAuth
from qualysdk.pm import get_assets

auth = TokenAuth(<username>, <password>, platform='qg1')

# Get all assets that are missing patches:
assets = get_assets(auth, query="patchStatus:Missing")
>>>[
  Asset(
    id='11111111-2222-3333-4444-555555555555', 
    name='My Asset',
    ...
  ),
  Asset(
    id='22222222-3333-4444-5555-666666666666', 
    name='My Other Asset',
    ...
  ),
  ...
]
```


## Get Patch Count API

```get_patch_count``` returns the number of patches for a given platform that match the given query and havingQuery.

|Parameter| Possible Values |Description| Required|
|--|--|--|--|
|```auth```|```qualysdk.auth.TokenAuth``` | Authentication object | ✅ |
| ```platform``` | ```Literal["windows", "linux"] = "windows"``` | The platform of the patches to return | ✅ |
| ```query``` | ```str``` | A patch QQL query to filter with | ❌ |
| ```havingQuery``` | ```str``` | A PM host QQL query to filter with | ❌ |

```py
from qualysdk.auth import TokenAuth
from qualysdk.pm import get_patch_count

auth = TokenAuth(<username>, <password>, platform='qg1')

# Get the number of patches for Windows
# that are critical severity:
count = get_patch_count(auth, platform='windows', query="vendorSeverity:Critical")
>>>100
```

## Lookup Host UUIDs from Asset IDs API

```lookup_host_uuids``` returns a list of host UUIDs for a given list of asset IDs.

```assetIds``` can be a list/BaseList of strings/integers, a single int/string, or a comma-separated string.

|Parameter| Possible Values |Description| Required|
|--|--|--|--|
|```auth```|```qualysdk.auth.TokenAuth``` | Authentication object | ✅ |
| ```assetIds``` | ```Union[list[str, int], BaseList[str, int], str, int]``` | The IDs of the assets to look up | ✅ |

### Example 1 with GAV Query

```py
from qualysdk.auth import TokenAuth
from qualysdk.pm import lookup_host_uuids
from qualysdk.gav import query_assets # Could also use get_all_assets!

auth = TokenAuth(<username>, <password>, platform='qg1')

# Get some assets. All we need is assetId.
# We can also filter for assets activated for PM:
assets = query_assets(
  auth, 
  includeFields='assetId',
  filter='sensors.activatedForModules:`PM`
)

# Get the host UUIDs for the assets:
uuids = lookup_host_uuids(auth, [asset.assetId for asset in assets])
>>>[
  (
    123456789,
    '11111111-2222-3333-4444-555555555555'
  ),
  (
    987654321,
    '22222222-3333-4444-5555-666666666666'
  ),
  ...
]
```

### Example 2 with List of ```assetIds```

```py
from qualysdk.auth import TokenAuth
from qualysdk.pm import lookup_host_uuids

auth = TokenAuth(<username>, <password>, platform='qg1')

ids = [123456789, 987654321]
uuids = lookup_host_uuids(auth, ids)
>>>[
  (
    123456789,
    '11111111-2222-3333-4444-555555555555'
  ),
  (
    987654321,
    '22222222-3333-4444-5555-666666666666'
  )
]
```

### Example 3 with Comma-Separated String of ```assetIds```

```py
from qualysdk.auth import TokenAuth
from qualysdk.pm import lookup_host_uuids

auth = TokenAuth(<username>, <password>, platform='qg1')

ids = '123456789,987654321'
uuids = lookup_host_uuids(auth, ids)
>>>[
  (
    123456789,
    '11111111-2222-3333-4444-555555555555'
  ),
  (
    987654321,
    '22222222-3333-4444-5555-666666666666'
  )
]
```

## Get Patch Catalog API

```get_patch_catalog``` returns the patch catalog for a given platform according to ```patchId```.

```patchId``` can be a list/BaseList of strings/integers, a single int/string, or a comma-separated string.

>**Head's Up!:** You should only pass in one platform at a time. If you pass in a mix of both Windows and Linux patches, the function will only return the patches that match the ```platform``` parameter (default is Windows).

|Parameter| Possible Values |Description| Required|
|--|--|--|--|
|```auth```|```qualysdk.auth.TokenAuth``` | Authentication object | ✅ |
| ```patchId``` | ```Union[list[str, int], BaseList[str, int], str, int]``` | The IDs of the patches to look up | ✅ |
| ```platform``` | ```Literal["windows", "linux"] = "windows"``` | The platform of the patches to return. Defaults to windows | ❌ |
| ```attributes``` | ```str``` | The attributes to return in the response as a comma-separated string | ❌ |

```py
from qualysdk.auth import TokenAuth
from qualysdk.pm import get_patch_catalog, get_patches

auth = TokenAuth(<username>, <password>, platform='qg1')

# Get some Linux patches:
patches = get_patches(
  auth, 
  platform='linux', 
  attributes="id"
)

# Get the catalog entries:
catalog = get_patch_catalog(
  auth, 
  [patch.id for patch in patches], 
  platform='linux'
)
>>>[
  CatalogPatch(
    "patchId": "11111111-2222-3333-4444-555555555555",
    "title": "My Patch",
    "vendor": "My Vendor",
    ...
  ),
  CatalogPatch(
    "patchId": "22222222-3333-4444-5555-666666666666",
    "title": "My Other Patch",
    ...
  ),
  ...
]
```

## Get Packages Associated with Linux Patches API

```get_packages_in_linux_patch``` returns the packages associated with a Linux patch.

If a ```BaseList``` or a ```list``` of patch IDs is passed, the function will use threading to speed up the process.

> <span style="color: red; font-weight: bold;">Warning:</span> You should filter down the patches as much as possible before passing them into this function. If you bulk-pass in a lot of patches, you will almost certainly hit a rate limit. **PM APIs do not return the headers necessary for the SDK to auto-recover from rate limits.**


|Parameter| Possible Values |Description| Required|
|--|--|--|--|
|```auth```|```qualysdk.auth.TokenAuth``` | Authentication object | ✅ |
| ```patchId``` | ```Union[str, BaseList[str]]``` | The ID(s) of the patch to get packages for | ✅ |
| ```threads``` | ```int=5``` | The number of threads to use for the lookup. | ❌ |
| ```filter``` | ```str``` | The QQL filter to search for packages | ❌ |
| ```pageNumber``` | ```int``` | The page number to return. The SDK will handle pagination for you. Users can use this if ```page_count``` is 1 to pull a specific page. | ❌ |
| ```pageSize``` | ```int=10``` | The number of packages to return per page | ❌ |

```py
from qualysdk.auth import TokenAuth
from qualysdk.pm import get_packages_in_linux_patch, get_patches

auth = TokenAuth(<username>, <password>, platform='qg1')

# Get some Linux patches:
patches = get_patches(
  auth, 
  platform='linux', 
  attributes="id",
  query="vendorSeverity:Critical"
)

# Get the packages for the patches:
packages = get_packages_in_linux_patch(
  auth, 
  [patch.id for patch in patches]
)
>>>PackageDetail(
  packageName='minidlna_1.3.0+dfsg-2+deb11u2', 
  architecture='noarch', 
  patchId='48e7d965-5f86-3118-a35f-b8fd1463e6b0'
)
```

## Get Products Associated with Windows Patches API

```get_products_in_windows_patch``` returns the products associated with a Windows patch.

If a ```BaseList``` or a ```list``` of patch IDs is passed, the function will use threading to speed up the process.

> <span style="color: red; font-weight: bold;">Warning:</span> You should filter down the patches as much as possible before passing them into this function. If you bulk-pass in a lot of patches, you will almost certainly hit a rate limit. **PM APIs do not return the headers necessary for the SDK to auto-recover from rate limits.**


|Parameter| Possible Values |Description| Required|
|--|--|--|--|
|```auth```|```qualysdk.auth.TokenAuth``` | Authentication object | ✅ |
| ```patchId``` | ```Union[str, BaseList[str]]``` | The ID(s) of the patch to get products for | ✅ |
| ```threads``` | ```int=5``` | The number of threads to use for the lookup. | ❌ |

```py
from qualysdk.auth import TokenAuth
from qualysdk.pm import get_products_in_windows_patch, get_patches

auth = TokenAuth(<username>, <password>, platform='qg1')

# Get some Windows patches:
patches = get_patches(
  auth, 
  platform='windows', 
  attributes="id",
  query="vendorSeverity:Critical"
)

# Get the products for the patches:
products = get_products_in_windows_patch(
  auth, 
  [patch.id for patch in patches]
)
>>>AssociatedProduct(
  product=['Adobe Audition 2024 24 x64'], 
  patchId='2c1649c0-a18a-3f77-8c52-a6ea297ab295'
)
```

## Count Product Vulnerabilities API

```count_product_vulns``` returns the number of active and fixed vulnerabilities stemming from products.

|Parameter| Possible Values |Description| Required|
|--|--|--|--|
|```auth```|```qualysdk.auth.TokenAuth``` | Authentication object | ✅ |
| ```severityList``` | ```Union[str, list[Literal["Critical", "Important", "Moderate", "Low", "None"]]]``` | The severity levels to count vulnerabilities for. Can be a list or strings or a comma-separated string | ❌ |
| ```tagUUIDs``` | ```Union[str, list[str]]``` | The UUIDs of the tags to filter with | ❌ |

```py
from qualysdk.auth import TokenAuth
from qualysdk.pm import count_product_vulns

auth = TokenAuth(<username>, <password>, platform='qg1')

# Get the number of Critical and Important
# vulnerabilities for all products:
count = count_product_vulns(
  auth, 
  severityList=["Critical", "Important"]
)
>>>[
  ProductVulnCount(
      name='Windows', 
      totalQIDCount=123, 
      patchableQIDCount=None, 
      type='APP_FAMILY', 
      patchableQIDs=None, 
      totalQIDs=None, 
      severity='Critical'
    ), 
  ProductVulnCount(
    name='Office', 
    totalQIDCount=123, 
    patchableQIDCount=None, 
    type='APP_FAMILY', 
    patchableQIDs=None, 
    totalQIDs=None, 
    severity='Critical'
  ),
  ...
]
```


## ```qualysdk-pm``` CLI tool

The ```qualysdk-pm``` CLI tool is a command-line interface for the PM portion of the SDK. It allows you to quickly pull down results from PM APIs and save them to an XLSX/TXT file.

Use ```--help``` on each command to see the available options.

### Usage

```bash
usage: qualysdk-pm [-h] -u USERNAME -p PASSWORD [-P {qg1,qg2,qg3,qg4}] {list_jobs,get_job_results,get_job_runs,lookup_cves,get_patches,get_patch_count,get_assets,get_patch_catalog} ...

CLI script to quickly perform Patch Management (PM) operations using qualysdk

positional arguments:
  {list_jobs,get_job_results,get_job_runs,lookup_cves,get_patches,get_patch_count,get_assets,get_patch_catalog}
                        Action to perform
    list_jobs           Get a list of PM jobs.
    get_job_results     Get results for a PM job.
    get_job_runs        Get runs for a PM job.
    lookup_cves         Look up CVEs for a given QID(s).
    get_patches         Get patches for a given platform.
    get_patch_count     Get the number of patches available for a platform according to query and havingQuery.
    get_assets          Get assets for a given platform.
    get_patch_catalog   Get patch catalog entries for a given platform.

options:
  -h, --help            show this help message and exit
  -u USERNAME, --username USERNAME
                        Qualys username
  -p PASSWORD, --password PASSWORD
                        Qualys password
  -P {qg1,qg2,qg3,qg4}, --platform {qg1,qg2,qg3,qg4}
                        Qualys platform
```
