<#
.SYNOPSIS
Advent of Code 2025, Day 3

.NOTES
- Joltage is a value from 1 to 9
#>

function Get-HighestBattery {
    param(
        [string]$subString,
        [int]$Idx
    )

    $returnIndex = 0
    $HighestBattery = 0
    $strLen = $subString.Length

    for ($i = 0; $i -lt ($strLen - $Idx); $i++) {

        # grab character, convert to int
        $currChar = $subString[$i]
        $currCharInt = [int][string]$currChar
   
        # compare current int to highest battery
        if ($currCharInt -gt $HighestBattery) {
            $HighestBattery = $currCharInt
            $returnIndex = $i    
        }
    }  

    return @(
        [string]$HighestBattery, $returnIndex
    )
}

function Get-MaxJoltage {
    param(
        [int]$Iterations,
        [string[]]$BatteryBanks
    )
   
    $Iterations--
    $Answer = 0
    
    $BatteryBanks | ForEach-Object {
        $subString = $_    # store original string
        $AnswerStr = ""    # place holder for final result
        $reverseIdxRange = ($Iterations..0)
        
        # loop through each index and return the highest battery in current bank snippet
        # then set subString to the original string minus the previous index
        $reverseIdxRange | ForEach-Object {

            # retrieve @(highest number string, index) in current battery bank
            $results = Get-HighestBattery -subString $subString -Idx $_
            
            # assign number string to answer string
            $AnswerStr += $results[0]

            # increment index from previous subString to create new subString
            $subString = $subString.Substring(($results[1] + 1))
        }

        $Answer += [long]$AnswerStr 
    }
    return $Answer
}

# Main Script
$sample = ".\sample.txt"
$input = ".\input.txt"
$data = Get-Content -Path $input

$partOne = Get-MaxJoltage 2 $data
$partTwo = Get-MaxJoltage 12 $data

Write-Host "PartOne: $partOne"
Write-Host "PartTwo: $partTwo"