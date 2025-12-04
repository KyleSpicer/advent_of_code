<#
.SYNOPSIS
Advent of Code 2025, Day 4

.NOTES
@ symbols are rolls of wrapping paper
#>

$Directions = @{
    N  = @(-1, 0)
    NE = @(-1, 1)
    E  = @(0, 1)
    SE = @(1, 1)
    S  = @(1, 0)
    SW = @(1, -1)
    W  = @(0, -1)
    NW = @(-1, -1)
}

function Get-Grid {
    param(
        [Object[]]$Data
    )

    $grid = foreach ($line in $Data) {
        # comma operator forces each line to be its own element
        # else PowerShell would flatten all into one char array
        , ($line.ToCharArray())
    }

    return $grid
}

function Show-Grid {
    param(
        [char[][]]$grid
    )

    $rows = $grid.Count
    $cols = $grid[0].Count

    for ($i = 0; $i -lt $rows; $i++) {
        for ($j = 0; $j -lt $cols; $j++) {
            Write-Host $grid[$i][$j] -NoNewline
        }
        Write-Host
    }
}

function Test-Roll {
    param(
        [char[][]]$Map,
        [int]$Row,
        [int]$Col,
        [int]$MaxRolls
    )

    $currentRollCount = 0
    $MapSize = $Map.Count - 1

    # check all directions counting adjacent rolls
    foreach ($dirName in $Directions.Keys) {
        $posArray = $Directions[$dirName]
        $dr = $posArray[0]
        $dc = $posArray[1]

        # calculate position to check
        $newRow = $Row + $dr
        $newCol = $Col + $dc

        # bounds check
        if ($newRow -lt 0 -or $newCol -lt 0 -or 
            $newRow -gt $MapSize -or $newCol -gt $MapSize) {
            continue # out of bounds, move to next position
        }

        # check if position is another roll of wrapping papers
        if ($Map[$newRow][$newCol] -eq '@') {
            $currentRollCount++
        }

        if ($currentRollCount -ge $MaxRolls) {
            return $false
        }
    }

    return $true
}

function Get-PartOne {
    param(
        [Object[]]$Data
    )

    $totalAccessibleRolls = 0

    # generate map
    $Map = Get-Grid $Data
    $rows = $Map.Count
    $cols = $Map[0].Count

    for ($i = 0; $i -lt $rows; $i++) {
        for ($j = 0; $j -lt $cols; $j++) {

            $currChar = $Map[$i][$j]
            
            if ($currChar -ne '@') {
                continue
            }

            if (Test-Roll -Map $Map -Row $i -Col $j -MaxRolls 4) {
                $totalAccessibleRolls += 1
            }
        }
    }

    return $totalAccessibleRolls
}

function Remove-PaperRolls {
    param(
        [char[][]]$Map
    )

    $rows = $Map.Count
    $cols = $Map[0].Count
    $totalRollsRemoved = 0

    for ($i = 0; $i -lt $rows; $i++) {
        for ($j = 0; $j -lt $cols; $j++) {

            $currChar = $Map[$i][$j]
            
            if ($currChar -ne '@') {
                continue
            }

            # remove rolls here
            if (Test-Roll -Map $Map -Row $i -Col $j -MaxRolls 4) {
                $totalRollsRemoved += 1
                $Map[$i][$j] = 'x'
            }
        }
    }

    return $totalRollsRemoved
}
function Get-PartTwo {
    param(
        [Object[]]$Data
    )

    # generate map
    $Map = Get-Grid $Data
    $rollsRemoved = 0

    # Write-Host "Initial state:"
    # Show-Grid $Map
    # Write-Host

    while ($true) {
        $removed = Remove-PaperRolls -Map $Map

        if ($removed -eq 0) {
            break
        }

        $rollsRemoved += $removed
        # Write-Host "Removed: $rollsRemoved"
        # Show-Grid $Map
        # Write-Host
    }

    return $rollsRemoved
}

# Main Script

$sample = ".\sample.txt"
$input = ".\input.txt"

$data = Get-Content -Path $input

$p1Duration = Measure-Command { $partOne = Get-PartOne $data }
Write-Host "Part One: $partOne ($($p1Duration.TotalSeconds) seconds)"

$p2Duration = Measure-Command { $partTwo = Get-PartTwo $data }
Write-Host "Part Two: $partTwo ($($p2Duration.TotalSeconds) seconds)"