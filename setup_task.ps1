# setup_task.ps1 - Register/update the daily 09:30 Windows scheduled task.
# Usage (normal privileges; task runs as the current user):
#   powershell -ExecutionPolicy Bypass -File .\setup_task.ps1
# Uninstall:
#   Unregister-ScheduledTask -TaskName "PH-Daily-Digest" -Confirm:$false
# ASCII-only on purpose: PowerShell 5.1 mis-reads non-BOM UTF-8 .ps1 as GBK.
$ErrorActionPreference = "Stop"
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$taskName = "PH-Daily-Digest"
$runScript = Join-Path $here "run.ps1"

$action = New-ScheduledTaskAction -Execute "powershell.exe" `
    -Argument "-NoProfile -ExecutionPolicy Bypass -WindowStyle Hidden -File `"$runScript`""

# Three triggers, all guarded to one real run/day by run.ps1's once-per-day marker:
#   1) Daily 09:30  - normal case when the laptop is awake.
#   2) At logon     - covers reboots and unlock-after-sleep (sign-in required).
#   3) Resume from sleep - the laptop case: fire when the lid opens. There is no
#      built-in "on wake" trigger, so subscribe to the System-log Power-Troubleshooter
#      event (id 1), which is written on every resume. Built via CIM (the
#      New-ScheduledTaskTrigger cmdlet has no event-trigger switch).
$tDaily = New-ScheduledTaskTrigger -Daily -At 9:30am

$tLogon = New-ScheduledTaskTrigger -AtLogOn -User $env:USERNAME
$tLogon.Delay = "PT1M"   # let Wi-Fi reconnect before the job runs

$evtClass = Get-CimClass -ClassName MSFT_TaskEventTrigger `
    -Namespace Root/Microsoft/Windows/TaskScheduler
$tResume = New-CimInstance -CimClass $evtClass -ClientOnly
$tResume.Enabled = $true
$tResume.Delay = "PT1M"
$tResume.Subscription = "<QueryList><Query Id='0' Path='System'><Select Path='System'>*[System[Provider[@Name='Microsoft-Windows-Power-Troubleshooter'] and (EventID=1)]]</Select></Query></QueryList>"

$triggers = @($tDaily, $tLogon, $tResume)

# Catch up after missed triggers (shutdown/sleep); allow running on battery
$settings = New-ScheduledTaskSettingsSet -StartWhenAvailable `
    -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries `
    -ExecutionTimeLimit (New-TimeSpan -Minutes 15)
$principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive -RunLevel Limited

Register-ScheduledTask -TaskName $taskName -Action $action -Trigger $triggers `
    -Settings $settings -Principal $principal `
    -Description "Product Hunt digest: daily 09:30 + on logon/resume (once-per-day guarded) -> MD/HTML archive + Slack" -Force | Out-Null

Write-Host "Registered scheduled task '$taskName' (daily 09:30 + logon + resume-from-sleep)."
Write-Host "Run now:        Start-ScheduledTask -TaskName '$taskName'"
Write-Host "Next run time:   Get-ScheduledTaskInfo -TaskName '$taskName'"
