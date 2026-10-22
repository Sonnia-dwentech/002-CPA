# Read-only local tool inventory. No installs, network checks or services started.
[CmdletBinding()]
param()
$ErrorActionPreference = 'Stop'
$projectRoot = Split-Path -Parent $PSScriptRoot
$checks = @(
    @{ Name = 'Python'; Command = 'python.exe'; Args = @('--version') },
    @{ Name = 'Node'; Command = 'node.exe'; Args = @('--version') },
    @{ Name = 'npm'; Command = 'npm.cmd'; Args = @('--version') },
    @{ Name = 'PostgreSQL client'; Command = 'psql.exe'; Args = @('--version') },
    @{ Name = 'Docker CLI'; Command = 'docker.exe'; Args = @('--version') }
)
Write-Output 'CPA read-only local setup inventory'
Write-Output ('Project: ' + $projectRoot)
foreach ($check in $checks) {
    $command = Get-Command $check.Command -CommandType Application -ErrorAction SilentlyContinue | Select-Object -First 1
    if ($null -eq $command) {
        Write-Output ($check.Name + ': NOT FOUND on PATH')
        continue
    }
    try {
        $arguments = $check.Args
        $result = & $command.Source @arguments 2>&1
        if ($LASTEXITCODE -ne 0) {
            Write-Output ($check.Name + ': version probe FAILED; exit ' + $LASTEXITCODE)
        } else {
            Write-Output ($check.Name + ': ' + (($result | ForEach-Object { [string]$_ }) -join ' '))
        }
    } catch {
        Write-Output ($check.Name + ': version probe FAILED')
    }
}
$templatePath = Join-Path $projectRoot '.env.example'
if (-not (Test-Path -LiteralPath $templatePath -PathType Leaf)) {
    Write-Output 'Template: MISSING'
    exit 1
}
# Validate only the public template, never read/print a private .env.
$expected = @{
    APP_ENV = 'local'; LOG_LEVEL = 'INFO'; DATABASE_URL = ''; FRONTEND_ORIGIN = ''
    AUTH_SECRET = ''; OPENAI_API_KEY = ''; OPENAI_MODEL = ''; STORAGE_BUCKET = ''
    MAX_AI_RUN_COST = ''; LIVE_AI_ENABLED = 'false'
}
$seen = @{}
foreach ($line in Get-Content -LiteralPath $templatePath) {
    if ($line -match '^\s*(#|$)') { continue }
    if ($line -notmatch '^([A-Z_]+)=(.*)$') {
        Write-Output 'Template: INVALID syntax (value suppressed)'; exit 1
    }
    $key = $Matches[1]; $value = $Matches[2]
    if ($seen.ContainsKey($key) -or -not $expected.ContainsKey($key) -or $value -cne $expected[$key]) {
        Write-Output 'Template: unexpected key, duplicate or non-placeholder value (value suppressed)'; exit 1
    }
    $seen[$key] = $true
}
if ($seen.Count -ne $expected.Count) {
    Write-Output 'Template: missing required placeholder keys'; exit 1
}
Write-Output 'Template: PASS — local/default or empty values only; proposed live switch false'
Write-Output 'Application setup: NOT VERIFIED — no approved locked application dependencies or runnable scaffold'
Write-Output 'Database: NOT VERIFIED — no connection attempted; Docker CLI presence is not service readiness'
Write-Output 'Approval: see progress.md and B010 report; inventory does not approve runtime compatibility'
Write-Output 'Exit 2 means incomplete application setup; exit 1 means template validation failed.'
exit 2
