<#
.SYNOPSIS
Advent of Code 2025, Day 7
#>

$Global:TimelineMemo = @{}

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

function Get-Timelines {
    param(
        [Object[]]$Array,
        [int]$row,
        [int]$col
    )

    $numRows = $Array.Count
    $numCols = $Array[0].Count
    $key = "$row,$col"

    # memoization lookup
    if ($TimelineMemo.ContainsKey($key)) {
        return $TimelineMemo[$key]
    }

    # advance position down
    $nr = $row + 1
    $nc = $col

    # hit bottom of map
    if ($nr -ge $numRows) {
        $TimelineMemo[$key] = 1
        return 1
    }

    $current = $Array[$nr][$nc]
    $totalTimelines = 0

    switch ($current) {
        '.' {
            # continue down
            $totalTimelines += Get-Timelines -Array $Array -row $nr -col $nc
        }
        '^' {
            # go left
            if ($nc - 1 -ge 0) {
                $totalTimelines += Get-Timelines -Array $Array -row $nr -col ($nc - 1)
            }
            
            # go right
            if ($nc + 1 -lt $numCols) {
                $totalTimelines += Get-Timelines -Array $Array -row $nr -col ($nc + 1)
            }
        }
    }

    # store current position's timeline count in memo
    $TimelineMemo[$key] = $totalTimelines
    return $totalTimelines
}

function Get-PartTwo {
    param(
        [Object[]]$Array
    )

    # get location of starting point
    $firstRow = -join $Array[0]
    $sc = $firstRow.IndexOf('S')

    return Get-Timelines -Array $Array -row 0 -col $sc
}

$sampleFile = ".\sample.txt"
$inputFile = ".\input.txt"

$Data = Get-Content -Path $inputFile | ForEach-Object { , $_.ToCharArray() }

$partOne = Get-PartOne -Array $Data
Write-Host "Part One: $partOne"

$partTwo = Get-PartTwo -Array $Data
Write-Host "Part Two: $partTwo"