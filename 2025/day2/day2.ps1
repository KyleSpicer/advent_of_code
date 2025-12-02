<#
.SYNOPSIS
Advent of Code 2025 Day 2
#>

function Get-RangesFromFile {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Path
    )

    # validate file exists
    if (-not (Test-Path $Path)) {
        throw "File not found: $Path"
    }

    $ranges = (Get-Content -Path $Path) -split ',' | ForEach-Object {
        $parts = $_ -split '-'
        [PSCustomObject]@{
            Low  = [long]$parts[0]
            High = [long]$parts[1]
        }
    }

    return $ranges
}

function Get-PartOneAnswer {
    param(
        [Parameter(Mandatory = $true)]
        [PSCustomObject[]]$Ranges
    )

    [long]$invalidIDs = 0

    foreach ($range in $Ranges) {

        for ($num = $range.Low; $num -le $range.High; $num++) {
                
            # convert num to string
            $numStr = $num.ToString()
            $numLen = $numStr.Length
                
            # check that length of int is even
            if ($numLen % 2 -ne 0) {
                # skip non-even length integers
                continue
            }
        
            # split string
            $half = $numLen / 2
            $left = $numStr.Substring(0, $half)
            $right = $numStr.Substring($half, $half)
        
            # compare each side
            if ($left -eq $right) {
                $invalidIDs += $num
            }
        }
    }

    return $invalidIDs
}

function Get-PartTwoAnswer {
    param(
        [Parameter(Mandatory = $true)]
        [PSCustomObject[]]$Ranges
    )

    [long]$invalidIDs = 0

    foreach ($range in $Ranges) {

        for ($num = $range.Low; $num -le $range.High; $num++) {

            # convert input num to string
            $numStr = $num.ToString()
            $half = [math]::Floor($numStr.Length / 2)
            
            # use regex to compare substrings in numStr
            for ($i = 1; $i -le $half; $i++) {
                $subStr = $numStr.SubString(0, $i)
                if ($numStr -match "^($subStr)+$") {
                    $invalidIDs += $num
                    break
                }
            }
        }
    }

    return $invalidIDs
}

# Main Script
Write-Output "=== Advent of Code (2025, Day 2)"
$sampleFile = ".\sample.txt"
$inputFile = ".\input.txt"

# create array of custom objects
# $ranges = Get-RangesFromFile $sampleFile
$ranges = Get-RangesFromFile $inputFile

$partOneDuration = Measure-Command { $partOne = Get-PartOneAnswer $ranges }
Write-Host "[+] Part One: $partOne ($($partOneDuration.TotalSeconds) seconds)"

$partTwoDuration = Measure-Command { $partTwo = Get-PartTwoAnswer $ranges }
Write-Host "[+] Part Two: $partTwo ($($partTwoDuration.TotalSeconds) seconds)"
