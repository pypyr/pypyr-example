Write-Host("$($args[0]):$(Get-Date)")
Start-Sleep $args[1]
Write-Host("$($args[0]) to stdout")
$stderr = [System.Console]::OpenStandardError()
$enc = [system.Text.Encoding]::UTF8
$err = $enc.GetBytes("$($args[0]): to sterr`r`n")
$stderr.Write($err, 0, $err.Length)
Write-Host $args[0] done
exit 0