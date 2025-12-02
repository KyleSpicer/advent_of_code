<#
.SYNOPSIS
Advent of Code 2025 Day 1

.DESCRIPTION
Sweet puzzles to help Santa's elves save Christmas!
URL: https://adventofcode.com/2025/day/1
#>

function Get-TableData {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Path
    )

    # validate file exists
    if (-not (Test-Path $Path)) {
        throw "File not found: $Path"
    }

    $tableData = Get-Content $Path | ForEach-Object {
        if ($_ -match '^([LR])(\d+)$') {
            
            # matches are stored in $Matches[]
            [PSCustomObject]@{
                Direction = $Matches[1]
                Rotation  = $Matches[2]
            }
        }
        else {
            Write-Warning "Invalid line: '$_'"
        }
    }

    return $tableData
}

function Get-PartOneAnswer {
    param(
        [Parameter(Mandatory = $true)]
        [PSCustomObject[]] $Data
    )

    $dialPosition = 50
    $answer = 0

    foreach ($rotation in $Data) {
        $direction = $rotation.Direction
        $rot = [int]$rotation.Rotation

        if ($direction -eq 'L') {
            $curr = $dialPosition - $rot      
        } 
        else {
            <# $direction is 'R' #>
            $curr = $dialPosition + $rot        
        }

        $dialPosition = ($curr % 100 + 100) % 100

        if (0 -eq $dialPosition) {
            $answer += 1
        }
    }

    return $answer
}

function Get-PartTwoAnswer {
    param(
        [Parameter(Mandatory = $true)]
        [PSCustomObject[]] $Data
    )

    $dialPosition = 50
    $answer = 0
    
    foreach ($rotation in $Data) {
        $direction = $rotation.Direction
        $rot = [int]$rotation.Rotation

        foreach ($num in 0..($rot - 1)) {
            
            if ($direction -eq 'L') {
                $dialPosition = ($dialPosition - 1 + 100) % 100
            }
            else {
                $dialPosition = ($dialPosition + 1) % 100
            }

            if ($dialPosition -eq 0) {
                $answer += 1
            }
        }
    }

    return $answer
}


# Main Script

Write-Output "=== Advent of Code (2025, Day 1)"
$samplePath = '.\sample.txt'
$inputPath = '.\input.txt'

# read in file data to PSCustomObject array
# $rotations = Get-TableData -Path $samplePath
$rotations = Get-TableData -Path $inputPath

# process day 1 part 1
$partOneAnswer = Get-PartOneAnswer $rotations
Write-Output "[+] Part One Answer: $partOneAnswer"

# process day 1 part 2
$partTwoAnswer = Get-PartTwoAnswer $rotations
Write-Output "[+] Part Two Answer: $partTwoAnswer"
