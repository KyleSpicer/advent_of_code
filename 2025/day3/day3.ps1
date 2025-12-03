<#
.SYNOPSIS
Advent of Code 2025 Day 3
#>

function Get-JoltagePartOne {
    param(
        [Parameter(Mandatory = $true)]
        [string]$batteryBank
    )
    
    $bankLen = $batteryBank.Length
    $joltage = 0

    for ($i = 0; $i -lt ($bankLen - 1); $i++) {
        $firstNum = [int]([string]$batteryBank[$i])
        
        for ($j = $i + 1; $j -lt $bankLen; $j++) {
            $secondNum = [int]([string]$batteryBank[$j])
            $curr = [int]([string]$firstNum + [string]$secondNum)
            
            if ($curr -gt $joltage) {
                $joltage = $curr
            }
        }
    }
    
    return $joltage
}

function Get-JoltagePartTwo {
    param(
        [Parameter(Mandatory = $true)]
        [string]$batteryBank
    )

    $joltageStr = ""
    $maxNums = 12
    $bankLen = $batteryBank.Length

    # create objects to store digit and index
    $numbersInfo = 0..($bankLen - 1) | ForEach-Object {
        [PSCustomObject]@{
            Index  = $_
            Number = [int][string]$batteryBank[$_]
        }
    }

    # sort array of objects by number
    $numbersInfo = $numbersInfo | Sort-Object Number -Descending

    Write-Host "[info] $($numbersInfo | Out-String)"

    return [int]$joltageStr
}

function Get-TotalJoltage {
    param(
        [Object[]]$Batteries,
        [switch]$first
    )

    $totalJoltage = 0

    foreach ($batteryBank in $Batteries) {
        if ($first) {
            $joltage = Get-JoltagePartOne $batteryBank
            $totalJoltage += $joltage
        }
        else {
            $joltage = Get-JoltagePartTwo $batteryBank
            $totalJoltage += $joltage
        }
    }

    return $totalJoltage
}

# Main Script
$sample = ".\sample.txt"
$input = ".\input.txt"

# get data from file
$data = Get-Content -Path $sample

# $partOneTime = Measure-Command { $partOne = Get-TotalJoltage $data -first }
# Write-Host "[+] Part One: $partOne ($($partOneTime.TotalSeconds) seconds)"

$partTwoTime = Measure-Command { $partTwo = Get-TotalJoltage $data }
Write-Host "[+] Part Two: $partTwo ($($partTwoTime.TotalSeconds) seconds)"