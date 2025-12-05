<#
.SYNOPSIS
Advent of Code 2025, Day 5
#>

function Get-RangesAndIDs {
    param(
        [string]$filePath
    )

    [PSCustomObject[]]$ranges = @()
    [uint64[]]$ids = @()

    $data = Get-Content -Path $filePath

    foreach ($line in $data) {
        if ($line -like "*-*") {
            $parts = $line -split '-'
            $ranges += [PSCustomObject]@{
                Low  = [uint64]$parts[0]
                High = [uint64]$parts[1]
            }
        }
        elseif ($line -match "^\d+$") {
            $ids += [uint64]$line
        }
        else {
            continue
        }
    }

    return [PSCustomObject]@{
        Ranges = $ranges
        IDs    = $ids
    }
}

function Get-FreshIDs {
    param(
        [PSCustomObject[]]$Ranges,
        [uint64[]]$IDs
    )

    $totalFreshIngredients = 0

    foreach ($id in $IDs) {
        foreach ($range in $Ranges) {
            if ($range.Low -le $id -and $id -le $range.High) {
                $totalFreshIngredients++
                break
            }
        }
    }

    return $totalFreshIngredients
}

function Get-ValidRangeCount {
    param(
        [PSCustomObject[]]$Ranges
    )

    $sortedRanges = $Ranges | Sort-Object -Property Low
    
    [uint64]$current = 0  # tracker for last max range value
    $validIds = 0   

    foreach ($newRange in $sortedRanges) {

        # set a current low variable to manipulate
        $currLow = $newRange.Low

        # update current starting low
        if ($currLow -le $current) {
            $currLow = $current + 1
        }

        # if the range is valid, add total elements to fresh ID counter
        if ($currLow -le $newRange.High) {
            $validIds += $newRange.High - $currLow + 1
        }

        # update current variable to last highest value
        $current = [math]::Max($current, $newRange.High)
    }

    return $validIds
}

# Main Script

$sample = ".\sample.txt"
$input = ".\input.txt"

$results = Get-RangesAndIDs -filePath $input

$partOneDuration = Measure-Command { $partOne = Get-FreshIDs -Ranges $results.Ranges -IDs $results.IDs }
Write-Host "[+] Part One: $partOne ($($partOneDuration.TotalSeconds) seconds)"

$partTwoDuration = Measure-Command { $partTwo = Get-ValidRangeCount -Ranges $results.Ranges }
Write-Host "[+] Part Two: $partTwo ($($partTwoDuration.TotalSeconds) seconds)"