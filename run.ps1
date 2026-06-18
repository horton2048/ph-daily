# run.ps1 - ph-daily runner. Called by the scheduled task.
# Sets UTF-8 (for Chinese output), runs via `uv run` (auto-pulls tzdata), logs to logs\.
# ASCII-only on purpose: PowerShell 5.1 mis-reads non-BOM UTF-8 .ps1 as GBK.
# NOTE: must be "Continue" not "Stop": with Stop, uv's stderr lines (e.g.
# "Installed 1 package") become NativeCommandError and abort the script.
$ErrorActionPreference = "Continue"
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $here

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$env:PYTHONUTF8 = "1"
$env:PYTHONIOENCODING = "utf-8"

$logDir = Join-Path $here "logs"
if (-not (Test-Path $logDir)) { New-Item -ItemType Directory -Path $logDir | Out-Null }
$stamp = Get-Date -Format "yyyy-MM-dd"
$log = Join-Path $logDir "$stamp.log"

# Once-per-day guard. On a laptop the logon/resume triggers can fire many times
# a day (every lid-open); the daily 09:30 trigger fires too. Run the real job at
# most once per local calendar day so Slack is not spammed. Manual runs pass args
# (e.g. --date / --dry-run / --force) and bypass the guard entirely.
$marker = Join-Path $logDir "last_success.txt"
$today = Get-Date -Format "yyyy-MM-dd"
if ($args.Count -eq 0 -and (Test-Path $marker)) {
    $last = (Get-Content $marker -Raw -ErrorAction SilentlyContinue).Trim()
    if ($last -eq $today) {
        "=== $(Get-Date -Format o) SKIP (already ran $today) ===" | Tee-Object -FilePath $log -Append
        exit 0
    }
}

# Locate uv (scheduled-task PATH may lack the user-level install dir)
$uv = (Get-Command uv -ErrorAction SilentlyContinue).Source
if (-not $uv) { $uv = Join-Path $env:USERPROFILE ".local\bin\uv.exe" }
if (-not (Test-Path $uv)) { $uv = $null }

"=== $(Get-Date -Format o) START ===" | Tee-Object -FilePath $log -Append
if ($uv) {
    & $uv run ph_daily.py @args 2>&1 | Tee-Object -FilePath $log -Append
} else {
    & python ph_daily.py @args 2>&1 | Tee-Object -FilePath $log -Append
}
$code = $LASTEXITCODE
"=== $(Get-Date -Format o) END (exit $code) ===" | Tee-Object -FilePath $log -Append
# Mark today done only for clean scheduled runs (no args); manual/dry runs do not count.
if ($code -eq 0 -and $args.Count -eq 0) {
    Set-Content -Path $marker -Value $today -Encoding ascii
}
exit $code
