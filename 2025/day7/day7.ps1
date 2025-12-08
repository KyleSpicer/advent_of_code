<#
.SYNOPSIS
Advent of Code 2025, Day 7
#>
function Show-Map {
    param(
        [Object[]]$Array
    )

    $rows = $Array.Count
    $cols = $Array[0].Count 

    for ($i = 0; $i -lt $rows; $i++) {
        for ($j = 0; $j -lt $cols; $j++) {
            Write-Host "$($Array[$i][$j])" -NoNewline
        }
        Write-Host
    }
    Write-Host
}

function Get-PartOne {
    param(
        [Object[]]$Array
    )   

    $answer = 0
    $numRows = $Array.Count
    $numCols = $Array[0].Count
    
    $queue = New-Object System.Collections.ArrayList
    $visited = New-Object System.Collections.Generic.HashSet[string]

    # get location of starting point
    $firstRow = -join $Array[0]
    $sc = $firstRow.IndexOf('S')
    $queue.Add(@(0, $sc)) | Out-Null

    # start shooting those beams
    while ($queue.Count -gt 0) {
        $cr, $cc = $queue[0]    # unpack coords
        $queue.RemoveAt(0)      # dequeue 

        # advance beam down
        $nr = $cr + 1
        $nc = $cc

        if (-not($nr -ge 0 -and 
                $nr -lt $numRows -and 
                $nc -ge 0 -and 
                $nc -lt $numCols)) {
            continue
        }
        
        $char = $Array[$cr + 1][$cc] 
        if ($char -eq '.') {
            # add new position to queue and continue
            if ($visited.Contains("$nr,$nc")) {
                continue
            }

            $queue.Add(@($nr, $nc)) | Out-Null
            $visited.Add("$nr,$nc") | Out-Null   # add coord to set
            continue
        }

        $char = $Array[$nr][$nc]
        if ($char -eq '^') {

            $answer++     # increase number of splits

            # create left starting point
            $cl = $nc - 1
            if ($visited.Contains("$nr,$cl")) {
            }
            else {
                $queue.Add(@($nr, $cl)) | Out-Null
                $visited.Add("$nr,$cl") | Out-Null
            }

            # create right starting point
            $cr = $nc + 1
            if ($visited.Contains("$nr,$cr")) {
            }
            else {
                $queue.Add(@($nr, $cr)) | Out-Null
                $visited.Add("$nr,$cr") | Out-Null
            }
        }
    }
    return $answer
}

$sampleFile = ".\sample.txt"
$inputFile = ".\input.txt"

$Data = Get-Content -Path $inputFile | ForEach-Object { , $_.ToCharArray() }

$partOne = Get-PartOne -Array $Data
Write-Host "Part One: $partOne"